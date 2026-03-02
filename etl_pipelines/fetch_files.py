import logging
from pathlib import Path


def fetch_files(raw_dir: str) -> list[str]:
    """Fetches all CSV files from the raw directory. Returns a list of file paths."""
    raw_path = Path(raw_dir)
    files = list(raw_path.glob("*.csv"))

    if not files:
        logging.warning(f"No CSV files found in {raw_dir}")
        return []
    
    logging.info(f"Found {len(files)} CSV files in {raw_dir}")
    return [str(f) for f in files]