import logging
from pathlib import Path
import pandas as pd

from rr_data_tools.transformations import convert_tz_string_to_datetime


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        data = pd.read_parquet(input_filepath)

        # Drop rows where 'list_status_id' equals 1
        logging.info("Dropping rows where 'list_status_id' equals 1.")
        data = data[data['list_status_id'] != 1]

        # Replace NaN values with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Lowercase the 'unsubscribe_reason' column
        logging.info("Converting the 'unsubscribe_reason' column to lowercase.")
        data['unsubscribe_reason'] = data['unsubscribe_reason'].str.lower()

        # Convert string timestamps to datetimes localized to America/Chicago
        logging.info("Converting the 'list_status_updated_timestamp' column to datetime.")
        data = convert_tz_string_to_datetime(data, column='list_status_updated_timestamp', timezone='America/Chicago')

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
