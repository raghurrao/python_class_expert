import numpy as np

def check_stationarity(time_series: np.ndarray) -> bool:
    """
    Run an Augmented Dickey-Fuller (ADF) test using statsmodels.
    Return True if the series is stationary (p-value < 0.05).
    """
    from statsmodels.tsa.stattools import adfuller
    result = adfuller(time_series)
    p_value = result[1]
    return p_value < 0.05