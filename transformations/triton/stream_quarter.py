import logging
from pathlib import Path
import pandas as pd
import relevant_radio_etl as rretl


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Duplicate 'reporting_date_end' column as 'run_month' and insert it as the first column
        df.insert(0, 'run_month', df['reporting_date_end'])

        df = (
            df.pipe(rretl.replace_nan_with_none)  # convert pandas "NaN" to "None" (represents SQL "NULL")
              .pipe(rretl.convert_blank_to_null)  # replace all blanks with "None"
              .pipe(rretl.get_run_month, 'run_month')
        )

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
