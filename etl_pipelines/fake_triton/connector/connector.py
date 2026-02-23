import random
import logging
from datetime import datetime, timedelta
from typing import Any


def _date_range(start_date: str, end_date: str) -> list[str]:
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)
    return dates


DUMMY_VALUES = {
    "station": lambda: random.choice(["WNOM", "WJMD", "WLOL", "WNFT"]),
    "stream_count": lambda: random.randint(100, 50000),
    "total_listening_hours": lambda: round(random.uniform(10, 5000), 2),
    "aqh": lambda: random.randint(50, 10000),
    "cume": lambda: random.randint(500, 100000),
    "avg_session_duration_seconds": lambda: random.randint(60, 7200),
    "unique_listeners": lambda: random.randint(100, 50000),
    "podcast_downloads": lambda: random.randint(50, 20000),
    "podcast_title": lambda: random.choice([
        "Morning Drive Podcast", "Faith & Family",
        "Catholic Perspective", "The Daily Word"
    ]),
    "daypart": None,  # passed through from filters, not generated
}


class FakeTritonConnector:
    """Generates fake Triton streaming analytics shaped data."""

    def fetch_data(self, registry: dict[str, Any]) -> list[dict]:
        fields = registry.get("fields", [])
        start_date = registry.get("start_date", "2025-01-01")
        end_date = registry.get("end_date", "2025-01-07")
        daypart = registry.get("daypart", "")
        dates = _date_range(start_date, end_date)

        results = []
        for date in dates:
            row = {}
            for field in fields:
                if field == "date":
                    row["date"] = date
                elif field == "daypart":
                    row["daypart"] = daypart
                elif field in DUMMY_VALUES and DUMMY_VALUES[field] is not None:
                    row[field] = DUMMY_VALUES[field]()
                else:
                    row[field] = "unknown"
            results.append(row)

        logging.info(f"Generated {len(results)} dummy rows for '{registry['name']}'")
        return results