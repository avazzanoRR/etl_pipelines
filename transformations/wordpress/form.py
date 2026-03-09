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

        # Add columns with default values 'None'
        for col, dtype in {'ac_campaign_name': 'string', 'special_status': 'Int64', 'digital_campaign_ind': 'Int64', 'address_ind': 'Int64'}.items():
            logging.info(f"Adding column '{col}' with default value None.")
            data[col] = None
            data[col] = data[col].astype(dtype)

        # Add column 'active_status' with default value 1
        logging.info("Adding column 'active_status' with default value 1.")
        data['active_status'] = 1
        data['active_status'] = data['active_status'].astype("Int64")

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
