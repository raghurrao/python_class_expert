import pandas as pd
import sqlite3

def run_analytics_pipeline(customers_csv: str, db_path: str) -> pd.DataFrame:
    """
    1. Load customer CSV (containing customer_id, name).
    2. Read transaction details from SQLite table 'transactions' (customer_id, spend).
    3. Merge the datasets.
    4. Group by name and return total spend per customer.
    """
    # TODO: Implement your solution here
    pass
