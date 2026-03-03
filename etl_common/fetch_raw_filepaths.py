import logging
from pathlib import Path


def fetch_raw_filepaths(raw_dir: str) -> list[str]:
    """Fetches all parquet files from the raw directory. Returns a list of file paths."""
    raw_path = Path(raw_dir)
    files = list(raw_path.glob("*.parquet"))

    if not files:
        logging.warning(f"No parquet files found in {raw_dir}")
        return []
    
    logging.info(f"Found {len(files)} parquet files in {raw_dir}")
    return [str(f) for f in files]