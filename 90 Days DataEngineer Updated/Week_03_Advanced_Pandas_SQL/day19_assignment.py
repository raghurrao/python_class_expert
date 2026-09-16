import sqlite3
import pandas as pd

def query_rolling_sales(db_path: str) -> pd.DataFrame:
    """
    Given SQLite db containing table 'sales' with: 'day' (INTEGER), 'revenue' (REAL).
    Write a window function SQL query to return:
    - 'day'
    - 'revenue'
    - 'cumulative_revenue' (the sum of revenue from day 1 up to current day).
    
    (Hint: Use: SUM(revenue) OVER (ORDER BY day) as cumulative_revenue)
    """
    # TODO: Implement your solution here
    pass
