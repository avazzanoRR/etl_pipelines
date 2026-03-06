import logging
from pathlib import Path
import pandas as pd
from rr_data_tools.transformations import get_reporting_week


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        df = df.where(pd.notna(df), None)

        # Calculate the reporting week based on the reporting date
        logging.info("Calculating 'reporting_week' from 'reporting_date'.")
        df['reporting_week'] = get_reporting_week(df['reporting_date'])

        # Round 'downloaded_hours' to 2 decimal places
        logging.info("Rounding 'downloaded_hours' to 2 decimal places.")
        df['downloaded_hours'] = df['downloaded_hours'].round(2)

        # Replace all blanks/nulls in 'dma' and 'episode_title' to the string 'N/A'
        logging.info("Converting blank and None values in 'dma' and 'episode_title' to 'N/A'.")
        df['dma'] = df['dma'].replace("", pd.NA).fillna("N/A")
        df['episode_title'] = df['episode_title'].replace("", pd.NA).fillna("N/A")

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
