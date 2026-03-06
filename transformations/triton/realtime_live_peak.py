import logging
from pathlib import Path
import pandas as pd


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Format 'livestream_datetime' to datetime with format like "07-Jun-2025 03:45 PM"
        logging.info("Converting 'livestream_datetime' to datetime with format like '07-Jun-2025 03:45 PM'.")
        df['livestream_datetime'] = pd.to_datetime(df['livestream_datetime'], format='%d-%b-%Y %I:%M %p')

        # Extract the date from 'livestream_datetime'
        logging.info("Extracting date from 'livestream_datetime'")
        df['livestream_date'] = df['livestream_datetime'].dt.normalize()

        # Extract hour and minute from 'livestream_datetime', then cast to nullable Int64
        logging.info("Extracting hour from 'livestream_datetime'")
        df['livestream_hour'] = df['livestream_datetime'].dt.hour.astype('Int64')
        logging.info("Extracting minute from 'livestream_datetime'")
        df['livestream_minute'] = df['livestream_datetime'].dt.minute.astype('Int64')

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
