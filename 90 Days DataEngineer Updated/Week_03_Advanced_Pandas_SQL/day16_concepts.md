# Day 16: Reshaping Data & Pivots

Data is often provided in a format that isn't ideal for the analysis you want to perform. Today we learn how to reshape data from "wide" to "long" format (and vice versa) using `melt` and `pivot_table`.

---

## 1. Wide vs. Long Data
* **Wide Data**: Each row represents a single entity, and each column represents a different attribute (or the same attribute at different times, like `Sales_Q1`, `Sales_Q2`). Great for reading, bad for some visualizations and groupby operations.
* **Long Data**: Each row represents one observation (e.g., one time period for one entity). Great for analysis and plotting.

---

## 2. Core Concepts & Operations

### Wide to Long (`pd.melt`)
`melt` "unpivots" a DataFrame from wide to long format, optionally leaving identifiers set.

```python
import pandas as pd

df_wide = pd.DataFrame({
    'Company': ['Apple', 'Google', 'Microsoft'],
    'Q1_Sales': [100, 80, 90],
    'Q2_Sales': [110, 85, 95]
})

# Melt the dataframe
df_long = pd.melt(
    df_wide,
    id_vars=['Company'],          # Columns to keep as identifiers (won't be melted)
    value_vars=['Q1_Sales', 'Q2_Sales'], # Columns to melt (if not specified, all non-id vars are used)
    var_name='Quarter',           # Name of the new 'variable' column
    value_name='Sales'            # Name of the new 'value' column
)

print(df_long)
#       Company   Quarter  Sales
# 0       Apple  Q1_Sales    100
# 1      Google  Q1_Sales     80
# 2   Microsoft  Q1_Sales     90
# 3       Apple  Q2_Sales    110
# 4      Google  Q2_Sales     85
# 5   Microsoft  Q2_Sales     95
```

### Long to Wide (`pivot_table`)
`pivot_table` creates a spreadsheet-style pivot table as a DataFrame. It takes long data and pivots it to wide format, optionally aggregating values.

```python
# Pivot back to wide format
df_pivoted = df_long.pivot_table(
    index='Company',   # Column to make the new index (rows)
    columns='Quarter', # Column to make the new columns
    values='Sales',    # Column to populate the values
    aggfunc='sum'      # How to aggregate if there are duplicates (default is 'mean')
)

# You can reset the index if you want 'Company' to be a regular column again
df_pivoted = df_pivoted.reset_index()
```

---

## 3. Reference Documentation
* [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html)
