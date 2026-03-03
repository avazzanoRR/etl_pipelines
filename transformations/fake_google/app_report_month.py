import logging
import shutil
from pathlib import Path
from typing import Any

import pandas as pd


def transform(file_path: str, transform_cfg: dict[str, Any]) -> str:
    """Transforms a parquet file."""
    staging_dir = Path(transform_cfg["staging_dir"])
    quarantine_dir = Path(transform_cfg["quarantine_dir"])

    staging_dir.mkdir(parents=True, exist_ok=True)
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    try:
        df = pd.read_parquet(file_path)

        # Rename columns to snake_case
        logging.info(f"Renaming columns")
        df = df.rename(columns={"newUsers": "new_users", "sessions": "total_sessions"})

        # Add a calculated column
        logging.info(f"Calculating sessions_per_new_user")
        df["sessions_per_new_user"] = (df["total_sessions"] / df["new_users"])

        # Round sessions_per_new_user to 2 decimal places
        df["sessions_per_new_user"] = df["sessions_per_new_user"].round(2).astype("float64")


        stem = Path(file_path).stem.replace("_extract", "")
        transformed_path = staging_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)
    
    except Exception as e:
        logging.error(f"Transform failed for {file_path}: {e}")
        quarantine_path = quarantine_dir / Path(file_path).name
        shutil.move(file_path, quarantine_path)
        logging.warning(f"Moved failed file to quarantine: {quarantine_path}")
        raise