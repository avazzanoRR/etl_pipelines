import logging
from datetime import datetime
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseDownloadRunner(ABC):
    """
    Abstract base class for download runners.
    Implements the common download flow:
    1) Fetch data
    2) Save to disk (JSON + CSV)

    Subclasses must implement:
    - _fetch()
    - _make_converter()
    """
    def __init__(self, main_config: dict[str, Any], registry: dict[str, Any]):
        self.main_config = main_config
        self.registry = registry
        self.name = registry.get("name", "")

    
    def run(self) -> None:
        logging.info(f"Starting download: '{self.name}'")
        logging.info(f"Resolved registry: {self.registry}")

        logging.info("Fetching data...")
        results = self._fetch(self.registry)

        logging.info("Saving data to disk...")
        self._save(self.registry, results)

        logging.info(f"Finished downloading '{self.name}'")


    @abstractmethod
    def _fetch(self, registry: dict[str, Any]) -> Any:
        """Fetch data. Must be implemented in each subclass."""
        ...


    @abstractmethod
    def _make_converter(self, txt_path: str):
        """Return a converter instance for converting JSON to CSV. Must be implemented in each subclass."""
        ...


    def _save(self, registry: dict[str, Any], results: Any) -> None:
        """Default save: write JSON, then convert to CSV."""
        output_dir = Path(self.main_config.get("output_path", "/tmp"))
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        json_path = output_dir / f"{registry['name']}_{timestamp}.json"
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2)
        logging.info(f"Saved JSON to {json_path}")

        converter = self._make_converter(str(json_path))
        converter.convert_to_csv(output_dir, registry)