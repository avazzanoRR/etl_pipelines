from typing import Any

from etl_pipelines.base_download_runner import BaseDownloadRunner
from etl_pipelines.fake_google.connector.connector import FakeGoogleConnector
from etl_pipelines.fake_google.connector.json_to_csv_converter import FakeGoogleJsonToCsvConverter


class FakeGoogleDownloadRunner(BaseDownloadRunner):
    """
    Dummy download runner for fake Google Analytics data.
    Orchestrates data generation and saving to disk.
    """
    def _fetch(self, registry: dict[str, Any]) -> Any:
        connector = FakeGoogleConnector()
        return connector.fetch_data(registry)
    
    def _make_converter(self, json_path: str) -> FakeGoogleJsonToCsvConverter:
        return FakeGoogleJsonToCsvConverter(json_path)