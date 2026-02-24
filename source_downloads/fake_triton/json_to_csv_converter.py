import csv
import json
import logging
from pathlib import Path
from typing import Any


def convert_to_csv(name: str, json_path: str, convert_cfg: dict[str, Any]) -> None:
    """Read JSON file, write filtered CSV to raw directory."""
    with open(json_path, "r") as f:
        data = json.load(f)

    if not data:
        logging.warning(f"No data to convert for '{name}'.")
        return

    raw_dir = Path(convert_cfg.get("raw_dir", "/tmp"))
    raw_dir.mkdir(parents=True, exist_ok=True)

    fieldnames = convert_cfg.get("fields", list(data[0].keys()))
    csv_path = raw_dir / f"{Path(json_path).stem}.csv"

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

    logging.info(f"Saved CSV to: {csv_path}")