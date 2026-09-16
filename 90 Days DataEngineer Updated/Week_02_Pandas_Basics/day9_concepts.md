# Day 9: Data Cleaning & Type Casting

Data cleaning is arguably the most common and time-consuming task in a data engineer or data scientist's workflow. Real-world data is rarely perfect. Today we learn how to handle missing values, duplicates, and incorrect data types.

---

## 1. Why Data Cleaning?
Before you can analyze data or feed it into machine learning models, it must be clean. Missing values can cause mathematical errors, duplicates can skew results, and wrong data types (like a date stored as a string) can prevent you from using powerful built-in functions.

---

## 2. Core Concepts & Operations

### Handling Missing Values
In Pandas, missing data is usually represented as `NaN` (Not a Number).

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 35, 25],
    'Salary': [50000, 60000, np.nan, 50000]
})

# Finding missing values
print(df.isna())  # Returns a boolean DataFrame of the same shape
print(df.isna().sum()) # Counts missing values in each column

# Dropping missing values
# dropna() removes any row with at least one NaN by default
df_clean = df.dropna()

# Filling missing values (Imputation)
# You can fill NaNs with a specific value, or a statistic like the mean
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)
df['Salary'] = df['Salary'].fillna(0)
```

### Handling Duplicates
Duplicate records often appear when joining tables or scraping data.

```python
# Finding duplicates
# duplicated() returns a boolean Series indicating whether each row is a duplicate
print(df.duplicated())

# Removing duplicates
df_unique = df.drop_duplicates()

# You can also drop duplicates based on specific columns
df_unique_names = df.drop_duplicates(subset=['Name'])
```

### Type Casting
Sometimes data is loaded with the wrong data type. For example, numbers might be loaded as strings if there are commas in them.

```python
df = pd.DataFrame({
    'ID': ['1', '2', '3'],
    'Price': ['10.5', '20.0', '15.7']
})

print(df.dtypes)
# ID       object (string)
# Price    object

# Convert ID to integer
df['ID'] = df['ID'].astype(int)

# Convert Price to float
df['Price'] = df['Price'].astype(float)
```

---

## 3. Reference Documentation
* [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
* [Pandas dtypes](https://pandas.pydata.org/docs/user_guide/basics.html#dtypes)
