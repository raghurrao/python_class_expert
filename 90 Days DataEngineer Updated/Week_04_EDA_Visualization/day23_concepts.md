# Day 23: Seaborn Statistical Plots

Seaborn is built on top of Matplotlib and integrates closely with Pandas DataFrames. It provides a high-level interface for drawing attractive and informative statistical graphics.

---

## 1. Why Seaborn?
While Matplotlib gives you absolute control, it can take 20 lines of code to create a nice-looking statistical chart. Seaborn can often do the same in just 1 line. It automatically handles Pandas DataFrames, semantic mapping (coloring by categories), and statistical aggregation.

---

## 2. Core Concepts & Operations

### Distribution Plots
Used to examine the distribution of a single variable.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample data
df = pd.DataFrame({
    'age': np.random.normal(35, 10, 1000),
    'salary': np.random.normal(60000, 15000, 1000),
    'department': np.random.choice(['Sales', 'IT', 'HR'], 1000)
})

# Histogram with Kernel Density Estimate (KDE) line
sns.histplot(data=df, x='age', kde=True)
plt.title('Age Distribution')
plt.show()

# Boxplot (great for showing outliers and quartiles)
sns.boxplot(data=df, x='department', y='salary')
plt.title('Salary by Department')
plt.show()
```

### Relational Plots
Used to understand the relationship between two variables.

```python
# Scatter plot with semantic mapping (coloring by department)
sns.scatterplot(data=df, x='age', y='salary', hue='department', alpha=0.6)
plt.title('Age vs Salary')
plt.show()
```

### Matrix Plots
Used to visualize data where both the X and Y axes are categorical, or to visualize correlation matrices.

```python
# Heatmap of correlations
correlation_matrix = df[['age', 'salary']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap')
plt.show()
```

---

## 3. Reference Documentation
* [Seaborn API Reference](https://seaborn.pydata.org/api.html)
* [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)