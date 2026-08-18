import numpy as np
import pandas as pd

def detect_and_clip_outliers(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Calculate IQR of column, define bounds (Q1 - 1.5*IQR, Q3 + 1.5*IQR),
    and clip values exceeding bounds.
    """
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.clip(df[col], lower, upper)
    return df
