import logging
import sqlalchemy
from typing import Any
from importlib import import_module
from sqlalchemy import create_engine

from relevant_radio_etl.registry_schemas import MSSQLConnectionConfig


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


def check_stage_empty(check_cfg: dict[str, Any]) -> None:
    """
    Checks that the staging table is empty before loading begins.
    Raises if the staging table contains rows from a previous failed run.
    """
    try:
        staging_table = _import_class(check_cfg["staging_table"])
        engine = _build_engine(check_cfg["database"])

        with engine.connect() as conn:
            count = conn.execute(sqlalchemy.text(f"SELECT COUNT(*) FROM {staging_table.__tablename__}")).scalar()
            if count > 0:
                raise RuntimeError(
                    f"Staging table '{staging_table.__tablename__}' is not empty ({count} rows). "
                    f"Previous merge_to_target may have failed. Please investigate and truncate manually before re-running."
                )

        logging.info(f"Staging table '{staging_table.__tablename__}' is empty. Proceeding with load.")

    except Exception as e:
        logging.error(f"check_stage_empty failed: {e}")
        raise