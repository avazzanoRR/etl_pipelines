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

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Lowercase the email address column
        logging.info("Converting the email_address column to lowercase.")
        data['email_address'] = data['email_address'].str.lower()

        # Title-case the name columns
        for col in ['first_name', 'last_name']:
            logging.info(f"Converting '{col}' to title-case.")
            data[col] = data[col].str.title()

        # Convert string timestamps to datetimes localized to America/Chicago
        for col in ['created_timestamp', 'updated_timestamp']:
            logging.info(f"Converting the '{col}' column to datetime.")
            data = convert_tz_string_to_datetime(data, column=col, timezone='America/Chicago')

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
