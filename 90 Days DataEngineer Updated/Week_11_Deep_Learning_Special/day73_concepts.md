# Day 73: Time Series & Stationarity

Time series data is data collected sequentially over time (e.g., daily stock prices, monthly sales, hourly temperature). Traditional ML models assume data points are independent of each other. In time series, data points are highly dependent on their past values (autocorrelation).

---

## 1. What is Stationarity?
Many time series forecasting models (like ARIMA) require the data to be **stationary**. 
A time series is stationary if its statistical properties do not change over time. Specifically:
1. **Constant Mean:** It doesn't have an upward or downward trend.
2. **Constant Variance:** The spread of the data doesn't get wider or narrower over time.
3. **No Seasonality:** It doesn't have repeating patterns at fixed intervals (like sales always spiking in December).

If your data is not stationary, you usually have to transform it (e.g., by taking the "difference" between consecutive days) before feeding it to a model.

---

## 2. Core Concepts & Operations

### The Augmented Dickey-Fuller (ADF) Test
How do you know if your data is stationary? You can look at a plot, but to be scientifically rigorous, you use a statistical test like the ADF test.

* **Null Hypothesis ($H_0$):** The time series is NOT stationary (it has a unit root / trend).
* **Alternative Hypothesis ($H_1$):** The time series IS stationary.

```python
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# 1. Create a clearly non-stationary series (a simple upward trend)
# e.g., 0, 1, 2, 3, 4, ..., 99
non_stationary_data = np.arange(100) 

# Run ADF test
result = adfuller(non_stationary_data)
p_value = result[1]

print(f"Non-Stationary Data P-Value: {p_value:.4f}")
if p_value < 0.05:
    print("Reject Null: Data is stationary.")
else:
    print("Fail to Reject Null: Data is NOT stationary (has a trend).")

# 2. Make it stationary by taking the first difference
# 1-0=1, 2-1=1, 3-2=1... The differenced series is just an array of 1s!
differenced_data = np.diff(non_stationary_data)

# In real data, differencing removes the trend and leaves the random noise, 
# which is usually stationary.
result_diff = adfuller(differenced_data)
p_value_diff = result_diff[1]

print(f"\nDifferenced Data P-Value: {p_value_diff:.4f}")
# (Note: adfuller might throw a warning on a perfectly constant array, but in real noisy data, p-value will drop below 0.05 here).
```

---

## 3. Reference Documentation
* [Statsmodels adfuller](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html)
* [Stationary process (Wikipedia)](https://en.wikipedia.org/wiki/Stationary_process)
