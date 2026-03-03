import logging
import shutil
from pathlib import Path
from typing import Any
from importlib import import_module

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rr_data_tools.sql_ops import split_dataframe, insert_in_chunks_parallel
from relevant_radio_etl.registry_schemas import MSSQLConnectionConfig


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def _build_engine(database_cfg: dict) -> sqlalchemy.engine.base.Engine:
    """Build a SQLAlchemy engine from the database config using MSSQLConnectionConfig."""
    conn_cfg = MSSQLConnectionConfig(**database_cfg["connection"])
    conn_cfg.validate()
    uri = conn_cfg.get_uri()
    return create_engine(uri)


def load_to_stage(file_path: str, stage_cfg: dict[str, Any]) -> str:
    """
    Reads a validated parquet file and inserts into SQL Server staging table in parallel chunks.
    Checks that the staging table is empty before inserting to prevent data pile-up and duplicates.
    On failure, moves the file to quarantine.
    """
    quarantine = Path(stage_cfg["quarantine_dir"])
    quarantine.mkdir(parents=True, exist_ok=True)

    try:
        df = pd.read_parquet(file_path)

        logging.info(f"Importing staging table class and base")
        staging_table = _import_class(stage_cfg["staging_table"])
        base = _import_class(stage_cfg["base"])

        logging.info(f"Building engine and creating staging table if not exists")
        engine = _build_engine(stage_cfg["database"])
        base.metadata.create_all(engine, checkfirst=True)
        session_factory = sessionmaker(bind=engine)

        logging.info(f"Checking staging table is empty before loading")
        with engine.connect() as conn:
            count = conn.execute(sqlalchemy.text(f"SELECT COUNT(*) FROM {staging_table.__tablename__}")).scalar()
            if count > 0:
                raise RuntimeError(
                    f"Staging table '{staging_table.__tablename__}' is not empty (contains {count} rows). "
                    f"A previous load_to_target may have failed. Please investigate and truncate manually before re-running."
                )
        
        batch_cfg = stage_cfg.get("batching", {})
        chunk_size = batch_cfg.get("chunk_size", 10000)
        max_workers = batch_cfg.get("max_workers", 5)

        logging.info(f"Inserting {file_path} into staging table in parallel chunks")
        chunks = split_dataframe(df, chunk_size)
        insert_in_chunks_parallel(session_factory, chunks, staging_table, max_workers=max_workers)

        logging.info(f"Successfully loaded {file_path} to staging table {staging_table.__tablename__}")
        return file_path
    
    except Exception as e:
        logging.error(f"Load to stage failed for {file_path}: {e}")
        quarantine_path = quarantine / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved {file_path} to quarantine: {quarantine_path}")
        raise