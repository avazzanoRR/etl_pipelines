import logging
from pathlib import Path
import pandas as pd
import hashlib


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        data = pd.read_parquet(input_filepath)

        # Standardize column names to lowercase with underscores instead of spaces
        logging.info("Standardizing column names to lowercase with underscores instead of spaces.")
        data.columns = data.columns.str.lower().str.replace(' ', '_').tolist()

        # Normalize text columns to lowercase and replace spaces with underscores
        logging.info("Normalizing text columns to lowercase and replacing spaces with underscores.")
        data = _standardize_text_columns(data)

        # Filter out rows where gift_type is 'recurring_gift_payment' or 'pledge_payment'
        logging.info("Filtering out rows where gift_type is 'recurring_gift_payment' or 'pledge_payment'.")
        data = data.loc[~(data['gift_type'].isin(['pledge_payment']))].copy()

        # Convert 'gift_date', 'gift_status_date' and 'gift_date_added' to datetime format
        logging.info("Converting 'gift_date', 'gift_status_date' and 'gift_date_added' to datetime format.")
        data['gift_date'] = pd.to_datetime(data['gift_date'], errors='coerce', format='%m/%d/%Y')
        data['gift_date_added'] = pd.to_datetime(data['gift_date_added'], errors='coerce', format='%m/%d/%Y')
        data['gift_status_date'] = pd.to_datetime(data['gift_status_date'], errors='coerce', format='%m/%d/%Y')

        # Convert 'gift_amount' to float after removing any currency symbols and commas
        logging.info("Converting 'gift_amount' to float after removing any currency symbols and commas.")
        data['gift_amount'] = data['gift_amount'].replace(r'[\$,]', '', regex=True).astype(float)

        # Filter out rows where gift_amount is less than or equal to zero
        logging.info("Filtering out rows where gift_amount is less than or equal to zero.")
        data = data.loc[data['gift_amount'] > 0].copy()

        # Map 'gift_installment_frequency' to numerical values
        logging.info("Mapping 'gift_installment_frequency' to numerical values.")
        data['recurring_frequency'] = 1
        data['recurring_frequency'] = data['gift_installment_frequency'].map(
            {
                'single_installment': 1,
                'monthly': 12,
                'quarterly': 4,
                'weekly': 52,
                'semi-monthly': 24,
                'biweekly': 26,
                'bimonthly': 6,
                'annually': 1,
                'semi-anually': 2,
            }
        ).fillna(1).astype("Int64")

        # Calculate 'total_projected_gift_amount'
        logging.info("Calculating 'total_projected_gift_amount'.")
        data['total_projected_gift_amount'] = data['gift_amount']
        data.loc[data['gift_type'] == 'recurring_gift', 'total_projected_gift_amount'] = data['gift_amount'] * data['recurring_frequency']
        data['total_projected_gift_amount'] = data['total_projected_gift_amount'].round(2).astype(float)

        # Create 'market' column based on 'campaign_list' and 'gift_constituency'
        logging.info("Creating 'market' column based on 'campaign_list' and 'gift_constituency'.")
        data['market'] = data['campaign_list']
        data.loc[(data['campaign_list']=='Annual Giving') & (~data['gift_constituency'].isin(['App', 'our website'])), 'market'] = 'Affiliate'
        data.loc[(data['campaign_list']=='Annual Giving') & (data['gift_constituency'].isin(['App', 'our website'])), 'market'] = 'App/Web'

        # Create 'ppm_ind' column based on 'package_list'
        logging.info("Creating 'ppm_ind' column based on 'package_list'.")
        data['ppm_ind'] = 0
        data.loc[data['package_list'].isin(['PrePledgeMailer', 'Pre-Pledge Mailer']), 'ppm_ind'] = 1
        data['ppm_ind'] = data['ppm_ind'].astype("Int64")

        # Deduplicate to keep only the first occurrence of each gift_id based on the earliest gift_date
        data = data.sort_values(by=['gift_id', 'gift_date']).groupby('gift_id', as_index=False).first().copy()

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Fill all blanks in string/object columns with 'not_specified'
        logging.info("Filling all blanks in string/object columns with 'not_specified'.")
        string_cols = data.select_dtypes(include=['string']).columns
        data[string_cols] = data[string_cols].fillna('not_specified')

        # Fill all blanks in numeric columns with 0
        logging.info("Filling all blanks in numeric columns with 0.")
        numeric_cols = data.select_dtypes(include=['number']).columns
        data[numeric_cols] = data[numeric_cols].fillna(0)

        # Add column 'record_active_ind' with default value 1
        logging.info("Adding column 'record_active_ind' with default value 1.")
        data['record_active_ind'] = 1
        data['record_active_ind'] = data['record_active_ind'].astype("Int64")

        # Create a match hash for each row to identify duplicates
        logging.info("Creating a match hash for each row to identify duplicates.")
        data['match_hash'] = data.apply(_create_match_hash, axis=1)
        data['match_hash'] = data['match_hash'].astype('string')

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise


def _standardize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize text columns to lowercase and replace spaces with underscores."""
    logging.info("Standardizing text columns to lowercase and replacing spaces with underscores.")

    df['gift_type'] = df['gift_type'].str.lower().str.replace(' ', '_').str.replace('-', '_').str.replace('(', '').str.replace(')', '').str.replace('/', '_')
    df['gift_subtype'] = df['gift_subtype'].fillna('not_specified').str.lower().str.replace(' ', '_')
    df['gift_installment_frequency'] = df['gift_installment_frequency'].str.lower().str.replace(' ','_')
    df['gift_payment_type'] = df['gift_payment_type'].str.lower().str.replace(' ','_')
    df['gift_status'] = df['gift_status'].str.lower().str.strip()
    df['campaign_list'] = df['campaign_list'].str.replace('Market','').str.strip()
    df['gift_gl_post_status'] = df['gift_gl_post_status'].str.lower().str.replace(' ','_').str.strip()
    df['gift_amount'] = df['gift_amount'].str.replace(',','').str.replace('$','').astype(float)

    return df


def _create_match_hash(row):
    """Create a hash value for a row based on specific columns to identify duplicates."""
    # Concatenate all match key values, handling None/null values
    match_values = [
        str(row['gift_id'] or ''),
        str(row['constituent_id'] or ''),
        str(row['gift_date'] or ''),
        str(row['gift_date_added'] or ''),
        str(row['gift_constituency'] or ''),
        str(row['campaign_list'] or ''),
        str(row['appeal_list'] or ''),
        str(row['package_list'] or ''),
        str(row['fund_list'] or ''),
        str(row['gift_type'] or ''),
        str(row['gift_subtype'] or ''),
        str(row['gift_installment_frequency'] or ''),
        str(row['recurring_frequency'] or ''),
        str(row['gift_amount'] or ''),
        str(row['total_projected_gift_amount'] or ''),
        str(row['market'] or ''),
        str(row['ppm_ind'] or ''),
        str(row['gift_payment_type'] or '')
    ]

    # Create hash from concatenated values
    match_string = '|'.join(match_values)
    return hashlib.md5(match_string.encode('utf-8')).hexdigest()
