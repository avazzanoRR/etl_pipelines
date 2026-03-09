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

        # Convert string timestamps to datetimes localized to America/Chicago
        logging.info("Converting 'message_created_datetime' to datetime.")
        data = convert_tz_string_to_datetime(data, column='message_created_datetime', timezone='America/Chicago')

        # Drop rows where 'message_created_datetime' is missing
        logging.info("Dropping rows with missing 'message_created_datetime'.")
        data = data.dropna(subset=['message_created_datetime'])

        # Replace NaN values with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
