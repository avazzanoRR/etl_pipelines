import logging
from pathlib import Path
import pandas as pd


def _safe_divide(numerator, denominator):
    return (numerator / denominator).replace([float('inf'), float('-inf')], None)


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

        # Calculate the page views per user
        logging.info("Calculating page views per user.")
        df['page_views_per_user'] = _safe_divide(df['page_views_count'], df['active_users_count'])

        # Round 'page_views_per_user' and 'avg_time_on_page' to 2 decimal places
        logging.info("Rounding 'page_views_per_user', 'avg_time_on_page', and 'bounce_rate' to 2 decimal places.")
        df['page_views_per_user'] = df['page_views_per_user'].round(2)
        df['avg_time_on_page'] = df['avg_time_on_page'].round(2)
        df['bounce_rate'] = df['bounce_rate'].round(2)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise
