import logging
from pathlib import Path
import pandas as pd


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

        # Drop rows where page_path is None
        logging.info("Dropping rows where page_path is None.")
        df = df.dropna(subset=['page_path'])

        # Split the page path into 3 levels
        logging.info("Splitting page path into hierarchical levels.")
        level1, level2, level3 = _split_page_path(df['page_path'])
        df['page_path_level_1'] = level1
        df['page_path_level_2'] = level2
        df['page_path_level_3'] = level3

        # Calculate the page views per user
        logging.info("Calculating page views per user.")
        df['page_views_per_user'] = _safe_divide(df['page_views_count'], df['active_users_count'])

        # Calculate the average engagement time per user
        logging.info("Calculating average engagement time per user.")
        df['avg_engagement_time'] = _safe_divide(df['user_engagement_duration'], df['active_users_count'])

        # Round 'page_views_per_user' and 'avg_engagement_time' to 2 decimal places
        logging.info("Rounding 'page_views_per_user' and 'avg_engagement_time' to 2 decimal places.")
        df['page_views_per_user'] = df['page_views_per_user'].round(2)
        df['avg_engagement_time'] = df['avg_engagement_time'].round(2)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        df.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise


def _safe_divide(numerator, denominator):
    return (numerator / denominator).replace([float('inf'), float('-inf')], None)


def _split_page_path(col: pd.Series):
    '''Split page path into three hierarchical levels.'''
    parts = (
        col
        .fillna('')  # replace missing entries with empty strings
        .str.strip('/')  # remove leading/trailing slashes
        .str.split('/', expand=True)  # split each path by '/' into columns
        .fillna('')  # ensure no NaN in any segment
    )

    # Ensure exactly three segments by adding empty columns if fewer exist
    for i in range(3):
        if i not in parts:
            parts[i] = ''

    # Format each segment with surrounding slashes (or empty if missing)
    level1 = parts[0].map(lambda x: f'/{x}/' if x else '').astype("string")
    level2 = parts[1].map(lambda x: f'/{x}/' if x else '').astype("string")
    level3 = parts[2].map(lambda x: f'/{x}/' if x else '').astype("string")
    return level1, level2, level3