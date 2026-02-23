import logging
from typing import Any
from pathlib import Path

from etl_pipelines.fake_triton.connector.get_download_registry import get_download_registry_path
from rr_data_tools.io_ops import inject_placeholders
from rr_data_tools.io_ops import load_config


class FakeGoogleDownloadRunner:
    """
    Download runner for Google.
    In production this would contain real HTTP/API logic specific to this source.
    """

    def __init__(self, main_config: dict[str, Any], download_params: dict[str, Any], verbose: bool=False):
        self.main_config = main_config
        self.download_params = download_params
        self.verbose = verbose
        self.name = download_params.get("name", "")

    def run(self):
        logging.info(f"Starting download: '{self.name}'")
        logging.info(f"Config contents: {self.main_config}")

        if self.verbose:
            logging.info(f"Download parameters: {self.download_params}")

        # Inject placeholders into download registry YAML
        registry_path = get_download_registry_path(self.name)
        registry = load_config(Path(registry_path))
        registry = inject_placeholders(registry, **self.download_params.get('filters', {}))

        logging.info(f"Download registry after injecting placeholders: {registry}")

        logging.info(f"Finished downloading '{self.name}'")