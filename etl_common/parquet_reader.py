import os
import logging
import pandas as pd
from pathlib import Path


class ParquetReader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.file_extension = self.file_path.suffix
        self.file_size = self.file_path.stat().st_size
        self.last_modified = self.file_path.stat().st_mtime
        self.created_time = os.path.getctime(self.file_path)

        if self.file_extension != ".parquet":
            raise ValueError(f"Unsupported file type: {self.file_extension}. Only .parquet files are allowed.")
        
    
    def pd_read_with_validation(self, dtype_map: dict) -> pd.DataFrame:
        """
        Reads a parquet file with safe error handling.
        Filters out columns not in dtype_map.
        
        Parameters:
        - dtype_map (dict): Column-to-dtype map for Pandas
        """
        logging.info(f"Reading parquet file: {self.file_path}")

        try:
            df = pd.read_parquet(self.file_path)
        except pd.errors.EmptyDataError:
            logging.warning(f"{self.file_path} is empty. Skipping.")
            return pd.DataFrame()
        except ValueError as e:
            logging.error(f"Schema validation failed for {self.file_path}: {e}")
            return pd.DataFrame()
        except Exception as e:
            logging.error(f"Unexpected error reading {self.file_path}: {e}")
            return pd.DataFrame()
        
        if df.empty:
            logging.warning(f"{self.file_path} contains no data rows.")
        
        # Identify and drop columns not in dtype_map
        expected_columns = set(dtype_map.keys())
        actual_columns = set(df.columns)
        extra_columns = actual_columns - expected_columns
        
        if extra_columns:
            logging.warning(
                f"Found {len(extra_columns)} unexpected column(s) in {self.file_path}"
                f"that are not in schema. Dropping: {extra_columns}"
            )
            df = df.drop(columns=extra_columns)

        # fail if missing cols
        
        return df