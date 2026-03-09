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

        # Add nulled columns with string type
        for col in ['marketing_program_name', 'marketing_program_type', 'marketing_program_sub_type']:
            logging.info(f"Adding '{col}' column.")
            data[col] = pd.Series(pd.NA, index=data.index, dtype="string")

        # Convert string timestamps to datetimes localized to America/Chicago
        for col in ['first_sent_datetime', 'last_sent_datetime', 'scheduled_datetime']:
            logging.info(f"Converting '{col}' to datetime.")
            data = convert_tz_string_to_datetime(data, column=col, timezone='America/Chicago')

        # Drop rows where 'first_sent_datetime' is missing
        logging.info("Dropping rows with missing 'first_sent_datetime'.")
        data = data.dropna(subset=['first_sent_datetime'])

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
