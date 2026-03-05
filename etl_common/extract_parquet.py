import logging
from pathlib import Path
import pandas as pd


def extract_parquet(input_filepath: str, output_dir: str, columns: list[str]) -> str:
    """
    Reads a parquet file, validates columns, and returns path to the processed file.
    
    Parameters:
    - input_filepath: Path to the input parquet file.
    - output_dir: Directory to write the processed file.
    - columns: List of expected columns in the parquet file.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        logging.info(f"Reading parquet file: {input_filepath}")
        df = safe_read_parquet(input_filepath)

        logging.info(f"Validating columns in {input_filepath}")
        df = validate_and_filter_columns(df, columns)

        staging_path = output_dir / f"{Path(input_filepath).stem}_extract.parquet"
        df.to_parquet(staging_path, index=False)
        logging.info(f"Extract successful. Staged to: {staging_path}")
        return str(staging_path)

    except Exception as e:
        logging.error(f"Extract failed for {input_filepath}: {e}")
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