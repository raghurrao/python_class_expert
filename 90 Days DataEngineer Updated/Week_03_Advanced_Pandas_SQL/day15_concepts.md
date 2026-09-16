# Day 15: Table Joins & Merges

Data in the real world is rarely stored in a single giant table. Usually, it's normalized and spread across multiple tables to reduce redundancy. Today we learn how to combine datasets using relational joins and concatenations.

---

## 1. Concatenation vs. Merging
* **Concatenation (`pd.concat`)**: Gluing dataframes together, either stacking them vertically (adding more rows) or side-by-side (adding more columns).
* **Merging (`pd.merge`)**: Combining dataframes based on common columns (keys). This is equivalent to SQL JOIN operations.

---

## 2. Core Concepts & Operations

### Concatenating DataFrames
Use `pd.concat()` to append rows or columns.

```python
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

# Vertical Concatenation (axis=0 is default)
# Stacks df2 below df1
vertical = pd.concat([df1, df2], axis=0, ignore_index=True)

# Horizontal Concatenation (axis=1)
# Places df2 next to df1
horizontal = pd.concat([df1, df2], axis=1)
```

### Merging (Joining) DataFrames
`pd.merge()` is the workhorse for relational data. You must specify the dataframes, the key(s) to join on, and the type of join (`how`).

```python
customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

orders = pd.DataFrame({
    'order_id': [101, 102],
    'customer_id': [1, 2],
    'amount': [250, 400]
})

# Inner Join (Default)
# Only keeps rows with matching keys in BOTH dataframes
inner_join = pd.merge(customers, orders, on='customer_id', how='inner')

# Left Join
# Keeps ALL rows from the left dataframe (customers), fills missing right values with NaN
left_join = pd.merge(customers, orders, on='customer_id', how='left')

# Right Join
# Keeps ALL rows from the right dataframe (orders)
right_join = pd.merge(customers, orders, on='customer_id', how='right')

# Outer Join
# Keeps ALL rows from BOTH dataframes, filling missing values with NaN where there is no match
outer_join = pd.merge(customers, orders, on='customer_id', how='outer')
```

### Joining on Different Column Names
If the keys have different names in the two dataframes, use `left_on` and `right_on`:

```python
orders2 = pd.DataFrame({'cust_id': [1, 2], 'amount': [250, 400]})
joined = pd.merge(customers, orders2, left_on='customer_id', right_on='cust_id', how='inner')
```

---

## 3. Reference Documentation
* [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html)
