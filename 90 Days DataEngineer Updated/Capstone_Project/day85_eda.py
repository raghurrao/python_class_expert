import pandas as pd

def run_capstone_eda(filepath: str):
    """
    1. Load the customer_churn.csv dataset.
    2. Calculate and return:
       - row_count (int)
       - mean_monthly_charges (float)
       - churn_rate (float, mean of churn column)
    """
    df = pd.read_csv(filepath)
    row_count = len(df)
    mean_monthly = float(df["monthly_charges"].mean())
    churn_rate = float(df["churn"].mean())
    return row_count, mean_monthly, churn_rate