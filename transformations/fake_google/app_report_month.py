import logging
from pathlib import Path

import pandas as pd


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        df = pd.read_parquet(input_filepath)

        # Rename columns to snake_case
        logging.info(f"Renaming columns")
        df = df.rename(columns={"newUsers": "new_users", "sessions": "total_sessions"})

        # Add a calculated column
        logging.info(f"Calculating sessions_per_new_user")
        df["sessions_per_new_user"] = (df["total_sessions"] / df["new_users"])

        # Round sessions_per_new_user to 2 decimal places
        df["sessions_per_new_user"] = df["sessions_per_new_user"].round(2).astype("float64")


        stem = Path(input_filepath).stem.replace("_extract", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)
    
    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise