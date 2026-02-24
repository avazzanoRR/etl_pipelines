import csv
import json
import logging
from pathlib import Path
from typing import Any
from datetime import datetime


def convert_to_csv(json_path: str, registry: dict[str, Any], main_config: dict[str, Any]) -> None:
    """Read JSON file, write filtered CSV to output directory."""
    with open(json_path, "r") as f:
        data = json.load(f)

    if not data:
        logging.warning("No data to convert to CSV.")
        return
    
    output_dir = Path(main_config.get("raw_dir", "/tmp"))
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    csv_path = output_dir / f"{registry['name']}_{timestamp}.csv"

    fieldnames = registry.get("fields", list(data[0].keys()))

    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)

    logging.info(f"Saved CSV to: {csv_path}")