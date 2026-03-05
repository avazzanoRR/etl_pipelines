import logging
from importlib import import_module

import pandas as pd

from rr_data_tools.data_validation_ops import LoadDataValidator


def _import_class(dotted_path: str):
    """Dynamically import a class from a dotted path string."""
    module_path, class_name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)


def validate_to_stage(input_filepath: str, staging_table_class_path: str) -> str:
    """
    Reads a transformed parquet file, validates against the staging table schema.
    
    Parameters:
    - input_filepath: Path to the transformed parquet file to validate.
    - staging_table_class_path: Dotted path to the SQLAlchemy ORM class representing the staging table schema.
    """
    try:
        df = pd.read_parquet(input_filepath)

        logging.info(f"Importing staging table class for validation")
        staging_table = _import_class(staging_table_class_path)

        logging.info(f"Validating {input_filepath} against staging table schema")
        validator = LoadDataValidator(table_class=staging_table)
        validator.validate(df)

        logging.info(f"Validation successful for {input_filepath}")
        return input_filepath

    except Exception as e:
        logging.error(f"Validation failed for {input_filepath}: {e}")
        raise