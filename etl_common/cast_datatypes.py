import logging
from typing import Any
from pathlib import Path
import shutil
import pandas as pd


def cast_datatypes(file_path: str, cast_cfg: dict[str, Any]) -> str:
    """
    Reads a staged parquet file, casts columns to specified dtypes, and writes back to staging.
    On failure, moves the file to quarantine.
    
    Parameters:
    - file_path: Path to the extracted parquet file.
    - cast_cfg: Configuration dict with staging_dir, quarantine_dir, and column_types.
    """
    staging_dir = Path(cast_cfg["staging_dir"])
    quarantine_dir = Path(cast_cfg["quarantine_dir"])
    column_types = cast_cfg["column_types"]

    staging_dir.mkdir(parents=True, exist_ok=True)
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    try:
        df = pd.read_parquet(file_path)

        for col, dtype in column_types.items():
            if col in df.columns:
                try:
                    df[col] = df[col].astype(dtype)
                except Exception as e:
                    logging.error(f"Failed to cast column {col} to {dtype}: {e}")
                    raise
            else:
                raise KeyError(f"Column {col} not found in DataFrame for dtype casting.")
    
        stem = Path(file_path).stem.replace("_extract", "")
        cast_path = staging_dir / f"{stem}_cast.parquet"
        df.to_parquet(cast_path, index=False)

        logging.info(f"Cast datatypes successful. Written to: {cast_path}")
        return str(cast_path)
    
    except Exception as e:
        logging.error(f"Cast failed for {file_path}: {e}")
        quarantine_path = quarantine_dir / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved {file_path} to quarantine: {quarantine_path}")
        raise
