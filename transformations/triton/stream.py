import logging
from pathlib import Path
import pandas as pd
from rr_data_tools.transformations import calculate_period_type


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Replace NaNs with None
        logging.info("Replacing NaNs with None")
        df = df.where(pd.notna(df), None)

        # Calculate the period type between 'reporting_date_start' and 'reporting_date_end'
        logging.info("Calculating 'period_type' between 'reporting_date_start' and 'reporting_date_end'.")
        df['period_type'] = calculate_period_type(df['reporting_date_start'], df['reporting_date_end']).astype('string')

        # Round 'tlh' and 'aas' to 2 decimal places
        logging.info("Rounding 'tlh' and 'aas' to 2 decimal places.")
        df['tlh'] = df['tlh'].round(2)
        df['aas'] = df['aas'].round(2)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
