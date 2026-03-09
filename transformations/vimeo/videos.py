import logging
from pathlib import Path
import pandas as pd
import numpy as np

from rr_data_tools.transformations import convert_tz_string_to_datetime


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        data = pd.read_parquet(input_filepath)

        # Convert 'video_published_date' to datetime localized to America/Chicago
        logging.info("Converting 'video_published_date' to datetime localized to America/Chicago.")
        data = convert_tz_string_to_datetime(data, column='video_published_date', timezone='America/Chicago')

        # Drop rows where 'video_uri' or 'video_published_date' is NaN
        logging.info("Dropping rows where 'video_uri' or 'video_published_date' is NaN.")
        data = data.dropna(subset=['video_uri', 'video_published_date']).copy()

        # Add indicator columns and assign video program
        logging.info("Adding indicator columns based on 'video_title'.")
        fraa, mass, chaplet = _get_indicator_columns(data['video_title'])
        data['FRAA_Ind'] = fraa
        data['Mass_Ind'] = mass
        data['Chaplet_Ind'] = chaplet

        data['video_program'] = _get_video_program(data)

        # Truncate video titles to 100 characters
        logging.info("Truncating video titles to 100 characters.")
        data['video_title'] = data['video_title'].str[:100]

        # Calculate the total hours viewed
        logging.info("Calculating the total hours viewed.")
        data['total_hours_viewed'] = (data['total_seconds_viewed'] / 3600).round(4).astype("float64")

        # Convert 'average_video_complete' to a percentage
        logging.info("Converting 'average_video_complete_percent' to a percentage.")
        data['average_video_complete_percent'] = (data['average_video_complete_percent'] / 100).round(4).astype("float64")

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


def _get_indicator_columns(search_col: pd.Series):
    fraa_ind = search_col.str.contains('rosary', case=False, na=False).astype(int)
    mass_ind = search_col.str.contains('mass', case=False, na=False).astype(int)
    chaplet_ind = search_col.str.contains('chaplet', case=False, na=False).astype(int)
    return fraa_ind, mass_ind, chaplet_ind


def _get_video_program(data: pd.DataFrame, default='Other') -> pd.Series:
    conditions = [
        data['FRAA_Ind'] == 1,
        data['Mass_Ind'] == 1,
        data['Chaplet_Ind'] == 1
    ]
    choices = ['FRAA', 'Mass', 'Chaplet']
    program_array = np.select(conditions, choices, default=default)
    return pd.Series(program_array, index=data.index).astype('string')
