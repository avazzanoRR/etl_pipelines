import logging
from zipfile import Path
import pandas as pd


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        df = pd.read_parquet(input_filepath)

        # Assign 'Other' as the default value for the 'video_program' column
        logging.info("Assigning default 'Other' to video_program.")
        df['video_program'] = 'Other'

        # Calculate the lifespan of each post in days
        logging.info("Calculating post lifespan in days.")
        df['post_lifespan'] = _calculate_post_lifespan(df['source_data_datetime'], df['published_datetime'])

        # Convert 'video_program' column to string type
        logging.info("Converting 'video_program' column to string type.")
        df['video_program'] = df['video_program'].astype('string')

        # Fill NAs in all numeric columns with 0
        logging.info("Filling NAs in numeric columns with 0.")
        numeric_columns = df.select_dtypes(include=['number']).columns
        df[numeric_columns] = df[numeric_columns].fillna(0)

        # Replace NaNs with None
        logging.info("Replacing NaNs with None.")
        df = df.where(pd.notna(df), None)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise



def _calculate_post_lifespan(report_dt_col: pd.Series, publish_dt_col: pd.Series, timezone_conversion: bool = False) -> pd.Series:
    """Calculates the lifespan of each post in days, given two timestamp series."""
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