import shutil
import logging
from pathlib import Path


def move_file(file_path: str, dest_dir: str) -> None:
    """Moves a file to the specified destination directory."""
    src = Path(file_path)
    destination_dir = Path(dest_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(src, destination_dir / src.name)
    logging.info(f"Moved {file_path} to {destination_dir / src.name}")