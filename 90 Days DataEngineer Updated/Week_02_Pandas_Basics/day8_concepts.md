# Day 8: Pandas Series & DataFrames

Today we transition to **Pandas**, the gold standard library for tabular data manipulation in Python. It is built on top of NumPy and provides flexible data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) data fast, easy, and expressive.

---

## 1. Why Pandas?
While NumPy is excellent for homogeneous numerical arrays, it lacks row/column labels and robust handling of missing data. Pandas introduces two primary data structures:
* **Series:** A 1-dimensional labeled array.
* **DataFrame:** A 2-dimensional labeled data structure with columns of potentially different types (similar to a spreadsheet or SQL table).

---

## 2. Core Concepts & Operations

### Creating a Series
A `Series` is like a column in a table. It holds data of any type, and each element has a label (index).

```python
import pandas as pd

# Creating from a list
data = [10, 20, 30]
s = pd.Series(data, index=['a', 'b', 'c'])
print(s)
# Output:
# a    10
# b    20
# c    30
# dtype: int64
```

### Creating a DataFrame
A `DataFrame` is a 2D structure, like a dictionary of Series objects. You can create it from a dictionary of lists.

```python
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)
# Output:
#       Name  Age      City
# 0    Alice   25  New York
# 1      Bob   30    London
# 2  Charlie   35     Paris
```

### Reading Files
Pandas makes it incredibly easy to load data from various file formats directly into a DataFrame.

```python
# Reading from CSV
# df = pd.read_csv('path/to/file.csv')

# Reading from Excel
# df = pd.read_excel('path/to/file.xlsx')

# Reading from JSON
# df = pd.read_json('path/to/file.json')
```

### Basic DataFrame Inspection
Once data is loaded, you can quickly inspect it using these methods:

```python
df.head()    # View the first 5 rows
df.tail(3)   # View the last 3 rows
df.info()    # Summary of columns, non-null counts, and data types
df.describe()# Statistical summary of numerical columns
df.shape     # Tuple representing (rows, columns)
```

---

## 3. Reference Documentation
* [Pandas 10 minutes Quickstart](https://pandas.pydata.org/docs/user_guide/10min.html)
* [Pandas API Reference - IO Tools](https://pandas.pydata.org/pandas-docs/stable/reference/io.html)
