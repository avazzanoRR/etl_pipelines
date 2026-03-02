import logging
import shutil
from pathlib import Path
from typing import Any
import pandas as pd
from importlib import import_module
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rr_data_tools.data_validation_ops.load_validation_ops import LoadDataValidator
from rr_data_tools.sql_ops import split_dataframe, insert_in_chunks_parallel
from relevant_radio_etl.registry_schemas import MSSQLConnectionConfig


def _build_engine(database_cfg: dict):
    """Build a SQLAlchemy engine from the database config using MSSQLConnectionConfig."""
    conn_cfg = MSSQLConnectionConfig(**database_cfg["connection"])
    conn_cfg.validate()
    uri = conn_cfg.get_uri()
    return create_engine(uri)


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def stage(file_path: str, stage_cfg: dict[str, Any]) -> str:
    """
    Reads a transformed parquet file, validates against the staging table schema,
    and inserts into the SQL Server staging table in parallel chunks.
    On failure, moves the file to quarantine.
    """
    quarantine_dir = Path(stage_cfg["quarantine_dir"])
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    try:
        df = pd.read_parquet(file_path)

        staging_table = _import_class(stage_cfg["staging_table"])
        base = _import_class(stage_cfg["base"])

        engine = _build_engine(stage_cfg["database"])
        base.metadata.create_all(engine, checkfirst=True)
        session_factory = sessionmaker(bind=engine)

        batch_cfg = stage_cfg.get("batching", {})
        chunk_size = batch_cfg.get("chunk_size", 10000)
        max_workers = batch_cfg.get("max_workers", 5)

        validated_chunks = []
        validator = LoadDataValidator(table_class=staging_table)
        chunks = split_dataframe(df, chunk_size)
        for i, chunk in enumerate(chunks):
            try:
                validator.validate(chunk)
                validated_chunks.append(chunk)
            except Exception as e:
                logging.error(f"Validation failed for chunk {i}: {e}", exc_info=True)
                raise

        insert_in_chunks_parallel(session_factory, validated_chunks, staging_table, max_workers=max_workers)

        logging.info(f"Successfully staged file: {file_path}")
        return file_path
    
    except Exception as e:
        logging.error(f"Stage failed for {file_path}: {e}")
        quarantine_path = quarantine_dir / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved file to quarantine: {quarantine_path}")
        raise