import shutil
import logging
from pathlib import Path


def quarantine_file(file_path: str, quarantine_dir: str) -> None:
    src = Path(file_path)
    destination = Path(quarantine_dir) / src.name
    shutil.move(src, destination)
    logging.warning(f"Moved {file_path} to quarantine: {destination}")