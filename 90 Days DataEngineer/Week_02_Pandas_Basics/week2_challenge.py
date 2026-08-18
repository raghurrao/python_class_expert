import pandas as pd

def clean_and_pipeline_transactions(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Pipeline to clean raw transactions:
    1. Drop duplicate 'transaction_id'.
    2. Fill NaN customer_id with -1.
    3. Fill NaN sales_amount with 0.0.
    4. Group by customer_id and return a summary dataframe with:
       - 'total_amount': sum of sales_amount
       - 'transaction_count': count of sales_amount
    """
    # TODO: Implement your solution here
    pass
