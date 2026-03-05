import logging
from pathlib import Path
import pandas as pd


def cast_datatypes(file_path: str, output_dir: str, column_types: dict[str, str]) -> str:
    """
    Reads a parquet file, casts columns to specified dtypes, and writes parquet to output_dir.

    Parameters:
    - file_path: Path to the input parquet file.
    - output_dir: Directory to write the processed file.
    - column_types: Dict mapping column names to target dtypes (e.g. {"sessions_per_new_user": "float64"}).
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

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
        cast_path = output_dir / f"{stem}_cast.parquet"
        df.to_parquet(cast_path, index=False)

        logging.info(f"Cast datatypes successful. Written to: {cast_path}")
        return str(cast_path)
    
    except Exception as e:
        logging.error(f"Cast failed for {file_path}: {e}")
        raise
