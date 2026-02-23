from typing import Any

from etl_pipelines.base_download_runner import BaseDownloadRunner
from etl_pipelines.fake_triton.connector.connector import FakeTritonConnector
from etl_pipelines.fake_triton.connector.get_download_registry import get_download_registry_path
from etl_pipelines.fake_triton.connector.json_to_csv_converter import FakeTritonJsonToCsvConverter


class FakeTritonDownloadRunner(BaseDownloadRunner):
    """
    Dummy download runner for fake Triton data.
    Orchestrates registry loading, data generation, and saving to disk.
    """
    def _get_registry_path(self, name: str) -> str:
        return get_download_registry_path(name)
    
    def _fetch(self, registry: dict[str, Any]) -> Any:
        connector = FakeTritonConnector()
        return connector.fetch_data(registry)
    
    def _make_converter(self, json_path: str) -> FakeTritonJsonToCsvConverter:
        return FakeTritonJsonToCsvConverter(json_path)