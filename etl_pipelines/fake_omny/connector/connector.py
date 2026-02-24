import random
import logging
from datetime import datetime, timedelta
from typing import Any


DUMMY_VALUES = {
    "episode_id": lambda: f"EP{random.randint(1000, 9999)}",
    "episode_title": lambda: random.choice([
        "Morning Reflection", "Daily Devotional", "Faith & Life",
        "Sunday Homily", "Catholic Answers", "The Word Today"
    ]),
    "plays": lambda: random.randint(50, 10000),
    "unique_listeners": lambda: random.randint(30, 8000),
    "avg_listen_duration_seconds": lambda: random.randint(60, 3600),
    "completion_rate": lambda: round(random.uniform(0.1, 1.0), 4),
    "downloads": lambda: random.randint(50, 15000),
    "shares": lambda: random.randint(0, 500),
    "clip_title": lambda: random.choice([
        "Clip: Morning Prayer", "Clip: Gospel Reading",
        "Clip: Homily Highlight", "Clip: Reflection"
    ]),
    "clip_plays": lambda: random.randint(10, 2000),
    "clip_duration_seconds": lambda: random.randint(15, 180),
}


class FakeOmnyConnector:
    """Generates fake Omny shaped data."""
    def fetch_data(self, registry: dict[str, Any]) -> list[dict[str, Any]]:
        start_date = registry.get("start_date", "2025-01-01")
        end_date = registry.get("end_date", "2025-01-07")
        dates = self._date_range(start_date, end_date)

        results = []
        for date in dates:
            row = {"date": date}
            for field, generator in DUMMY_VALUES.items():
                row[field] = generator()
            results.append(row)

        logging.info(f"Fetched {len(results)} rows of data.")
        return results
    

    def _date_range(self, start_date: str, end_date: str) -> list[str]:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        dates = []
        current = start
        while current <= end:
            dates.append(current.strftime("%Y-%m-%d"))
            current += timedelta(days=1)
        return dates