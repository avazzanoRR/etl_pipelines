import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Any

from etl_pipelines.fake_triton.connector.connector import FakeTritonConnector


def fetch_data(registry: dict[str, Any], main_config: dict[str, Any]) -> str:
    """Instantiate connector, fetch data, write to JSON, return file path."""
    connector = FakeTritonConnector()
    results = connector.fetch_data(registry)

    output_dir = Path(main_config.get("output_path", "/tmp"))
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    json_path = output_dir / f"{registry['name']}_{timestamp}.json"

    with open(json_path, "w") as f:
        json.dump(results, f, indent=2)

    logging.info(f"Saved JSON to: {json_path}")
    return str(json_path)