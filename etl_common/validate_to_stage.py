import logging
import shutil
from pathlib import Path
from typing import Any
from importlib import import_module

import pandas as pd

from rr_data_tools.data_validation_ops import LoadDataValidator


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def validate_to_stage(file_path: str, staging_table_class_path: str, quarantine_dir: str) -> str:
    """
    Reads a transformed parquet file, validates against the staging table schema.
    On failure, moves the file to quarantine.
    
    Parameters:
    - file_path: Path to the transformed parquet file to validate.
    - staging_table_class_path: Dotted path to the SQLAlchemy ORM class representing the staging table schema.
    - quarantine_dir: Directory to move the file if validation fails.
    """
    quarantine_dir = Path(quarantine_dir)
    quarantine_dir.mkdir(parents=True, exist_ok=True)

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
        quarantine_path = quarantine_dir / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved {file_path} to quarantine: {quarantine_path}")
        raise