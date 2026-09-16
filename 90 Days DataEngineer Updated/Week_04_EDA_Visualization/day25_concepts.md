# Day 25: Correlation Analysis

When doing Exploratory Data Analysis, you often want to know if two variables move together. Today we cover checking linear relationships between variables using correlation coefficients.

---

## 1. What is Correlation?
Correlation measures the strength and direction of a linear relationship between two continuous variables.
* **1.0**: Perfect positive correlation (as X goes up, Y goes up proportionally).
* **-1.0**: Perfect negative correlation (as X goes up, Y goes down proportionally).
* **0.0**: No linear correlation (the variables do not move together).

*Important:* Correlation does NOT imply causation! Just because ice cream sales and shark attacks both increase in summer (strong positive correlation) doesn't mean eating ice cream causes shark attacks.

---

## 2. Core Concepts & Operations

### Pearson Correlation Coefficient
This is the standard correlation coefficient, measuring the linear relationship between two variables. It assumes the data is normally distributed.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'study_hours': [2, 4, 6, 8, 10],
    'exam_score': [60, 70, 80, 85, 95],
    'video_games_hours': [10, 8, 6, 4, 2]
})

# Calculate correlation for a single pair
corr_pair = df['study_hours'].corr(df['exam_score'])
print(f"Correlation between study and score: {corr_pair}")

# Calculate the correlation matrix for all numeric columns
corr_matrix = df.corr() # Default is method='pearson'
print(corr_matrix)
```

### Visualizing Correlation
The best way to interpret a correlation matrix with many variables is to use a Seaborn heatmap.

```python
# Create a heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix, 
    annot=True,      # Show the correlation numbers
    cmap='coolwarm', # Use a diverging color map (red for positive, blue for negative)
    vmin=-1,         # Minimum correlation value
    vmax=1           # Maximum correlation value
)
plt.title('Correlation Matrix Heatmap')
plt.show()
```

### Other Correlation Methods
If your data isn't normally distributed or has extreme outliers, rank-based methods might be better.

```python
# Spearman Rank Correlation (evaluates monotonic relationships based on rank)
spearman_corr = df.corr(method='spearman')
```

---

## 3. Reference Documentation
* [Pandas DataFrame.corr](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html)