import ast
import logging
from pathlib import Path
import pandas as pd
from typing import Optional

from rr_data_tools.transformations import convert_tz_string_to_datetime, format_unicode_characters


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

        # Convert string timestamps to datetime localized to America/Chicago
        logging.info("Converting 'published_utc' to datetime.")
        df = convert_tz_string_to_datetime(df, 'published_utc', 'America/Chicago')

        # Format special unicode characters
        logging.info("Formatting unicode characters in 'clip_title'.")
        df['clip_title'] = format_unicode_characters(df['clip_title'])

        # Replace newlines with semicolons in 'clip_description'
        logging.info("Replacing newlines with semicolons in 'clip_description'.")
        df['clip_description'] = df['clip_description'].str.replace('\n', ';', regex=False)

        # Format the tags into a string instead of a list
        logging.info("Formatting tags in 'clip_tags'.")
        df['clip_tags'] = _format_tags(df['clip_tags'])

        # Cap the tags at 100 characters
        logging.info("Capping 'clip_tags' at 100 characters and converting it to string dtype.")
        df['clip_tags'] = df['clip_tags'].str.slice(0, 100).astype('string')

        # Replace nulls in 'clip_duration_seconds' with 0.00, then round to 2 decimal places
        logging.info("Replacing nulls in 'clip_duration_seconds' with 0.00 and rounding to 2 decimal places.")
        df['clip_duration_seconds'] = df['clip_duration_seconds'].fillna(0.00).round(2)

        # Save transformed file to output directory
        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise


def _format_tags(col: pd.Series) -> pd.Series:
    '''
    Turn a stringified Python list into a comma-joined string.
    Empty or missing lists become None.
    '''
    def _fmt(val: Optional[str]) -> Optional[str]:
        if not val:
            return None
        items = ast.literal_eval(val)
        return ', '.join(items) if items else None
    return col.apply(_fmt)