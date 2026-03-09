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

        # Fill blanks in 'video_title' with 'No Title'
        logging.info("Filling blanks in 'video_title' with 'No Title'.")
        data['video_title'] = data['video_title'].fillna('No Title')

        # Assign 'Other' as the default value for the 'video_program' column
        logging.info("Assigning default 'Other' to video_program.")
        data['video_program'] = 'Other'

        # Extract TikTok video ID from the 'Video link' column
        logging.info("Extracting TikTok video ID from 'video_link'.")
        data['tiktok_video_id'] = data['video_link'].str.split('/').str[5].astype("string")

        # Calculate the lifespan of each post in days
        logging.info("Calculating post lifespan in days.")
        data['post_lifespan'] = _calculate_post_lifespan(data['source_data_datetime'], data['published_datetime'])

        # Recast string columns that went through transformations (to ensure they are 'string' dtype instead of 'object')
        logging.info("Recasting string columns to 'string' dtype")
        string_columns = ['tiktok_video_id', 'video_title', 'video_program']
        data[string_columns] = data[string_columns].astype('string')

        # Fill NAs in all numeric columns with 0
        logging.info("Filling NAs in numeric columns with 0.")
        numeric_columns = data.select_dtypes(include=['number']).columns
        data[numeric_columns] = data[numeric_columns].fillna(0)

        # Replace NaNs with None
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


def _calculate_post_lifespan(report_dt_col: pd.Series, publish_dt_col: pd.Series, timezone_conversion: bool = False) -> pd.Series:
    '''Calculates the lifespan of each post in days, given two timestamp series.'''
    # Ensure both series are datetimes
    report_dt_col = pd.to_datetime(report_dt_col, errors='coerce')
    publish_dt_col = pd.to_datetime(publish_dt_col, errors='coerce')

    # Optional timezone conversion, then drop the tz
    if timezone_conversion:
        publish_dt_col = publish_dt_col.dt.tz_convert('America/Chicago').tz_localize(None)

    # Compute lifespan in days
    lifespan = (report_dt_col - publish_dt_col).dt.days + 1

    # Convert to Int64 to preserve nulls
    return lifespan.astype('Int64')
