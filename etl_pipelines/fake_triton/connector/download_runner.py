from typing import Any

from etl_pipelines.base_download_runner import BaseDownloadRunner
from etl_pipelines.fake_triton.connector.connector import FakeTritonConnector
from etl_pipelines.fake_triton.connector.json_to_csv_converter import FakeTritonJsonToCsvConverter


class FakeTritonDownloadRunner(BaseDownloadRunner):
    """
    Dummy download runner for fake Triton streaming analytics data.
    Orchestrates data generation and saving to disk.
    """

    def _fetch(self, registry: dict[str, Any]) -> list[dict]:
        connector = FakeTritonConnector()
        return connector.fetch_data(registry)

    def _make_converter(self, json_path: str) -> FakeTritonJsonToCsvConverter:
        return FakeTritonJsonToCsvConverter(json_path)