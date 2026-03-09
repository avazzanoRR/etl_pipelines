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

        # Convert 'tag_created_datetime' to datetime type
        logging.info("Converting 'tag_created_datetime' to datetime.")
        data['tag_created_datetime'] = pd.to_datetime(data['tag_created_datetime'])

        # Replace NaN values with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Add nulled columns with string type
        for col in ['tag_type', 'tag_sub_type']:
            logging.info(f"Adding '{col}' column.")
            data[col] = pd.Series(pd.NA, index=data.index, dtype="string")

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
