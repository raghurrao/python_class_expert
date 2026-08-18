import pandas as pd

def generate_eda_summary(df: pd.DataFrame) -> dict:
    """
    Compute a dictionary of EDA metrics:
    - 'row_count': number of rows
    - 'column_count': number of columns
    - 'null_count': total number of missing cells
    - 'correlation_matrix': Pearson correlation dataframe
    """
    return {
        "row_count": len(df),
        "column_count": len(df.columns),
        "null_count": int(df.isna().sum().sum()),
        "correlation_matrix": df.corr(numeric_only=True)
    }