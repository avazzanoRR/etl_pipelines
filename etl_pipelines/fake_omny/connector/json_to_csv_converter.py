import csv
import json
import logging
from pathlib import Path
from typing import Any


class FakeOmnyJsonToCsvConverter:
    """Converts fake Omny JSON output to CSV."""
    def __init__(self, json_path: str):
        self.json_path = json_path


    def convert_to_csv(self, output_dir: Path, registry: dict[str, Any]) -> None:
        with open(self.json_path, "r") as f:
            data = json.load(f)

        if not data:
            logging.warning("No data to convert to CSV.")
            return
        
        csv_path = output_dir / f"{registry['name']}.csv"
        fieldnames = list(data[0].keys())

        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        logging.info(f"Saved CSV to: {csv_path}")