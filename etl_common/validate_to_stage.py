import logging
import shutil
from pathlib import Path
from importlib import import_module

import pandas as pd

from rr_data_tools.data_validation_ops import LoadDataValidator


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def validate_to_stage(file_path: str, staging_table_class_path: str) -> str:
    """
    Reads a transformed parquet file, validates against the staging table schema.
    
    Parameters:
    - file_path: Path to the transformed parquet file to validate.
    - staging_table_class_path: Dotted path to the SQLAlchemy ORM class representing the staging table schema.
    """
    try:
        df = pd.read_parquet(file_path)

        logging.info(f"Importing staging table class for validation")
        staging_table = _import_class(staging_table_class_path)

        logging.info(f"Validating {file_path} against staging table schema")
        validator = LoadDataValidator(table_class=staging_table)
        validator.validate(df)

        logging.info(f"Validation successful for {file_path}")
        return file_path

    except Exception as e:
        logging.error(f"Validation failed for {file_path}: {e}")
        raise