import logging
from typing import Any
from importlib import import_module
from sqlalchemy import create_engine

from rr_data_tools.sql_ops import MergeQueryBuilder, execute_merge


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def merge_to_target(staging_table_class_path: str, target_table_class_path: str, database_uri: str, query_params: dict[str, Any]) -> str:
    """
    Merges data from the staging table into the target table.
    Staging table is automatically truncated after a successful merge.
    
    Parameters:
    - staging_table_class_path: Dotted path to the SQLAlchemy ORM class representing the staging table schema.
    - target_table_class_path: Dotted path to the SQLAlchemy ORM class representing the target table schema.
    - database_uri: Database connection URI for SQLAlchemy engine.
    - query_params: Instructions to build the MERGE statement. Includes match_keys, insert_columns, update_columns, etc.
    """
    try:
        staging_table = _import_class(staging_table_class_path)
        target_table = _import_class(target_table_class_path)

        engine = create_engine(database_uri)

        logging.info(f"Building MERGE query")
        merge_builder = MergeQueryBuilder(staging_table, target_table, query_params)
        merge_query = merge_builder.build()
        
        logging.info(f"Executing MERGE query from {staging_table.__tablename__} to {target_table.__tablename__}")
        execute_merge(engine, merge_query, staging_table, target_table)
        logging.info(f"Merge successful from {staging_table.__tablename__} to {target_table.__tablename__}")

    except Exception as e:
        logging.error(f"Merge to target failed for: {e}")
        raise