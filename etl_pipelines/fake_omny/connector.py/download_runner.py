import logging
from typing import Any


class FakeOmnyDownloadRunner:
    """
    Download runner for Source 1.
    In production this would contain real HTTP/API logic specific to this source.
    """

    def __init__(self, download_params: dict[str, Any], verbose: bool=False):
        self.download_params = download_params
        self.verbose = verbose
        self.name = download_params.get("name", "source_1")

    def run(self):
        logging.info(f"[Source1DownloadRunner] Starting download: '{self.name}'")

        if self.verbose:
            logging.info(f"[Source1DownloadRunner] Download parameters: {self.download_params}")

        filters = self.download_params.get("filters", {})
        logging.info(f"[Source1DownloadRunner] Finished downloading '{self.name}'")
