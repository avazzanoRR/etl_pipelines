import shutil
import logging
from pathlib import Path


def quarantine_file(file_path: str, quarantine_dir: str) -> None:
    # Create the quarantine directory if it doesn't exist
    quarantine_dir = Path(quarantine_dir)
    quarantine_dir.mkdir(parents=True, exist_ok=True)

    # Move the file to the quarantine directory
    src = Path(file_path)
    destination = Path(quarantine_dir) / src.name
    shutil.move(src, destination)
    logging.warning(f"Moved {file_path} to quarantine: {destination}")