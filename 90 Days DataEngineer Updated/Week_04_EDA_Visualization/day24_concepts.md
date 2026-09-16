# Day 24: Outlier Detection (IQR Method)

Outliers are data points that differ significantly from other observations. They can occur due to variability in measurement or indicate experimental errors. Finding and handling them is a crucial part of Exploratory Data Analysis (EDA).

---

## 1. Why Detect Outliers?
Outliers can drastically skew the results of your data analysis and machine learning models. For example, a single billionaire in a room of 10 average-income people will make the "average" income look like millions of dollars, which is misleading.

---

## 2. Core Concepts & Operations

### The Interquartile Range (IQR) Method
The IQR is a robust measure of statistical dispersion. It is the range between the first quartile (25th percentile) and the third quartile (75th percentile).

* **Q1 (First Quartile):** 25% of the data falls below this value.
* **Q3 (Third Quartile):** 75% of the data falls below this value.
* **IQR:** Q3 - Q1 (The middle 50% of the data).

A commonly used rule of thumb to identify outliers is:
* Lower Bound: `Q1 - 1.5 * IQR`
* Upper Bound: `Q3 + 1.5 * IQR`

Any data point outside these bounds is considered a potential outlier.

### Implementation in Pandas

```python
import pandas as pd
import numpy as np

# Sample data with an outlier (1000)
df = pd.DataFrame({'value': [10, 12, 11, 15, 14, 13, 1000, 12, 11]})

# 1. Calculate Q1 and Q3
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)

# 2. Calculate IQR
IQR = Q3 - Q1

# 3. Define the bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# 4. Find the outliers
outliers = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]
print(f"Outliers:\n{outliers}")

# 5. Handle the outliers
# Option A: Remove them
df_clean = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

# Option B: Clip (Winsorize) them to the bounds
df_clipped = df.copy()
df_clipped['value'] = np.clip(df_clipped['value'], lower_bound, upper_bound)
```

---

## 3. Reference Documentation
* [Pandas quantile method](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)
* [Numpy clip method](https://numpy.org/doc/stable/reference/generated/numpy.clip.html)
