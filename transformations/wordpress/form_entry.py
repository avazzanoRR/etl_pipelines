import logging
from pathlib import Path
from typing import Any
import pandas as pd
from user_agents import parse
from rr_data_tools.transformations import convert_tz_string_to_datetime


def transform(input_filepath: str, output_dir: str) -> str:
    """Transforms a parquet file. Outputs to output_dir."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting transform for: {input_filepath}")
    try:
        data = pd.read_parquet(input_filepath)

        # Fill missing values in 'utm_...' with values from 'utm_..._1st'
        fallback_map = {'utm_source': 'utm_source_1st', 'utm_medium': 'utm_medium_1st', 'utm_campaign': 'utm_campaign_1st', 'utm_content': 'utm_content_1st', 'utm_term': 'utm_term_1st'}
        for col, fallback in fallback_map.items():
            logging.info(f"Filling missing '{col}' values with '{fallback}'.")
            data[col] = _fill_missing_from_another(data[col], data[fallback], missing_value='False')

        # Lowercase 'email_address'
        logging.info("Lowercasing 'email_address'.")
        data['email_address'] = data['email_address'].str.lower()

        # Titlecase 'first_name' and 'last_name'
        logging.info("Titlecasing 'first_name' and 'last_name'.")
        data['first_name'] = data['first_name'].str.title()
        data['last_name'] = data['last_name'].str.title()

        # Convert 'form_entry_datetime' to datetime localized to America/Chicago
        logging.info("Converting 'form_entry_datetime' to datetime localized to America/Chicago.")
        data = convert_tz_string_to_datetime(data, column='form_entry_datetime', timezone='America/Chicago')

        # Parse user agent strings
        logging.info("Parsing user agent strings in 'entry_user_agent'.")
        data = _parse_user_agent(data, column='entry_user_agent')

        # Truncate entry_user_agent to 100 characters
        logging.info("Truncating 'entry_user_agent' to 100 characters.")
        data['entry_user_agent'] = data['entry_user_agent'].str.slice(0, 100)

        # Replace NaN values with None
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


def _fill_missing_from_another(col, fallback, missing_value: Any=None) -> pd.Series:
    """
    Return a Series where values in 'col' that are missing (or equal to 'missing_value')
    are replaced by the corresponding values in 'fallback'.

    Parameters:
    - col: pd.Series to fill
    - fallback: pd.Series of same index to pull replacements from
    - missing_value: if None, treats pd.NA/np.nan as missing; otherwise treats that exact value as missing

    Returns:
    - pd.Series: The col with updated values
    """
    if missing_value is None:
        # fillna covers NaN/NA
        result = col.fillna(fallback)
    else:
        # only overwrite entries exactly equal to missing_value
        result = col.copy()
        mask = result == missing_value
        result.loc[mask] = fallback.loc[mask]
    return result.astype(col.dtype)


def _parse_user_agent(df, column):
    def _parse_user_agent_inner(ua_string):
        # Check if the value is NaN
        if pd.isna(ua_string):
            # Return NaN for all fields if the input is NaN
            return pd.Series({
                'browser_family': pd.NA,
                'browser_version': pd.NA,
                'os_family': pd.NA,
                'os_version': pd.NA,
                'device_family': pd.NA,
                'device_type': pd.NA,
                'is_touch_capable': pd.NA,
                'is_bot': pd.NA
            })

        # Parse the user-agent string
        ua = parse(ua_string)

        # Determine device type
        if ua.is_mobile:
            device_type = "mobile"
        elif ua.is_tablet:
            device_type = "tablet"
        else:
            device_type = "pc"

        # Return parsed details
        return pd.Series({
            'browser_family': ua.browser.family,
            'browser_version': ua.browser.version_string,
            'os_family': ua.os.family,
            'os_version': ua.os.version_string,
            'device_family': ua.device.family,
            'device_type': device_type,
            'is_touch_capable': int(ua.is_touch_capable),
            'is_bot': int(ua.is_bot)
        })

    parsed = df[column].apply(_parse_user_agent_inner)
    for col in parsed.columns:
        if col in ('is_touch_capable', 'is_bot'):
            parsed[col] = parsed[col].astype('Int64')
        else:
            parsed[col] = parsed[col].astype('string')

    return df.join(parsed)
