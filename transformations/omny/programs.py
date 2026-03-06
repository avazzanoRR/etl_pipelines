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

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        df = df.where(pd.notna(df), None)

        # Cap the 'program_description' at 1000 characters
        logging.info("Capping 'program_description' at 1000 characters.")
        df['program_description'] = df['program_description'].str.slice(0, 1000)

        # Save transformed file to output directory
        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
