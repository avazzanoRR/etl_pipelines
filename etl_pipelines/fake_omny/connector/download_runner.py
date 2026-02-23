from typing import Any

from etl_pipelines.base_download_runner import BaseDownloadRunner
from etl_pipelines.fake_omny.connector.connector import FakeOmnyConnector
from etl_pipelines.fake_omny.connector.json_to_csv_converter import FakeOmnyJsonToCsvConverter


class FakeOmnyDownloadRunner(BaseDownloadRunner):
    """
    Dummy download runner for fake Omny podcast analytics data.
    Orchestrates data generation and saving to disk.
    """

    def _fetch(self, registry: dict[str, Any]) -> list[dict]:
        connector = FakeOmnyConnector()
        return connector.fetch_data(registry)

    def _make_converter(self, json_path: str) -> FakeOmnyJsonToCsvConverter:
        return FakeOmnyJsonToCsvConverter(json_path)