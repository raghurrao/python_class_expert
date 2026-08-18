# Day 15: Table Joins & Merges

Today we learn relational joins.

## Core Concepts
* `pd.merge(df1, df2, on='key', how='inner'|'left'|'right'|'outer')`.
* `pd.concat([df1, df2], axis=0)`: Row-wise concatenation.
* `pd.concat([df1, df2], axis=1)`: Column-wise concatenation.
