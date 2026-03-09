import logging
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta


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

        # Ensure correct data types
        logging.info("Ensuring correct data types.")
        data['constituent_id'] = data['constituent_id'].astype('string')
        data['gift_status_date'] = pd.to_datetime(data['gift_status_date'], format='%m/%d/%Y', errors='coerce')
        data['gift_date'] = pd.to_datetime(data['gift_date'], format='%m/%d/%Y', errors='coerce')

        # Calculate date range for last year
        logging.info("Filtering to only active or inactive gifts or gifts with a status date in the last year.")
        today = datetime.now()
        one_year_ago = today - timedelta(days=365)

        # Filter to only active or inactive gifts or gifts with a status date in the last year
        data = data.loc[data['gift_status'].isin(['Active', 'Inactive']) | (data['gift_status_date'].between(one_year_ago, today))].copy()
        data = data.sort_values(by=['constituent_id','gift_date'], ascending=[True,False]).groupby('constituent_id').first().reset_index().copy()

        # Add record_active_ind column
        logging.info("Adding record_active_ind column.")
        data['record_active_ind'] = 1
        data['record_active_ind'] = data['record_active_ind'].astype('Int64')

        # Fill all blanks in string/object columns with 'not_specified'
        logging.info("Filling all blanks in string/object columns with 'not_specified'.")
        string_cols = data.select_dtypes(include=['string']).columns
        data[string_cols] = data[string_cols].fillna('not_specified')

        # Fill all blanks in numeric columns with 0
        logging.info("Filling all blanks in numeric columns with 0.")
        numeric_cols = data.select_dtypes(include=['number']).columns
        data[numeric_cols] = data[numeric_cols].fillna(0)

        # Rename columns
        logging.info("Renaming columns for recurring donor status table.")
        data = data.rename(columns={
            'gift_date': 'recurring_gift_start_date',
            'gift_status': 'recurring_gift_status',
            'gift_status_date': 'recurring_gift_status_date'
        })

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
