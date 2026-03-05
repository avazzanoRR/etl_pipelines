import logging
from importlib import import_module
from sqlalchemy import create_engine


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def create_tables(base_class_path: str, database_uri: str) -> None:
    """
    Creates tables in the database based on the SQLAlchemy declarative base class.
    
    Parameters:
    - base_class_path: Dotted path to the SQLAlchemy declarative base class for metadata.
    - database_uri: Database connection URI for SQLAlchemy engine.
    """
    base = _import_class(base_class_path)
    engine = create_engine(database_uri)

    for table_name in base.metadata.tables:
        logging.info(f"Creating {table_name} table if it does not exist")

    base.metadata.create_all(engine, checkfirst=True)
    logging.info(f"Tables created successfully in the database")