import csv
import json
import logging
from pathlib import Path
from typing import Any


def convert_to_csv(json_path: str, registry: dict[str, Any], main_config: dict[str, Any]) -> None:
    """Read JSON file, write filtered CSV to output directory."""
    with open(json_path, "r") as f:
        data = json.load(f)

    if not data:
        logging.warning("No data to convert to CSV.")
        return

    output_dir = Path(main_config.get("output_path", "/tmp"))
    output_dir.mkdir(parents=True, exist_ok=True)

    fieldnames = registry.get("fields", list(data[0].keys()))
    csv_path = output_dir / f"{Path(json_path).stem}.csv"

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

    logging.info(f"Saved CSV to: {csv_path}")