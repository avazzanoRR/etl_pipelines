import logging
import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from rr_data_tools.io_ops import inject_placeholders, load_config


class BaseDownloadRunner(ABC):
    """
    Abstract base class for download runners.
    Implements the common download flow:
    1) Inject placeholders into registry
    2) Fetch data
    3) Save to disk (JSON + CSV)

    Subclasses must implement:
    - _fetch()
    - _make_converter()
    """
    def __init__(self, main_config: dict[str, Any], download_params: dict[str, Any]):
        self.main_config = main_config
        self.download_params = download_params
        self.name = download_params.get("name", "")

    
    def run(self) -> None:
        logging.info(f"Starting download: '{self.name}'")

        registry_path = self._get_registry_path(self.name)
        registry = load_config(Path(registry_path))
        registry = inject_placeholders(registry, **self.download_params.get('filters', {}))

        logging.info(f"Download registry after injecting placeholders: {registry}")

        logging.info("Fetching data...")
        results = self._fetch(registry)

        logging.info("Saving data to disk...")
        self._save(registry, results)

        logging.info(f"Finished downloading '{self.name}'")


    @abstractmethod
    def _get_registry_path(self, name: str) -> str:
        """Return the path to the download registry YAML for the given name."""
        ...


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

        json_path = output_dir / f"{registry['name']}.json"
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2)
        logging.info(f"Saved JSON to {json_path}")

        converter = self._make_converter(str(json_path))
        converter.convert_to_csv(output_dir, registry)