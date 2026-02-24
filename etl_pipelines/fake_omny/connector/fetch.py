import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Any

from etl_pipelines.fake_omny.connector.connector import FakeOmnyConnector


def fetch_data(name: str, fetch_cfg: dict[str, Any], main_config: dict[str, Any]) -> str:
    """Instantiate connector, fetch data, write to JSON, return file path."""
    connector = FakeOmnyConnector()
    results = connector.fetch_data(fetch_cfg)

    output_dir = Path(main_config.get("source_dir", "/tmp"))
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    json_path = output_dir / f"{name}_{timestamp}.json"

    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)

    logging.info(f"Saved JSON to {json_path}")
    return str(json_path)