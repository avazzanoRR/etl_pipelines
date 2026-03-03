import logging
import shutil
from pathlib import Path
from typing import Any
from importlib import import_module
from sqlalchemy import create_engine

from relevant_radio_etl.registry_schemas import MSSQLConnectionConfig
from rr_data_tools.sql_ops import MergeQueryBuilder, execute_merge


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def _build_engine(database_cfg: dict):
    """Build a SQLAlchemy engine from the database config using MSSQLConnectionConfig."""
    conn_cfg = MSSQLConnectionConfig(**database_cfg["connection"])
    conn_cfg.validate()
    uri = conn_cfg.get_uri()
    return create_engine(uri)


def merge_to_target(file_path: str, merge_cfg: dict[str, Any]) -> str:
    """
    Merges data from the staging table into the target table using a MERGE statement.
    Staging table is automatically truncated after a successful merge.
    """
    try:
        staging_table = _import_class(merge_cfg["staging_table"])
        target_table = _import_class(merge_cfg["target_table"])

        engine = _build_engine(merge_cfg["database"])

        logging.info(f"Building MERGE query")
        merge_builder = MergeQueryBuilder(staging_table, target_table, merge_cfg.get("query_params"))
        merge_query = merge_builder.build()

        logging.info(f"Executing MERGE query from {staging_table.__tablename__} to {target_table.__tablename__}")
        execute_merge(engine, merge_query, staging_table, target_table)
        logging.info(f"Merge successful from {staging_table.__tablename__} to {target_table.__tablename__}")

    except Exception as e:
        logging.error(f"Merge to target failed for {file_path}: {e}")
        raise