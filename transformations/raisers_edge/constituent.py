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

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Standardize column names to lowercase with underscores instead of spaces
        logging.info("Standardizing column names to lowercase with underscores instead of spaces.")
        data.columns = data.columns.str.lower().str.replace(' ', '_').tolist()

        # Strip whitespace from all string columns
        data = _strip_whitespace_from_string_columns(data)

        # Convert 'constituent_date_added' and 'constituent_date_last_changed' to datetime format
        logging.info("Converting 'constituent_date_added' and 'constituent_date_last_changed' to datetime format.")
        data['constituent_date_added'] = pd.to_datetime(data['constituent_date_added'], errors='coerce', format='%m/%d/%Y')
        data['constituent_date_last_changed'] = pd.to_datetime(data['constituent_date_last_changed'], errors='coerce', format='%m/%d/%Y')

        # Keep only the most recent record for each constituent_id based on constituent_date_added
        logging.info("Keeping only the most recent record for each constituent_id based on constituent_date_added.")
        data = data.sort_values(by=['constituent_id', 'constituent_date_added'], ascending=[True, False]).groupby('constituent_id').first().reset_index().copy()

        # Convert 'constituent_id' to string type
        logging.info("Converting 'constituent_id' to string type.")
        data['constituent_id'] = data['constituent_id'].astype('string')

        # Fill all blanks in string/object columns with 'not_specified'
        logging.info("Filling all blanks in string/object columns with 'not_specified'.")
        string_cols = data.select_dtypes(include=['string']).columns
        data[string_cols] = data[string_cols].fillna('not_specified')

        # Add column 'record_active_ind' with default value 1
        logging.info("Adding column 'record_active_ind' with default value 1.")
        data['record_active_ind'] = 1
        data['record_active_ind'] = data['record_active_ind'].astype("Int64")

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise


def _strip_whitespace_from_string_columns(df: pd.DataFrame) -> pd.DataFrame:
    str_cols = df.select_dtypes(include=['object', 'string']).columns
    for col in str_cols:
        df[col] = df[col].str.strip()
    return df
