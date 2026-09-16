# Day 11: String & Datetime Processing

Today we learn string operations and parsing datetimes, which are vital for handling unstructured text data, time-series data, and log files.

---

## 1. Why Specialized Accessors?
Pandas columns (Series) have special "accessors" (`.str` for text, `.dt` for datetimes) that let you apply Python-like methods to an entire column at once, leveraging vectorization for speed.

---

## 2. Core Concepts & Operations

### String Processing (`.str`)
When working with object (string) columns, you can use the `.str` accessor to apply string methods across the entire Series.

```python
import pandas as pd

df = pd.DataFrame({
    'Product': ['Apple iPhone', 'Samsung Galaxy', 'google pixel'],
    'Price': ['$999', '$899', '$799']
})

# Convert to lowercase
df['Product'] = df['Product'].str.lower()

# Check if a string contains a substring (useful for filtering)
has_apple = df['Product'].str.contains('apple') # Returns boolean Series

# String replacement (e.g., removing '$' from price)
df['Price_Clean'] = df['Price'].str.replace('$', '')

# Splitting strings
# expand=True returns a DataFrame instead of a list of strings
split_names = df['Product'].str.split(' ', expand=True)
df['Brand'] = split_names[0]
df['Model'] = split_names[1]
```

### Datetime Processing (`.dt`)
Time-series data is ubiquitous. Pandas excels at datetime manipulation, but you first need to ensure your data is in a datetime format, not a string.

```python
df = pd.DataFrame({
    'Date_String': ['2023-01-15', '2023-02-20', '2023-03-25']
})

# Convert string to datetime
# pd.to_datetime is incredibly smart at inferring formats, but you can also specify the format string.
df['Date'] = pd.to_datetime(df['Date_String'])

# Now you can use the .dt accessor to extract components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Get the day of the week (0 = Monday, 6 = Sunday)
df['Weekday'] = df['Date'].dt.dayofweek

# Get the name of the day
df['Day_Name'] = df['Date'].dt.day_name()
```

---

## 3. Reference Documentation
* [Working with text data](https://pandas.pydata.org/docs/user_guide/text.html)
* [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html)
