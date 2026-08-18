import pandas as pd

def calculate_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the Pearson correlation matrix for the numeric columns of the dataframe.
    """
    return df.corr(method="pearson")