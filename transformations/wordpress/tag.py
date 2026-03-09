import logging
from pathlib import Path
import pandas as pd


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        data = pd.read_parquet(input_filepath)

        # Drop rows where 'tag_count' is '0'
        logging.info("Dropping rows where 'tag_count' is '0'.")
        data = data[data['tag_count'] != '0']

        # Replace NaN values with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Drop the 'tag_count' column
        logging.info("Dropping 'tag_count' column.")
        data = data.drop(columns=['tag_count'])

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
