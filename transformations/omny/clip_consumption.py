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

        # Define metric columns
        metric_cols = [
            'time_spent_listening',
            'listened_to_25_percent',
            'listened_to_50_percent',
            'listened_to_75_percent',
            'listened_to_100_percent',
            'average_completion'
        ]

        # Remove rows where all metric values are null
        initial_row_count = len(df)
        logging.info(f"Initial row count: {initial_row_count}")

        df = df.dropna(subset=metric_cols, how='all')

        rows_removed = initial_row_count - len(df)
        logging.info(f"Removed {rows_removed} rows with all blank metric values. Remaining rows: {len(df)}")

        # Replace remaining NaNs with None
        logging.info("Replacing NaNs with None.")
        df = df.where(pd.notna(df), None)

        # Round all float columns to 4 decimal places
        for col in metric_cols:
            logging.info(f"Rounding '{col}' to 4 decimal places")
            df[col] = df[col].round(4)

        # Save transformed file to output directory
        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
