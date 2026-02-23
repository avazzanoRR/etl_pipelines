import random
import logging
from datetime import datetime, timedelta
from typing import Any


DUMMY_VALUES = {
    "page_path": lambda: random.choice(["/home", "/about", "/contact", "/blog"]),
    "sessions": lambda: random.randint(100, 5000),
    "bounceRate": lambda: round(random.uniform(0.2, 0.8), 4),
    "avgSessionDuration": lambda: round(random.uniform(30, 300), 2),
    "newUsers": lambda: random.randint(50, 2000),
    "pageviews": lambda: random.randint(200, 10000),
    "landingPage": lambda: random.choice(["/", "/blog", "/pricing", "/contact"]),
    "conversions": lambda: random.randint(0, 200),
}


class FakeGoogleConnector:
    """Generates fake Google Analytics data."""
    def fetch_data(self, registry: dict[str, Any]) -> list[dict[str, Any]]:
        fields = registry.get("fields", [])
        start_date = registry.get("start_date", "2025-01-01")
        end_date = registry.get("end_date", "2025-01-07")
        dates = self._date_range(start_date, end_date)

        results = []
        for date in dates:
            row = {}
            for field in fields:
                if field == "date":
                    row["date"] = date
                elif field in DUMMY_VALUES:
                    row[field] = DUMMY_VALUES[field]()
                else:
                    row[field] = "unknown"
            results.append(row)

        logging.info(f"Fetched {len(results)} rows of data.")
        return results
    

    def _date_range(self, start_date: str, end_date: str) -> list[str]:
        """Generate a list of date strings between start_date and end_date."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        dates = []
        current = start
        while current <= end:
            dates.append(current.strftime("%Y-%m-%d"))
            current += timedelta(days=1)
        return dates