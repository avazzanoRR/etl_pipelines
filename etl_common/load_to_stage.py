import logging
import shutil
from pathlib import Path
from importlib import import_module

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rr_data_tools.sql_ops import split_dataframe, insert_in_chunks_parallel


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def load_to_stage(file_path: str, staging_table_class_path: str, base_class_path: str, quarantine_dir: str, database_uri: str, chunk_size: int = 10000, max_workers: int = 5) -> str:
    """
    Reads a validated parquet file and inserts into SQL Server staging table in parallel chunks.
    On failure, moves the file to quarantine.
    
    Parameters:
    - file_path: Path to the validated parquet file to load.
    - staging_table_class_path: Dotted path to the SQLAlchemy ORM class representing the staging table schema.
    - base_class_path: Dotted path to the SQLAlchemy declarative base class for metadata.
    - quarantine_dir: Directory to move the file if loading fails.
    - database_uri: Database connection URI for SQLAlchemy engine.
    - chunk_size: Number of rows per chunk for parallel insertion.
    - max_workers: Maximum number of parallel workers for insertion.
    """
    quarantine_dir = Path(quarantine_dir)
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    try:
        df = pd.read_parquet(file_path)

        logging.info(f"Importing staging table class and base class")
        staging_table = _import_class(staging_table_class_path)
        base = _import_class(base_class_path)

        logging.info(f"Building SQLAlchemy engine and creating staging table if not exists")
        engine = create_engine(database_uri)
        base.metadata.create_all(engine, checkfirst=True)
        session_factory = sessionmaker(bind=engine)

        logging.info(f"Inserting {file_path} into staging table in parallel chunks")
        chunks = split_dataframe(df, chunk_size)
        insert_in_chunks_parallel(session_factory, chunks, staging_table, max_workers=max_workers)

        logging.info(f"Successfully loaded to stage: {file_path}")
        return file_path

    except Exception as e:
        logging.error(f"Load to stage failed for {file_path}: {e}")
        quarantine_path = quarantine_dir / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved {file_path} to quarantine: {quarantine_path}")
        raise