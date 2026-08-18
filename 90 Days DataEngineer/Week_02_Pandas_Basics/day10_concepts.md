# Day 10: Slicing, Filtering & Querying

Today we learn to query dataframes using conditional filters and pandas indexing.

## Core Concepts
* `loc[row_label, col_label]`: Access by label.
* `iloc[row_idx, col_idx]`: Access by integer position.
* **Boolean Filtering:** `df[df['col'] > val]`
* **Multi-Condition Filtering:** Use `&` (AND) and `|` (OR) with parentheses.
