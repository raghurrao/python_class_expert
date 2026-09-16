# Day 12: Data Aggregation & GroupBy

Aggregation allows summarizing columns into single values. GroupBy allows segmenting records by category and then aggregating them independently. This is the equivalent of a SQL `GROUP BY` clause.

---

## 1. Why Aggregate and GroupBy?
Raw data tells you individual transactions. Aggregations tell you "total revenue," "average age," or "maximum score." GroupBy takes this a step further by answering questions like "total revenue *by region*" or "average age *by department*."

---

## 2. Core Concepts & Operations

### Simple Aggregations
You can apply statistical methods directly to DataFrames or Series.

```python
import pandas as pd

df = pd.DataFrame({
    'Department': ['Sales', 'IT', 'Sales', 'IT', 'HR'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [60000, 80000, 70000, 90000, 65000],
    'Experience_Years': [3, 5, 4, 8, 2]
})

print(df['Salary'].mean())   # Average salary overall
print(df['Salary'].sum())    # Total salary overall
print(df['Salary'].max())    # Highest salary
```

### The `agg()` Method
The `agg()` method allows you to apply multiple aggregation functions at once, or different functions to different columns.

```python
# Apply multiple functions to a single column
print(df['Salary'].agg(['mean', 'min', 'max']))

# Apply different functions to different columns
print(df.agg({
    'Salary': ['min', 'max'],
    'Experience_Years': 'mean'
}))
```

### GroupBy
The `groupby()` method splits the data into groups based on some criteria, applies a function to each group independently, and combines the results back together (the Split-Apply-Combine strategy).

```python
# 1. Split by Department
grouped = df.groupby('Department')

# 2. Apply mean() to the Salary column of each group
avg_salary_by_dept = grouped['Salary'].mean()
print(avg_salary_by_dept)
# Output:
# Department
# HR       65000.0
# IT       85000.0
# Sales    65000.0
# Name: Salary, dtype: float64

# You can do this in one line
print(df.groupby('Department')['Salary'].mean())
```

### GroupBy with Multiple Aggregations
You can chain `groupby` with `agg` to get very detailed summaries.

```python
summary = df.groupby('Department').agg({
    'Salary': ['mean', 'sum'],
    'Experience_Years': 'max',
    'Employee': 'count' # Count the number of employees per department
})
print(summary)
```

---

## 3. Reference Documentation
* [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html)
* [Pandas essential basic functionality (Aggregations)](https://pandas.pydata.org/docs/user_guide/basics.html#descriptive-statistics)
