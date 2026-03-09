import logging
from pathlib import Path
import ast
import pandas as pd
from sqlalchemy.engine import Engine


def transform(input_filepath: str, output_dir: str, engine=None) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        data = pd.read_parquet(input_filepath)

        # Replace NaN values with None
        logging.info("Replacing NaNs with None.")
        data = data.where(pd.notna(data), None)

        # Map category IDs to category names
        logging.info("Mapping category IDs to category names.")
        data = _map_categories(data, engine=engine)

        # Map tag IDs to tag names
        logging.info("Mapping tag IDs to tag names.")
        data = _map_tags(data, engine=engine)

        # Create columns for GA path levels
        logging.info("Creating GA path level columns.")
        data = _get_ga_path_level(data, column_name='url_path')

        # Create column for word count
        logging.info("Creating word count column.")
        data = _get_word_count(data, column_name='yoast_head_json_schema')

        # Truncate post_title and url_path to 100 characters
        logging.info("Truncating 'post_title' and 'url_path' to 100 characters.")
        data['post_title'] = data['post_title'].str.slice(0, 100)
        data['url_path'] = data['url_path'].str.slice(0, 100)

        stem = Path(input_filepath).stem.replace("_cast", "")
        transformed_path = output_dir / f"{stem}_transform.parquet"
        data.to_parquet(transformed_path, index=False)

        logging.info(f"Transform successful. Written to: {transformed_path}")
        return str(transformed_path)

    except Exception as e:
        logging.error(f"Transform failed for {input_filepath}: {e}")
        raise


def _get_ga_path_level(df: pd.DataFrame, column_name: str) -> pd.DataFrame:

    df['ga_path_level_1'] = df[column_name].apply(lambda x: x[25:31]).astype("string")
    df['ga_path_level_2'] = df[column_name].apply(lambda x: x[30:34]).astype("string")
    df['ga_path_level_3'] = df[column_name].apply(lambda x: x[33:]).astype("string")

    return df


def _get_word_count(df, column_name):

    def extract_word_count(row):
        # Safely parse the string into a Python object
        try:
            row = ast.literal_eval(row)
        except (ValueError, SyntaxError):
            return None  # Return None if parsing fails

        # Filter for articles
        articles = [item for item in row if item.get("@type") == "Article"]
        if articles:
            # Safely retrieve the 'wordCount' if it exists; return None otherwise
            return articles[0].get('wordCount', None)
        return None  # Return None if no "Article" is found

    df['word_count'] = df[column_name].apply(extract_word_count).astype("Int64")
    return df


def _map_categories(df: pd.DataFrame, engine: Engine) -> pd.DataFrame:
    """
    Maps category IDs in 'post_category_ids' to their corresponding category names using a SQL lookup table.

    Parameters:
    df (pd.DataFrame): Input DataFrame that should have a column 'post_category_ids' containing lists of category IDs.
    engine: SQLAlchemy engine for connecting to the SQL Server.

    Returns:
    pd.DataFrame: A DataFrame with an additional 'post_categories' column that maps IDs to their category names.
    """

    # Fetch lookup data
    try:
        query = "SELECT category_id, category_name FROM DimCategory"
        lookup_df = pd.read_sql(query, engine)
    except Exception as e:
        raise ValueError(f"Failed to read lookup table: {e}")

    # Convert lookup table to dictionary
    lookup_dict = pd.Series(lookup_df.category_name.values, index=lookup_df.category_id).to_dict()

    # Verify column existence
    if 'post_category_ids' not in df.columns:
        raise KeyError("Input DataFrame must contain a 'post_category_ids' column.")

    df['post_category_ids'] = df['post_category_ids'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Map category IDs to category names
    df = df.copy()
    df['categories_desc'] = df['post_category_ids'].apply(
        lambda id_list: '; '.join([lookup_dict.get(i, 'Unknown') for i in id_list])
    )
    df['categories_desc'] = df['categories_desc'].astype("string")

    return df


def _map_tags(df: pd.DataFrame, engine: Engine) -> pd.DataFrame:
    """
    Maps category IDs in 'post_category_ids' to their corresponding category names using a SQL lookup table.

    Parameters:
    df (pd.DataFrame): Input DataFrame that should have a column 'post_category_ids' containing lists of category IDs.
    engine: SQLAlchemy engine for connecting to the SQL Server.

    Returns:
    pd.DataFrame: A DataFrame with an additional 'post_categories' column that maps IDs to their category names.
    """

    # Fetch lookup data
    try:
        query = "SELECT tag_id, tag_name FROM DimTag"
        lookup_df = pd.read_sql(query, engine)
    except Exception as e:
        raise ValueError(f"Failed to read lookup table: {e}")

    # Convert lookup table to dictionary
    lookup_dict = pd.Series(lookup_df.tag_name.values, index=lookup_df.tag_id).to_dict()

    # Verify column existence
    if 'post_tag_ids' not in df.columns:
        raise KeyError("Input DataFrame must contain a 'post_tag_ids' column.")

    df['post_tag_ids'] = df['post_tag_ids'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    # Map category IDs to category names
    df = df.copy()
    df['tags_desc'] = df['post_tag_ids'].apply(
        lambda id_list: '; '.join([lookup_dict.get(i, 'Unknown') for i in id_list])
    )
    df['tags_desc'] = df['tags_desc'].astype("string")

    return df
