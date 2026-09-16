# Day 10: Slicing, Filtering & Querying

Data analysis often requires drilling down into specific subsets of your data. Today we learn to query DataFrames using label-based indexing, position-based indexing, and conditional filtering.

---

## 1. Why Slicing & Filtering?
You rarely want to analyze your entire dataset at once. You might need to look only at "sales from Q3," "customers over 30," or simply extract the first 10 rows for a quick preview. Pandas provides powerful tools to slice and filter data efficiently.

---

## 2. Core Concepts & Operations

### Accessing by Label: `loc`
`loc` is used to access a group of rows and columns by their labels or a boolean array.

```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'SF']
}, index=['ID1', 'ID2', 'ID3'])

# Select a single row by index label
print(df.loc['ID2'])

# Select multiple rows and specific columns
print(df.loc[['ID1', 'ID3'], ['Name', 'City']])

# Slicing with labels (Note: both start and stop are INCLUDED)
print(df.loc['ID1':'ID2', 'Age':'City'])
```

### Accessing by Position: `iloc`
`iloc` is used to access a group of rows and columns by integer position (from 0 to length-1).

```python
# Select the first row (index 0)
print(df.iloc[0])

# Select first two rows and first two columns
print(df.iloc[:2, :2])

# Select specific rows and columns by their integer positions
print(df.iloc[[0, 2], [0, 2]])
```

### Boolean Filtering
You can filter a DataFrame by applying a condition to a column, which returns a boolean Series. Passing this Series back to the DataFrame filters out the `False` rows.

```python
# Simple condition
adults = df[df['Age'] >= 30]

# Multiple conditions
# Use & for AND, | for OR. Parentheses are REQUIRED around each condition.
target_group = df[(df['Age'] >= 30) & (df['City'] == 'SF')]
```

### Querying with `query()`
Pandas also provides a SQL-like string querying syntax which can be more readable for complex filtering.

```python
# Equivalent to the multiple condition above
target_group = df.query("Age >= 30 and City == 'SF'")
```

---

## 3. Reference Documentation
* [Indexing and selecting data](https://pandas.pydata.org/docs/user_guide/indexing.html)
