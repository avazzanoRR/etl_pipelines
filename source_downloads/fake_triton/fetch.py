from typing import Any
import json
import uuid
import logging
from pathlib import Path
from datetime import datetime

from source_downloads.fake_triton.connector import FakeTritonConnector


def fetch_data(fetch_cfg: dict[str, Any]) -> str:
    """Instantiate connector, fetch data, write to JSON, return file path."""
    connector = FakeTritonConnector()
    results = connector.fetch_data(fetch_cfg)

    output_dir = Path(fetch_cfg.get("source_dir", "/tmp"))
    output_dir.mkdir(parents=True, exist_ok=True)

    name = fetch_cfg.get("name")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    uid = uuid.uuid4().hex[:8]
    json_path = output_dir / f"{name}_{timestamp}_{uid}.json"

    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)

    logging.info(f"Saved JSON to {json_path}")
    return str(json_path)