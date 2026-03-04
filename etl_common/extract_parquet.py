import logging
import shutil
from pathlib import Path
import pandas as pd


def extract_parquet(raw_path: str, processing_dir: str, quarantine_dir: str, columns: list[str]) -> str:
    """
    Reads a parquet file, validates columns, and returns path to the processed file.
    
    Parameters:
    - raw_path: Path to the input parquet file.
    - processing_dir: Directory to write the processed file.
    - quarantine_dir: Directory to move the file if processing fails.
    - columns: List of expected columns in the parquet file.
    """
    processing_dir = Path(processing_dir)
    quarantine_dir = Path(quarantine_dir)
    processing_dir.mkdir(parents=True, exist_ok=True)
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    try:
        logging.info(f"Reading parquet file: {raw_path}")
        df = safe_read_parquet(raw_path)

        logging.info(f"Validating columns in {raw_path}")
        df = validate_and_filter_columns(df, columns)

        staging_path = processing_dir / f"{Path(raw_path).stem}_extract.parquet"
        df.to_parquet(staging_path, index=False)
        logging.info(f"Extract successful. Staged to: {staging_path}")
        return str(staging_path)

    except Exception as e:
        logging.error(f"Extract failed for {raw_path}: {e}")
        quarantine_path = quarantine_dir / Path(raw_path).name
        shutil.move(raw_path, quarantine_path)
        logging.warning(f"Moved {raw_path} to quarantine: {quarantine_path}")
        raise


def safe_read_parquet(file_path: str) -> pd.DataFrame:
    """Reads a parquet file with error handling."""
    try:
        df = pd.read_parquet(file_path)
    except pd.errors.EmptyDataError:
        logging.error(f"{file_path} is empty. Ending extraction process.")
        raise
    except Exception as e:
        logging.error(f"Unexpected error reading {file_path}. Ending extraction process. {e}")
        raise

    if df.empty:
        logging.warning(f"{file_path} contains no data rows.")

    return df


def validate_and_filter_columns(df: pd.DataFrame, expected_columns: list[str]) -> pd.DataFrame:
    """Validates that expected columns are present and drops any extra columns."""
    present_columns = set(df.columns)
    missing_columns = set(expected_columns) - present_columns
    extra_columns = present_columns - set(expected_columns)

    if missing_columns:
        raise ValueError(f"Missing expected columns: {missing_columns}")

    if extra_columns:
        logging.warning(f"Found {len(extra_columns)} unexpected column(s) that are not in schema. Dropping: {extra_columns}")
        df = df.drop(columns=extra_columns)

    return df