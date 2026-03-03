import logging
import shutil
from pathlib import Path
from typing import Any

from transformations.parquet_reader import ParquetReader


def extract(file_path: str, extract_cfg: dict[str, Any]) -> str:
    """
    Reads a parquet file, validates columns, casts dtypes, and writes to staging.
    On failure, moves the original file to quarantine.
    
    Parameters:
    - file_path: Path to the input parquet file.
    - extract_cfg: Configuration dict with staging_dir, quarantine_dir, and column_types.
    """
    staging_dir = Path(extract_cfg["staging_dir"])
    quarantine_dir = Path(extract_cfg["quarantine_dir"])
    column_types = extract_cfg["column_types"]

    staging_dir.mkdir(parents=True, exist_ok=True)
    quarantine_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        parquet_file = ParquetReader(file_path)
        df = parquet_file.pd_read_with_validation(column_types)

        # Cast columns to expected dtypes
        for col, dtype in column_types.items():
            df[col] = df[col].astype(dtype)
        
        staging_path = staging_dir / f"{Path(file_path).stem}_extract.parquet"
        df.to_parquet(staging_path, index=False)

        logging.info(f"Extract successful. Staged to: {staging_path}")
        return str(staging_path)
    
    except Exception as e:
        logging.error(f"Extract failed for {file_path}: {e}")
        quarantine_path = quarantine_dir / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved {file_path} to quarantine: {quarantine_path}")
        raise
