# Day 86: Feature Engineering Pipeline

We build the preprocessing pipelines. Numerical inputs are scaled, categorical variables are one-hot encoded.

## Pipeline Architecture:
* Numerical pipeline: Standard scaling.
* Categorical pipeline: One-hot encoding.
* Combine them using `ColumnTransformer`.