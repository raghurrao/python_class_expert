# Day 22: Matplotlib

Data visualization is a critical skill for any data professional. Before building models, you must understand the data. Matplotlib is the foundation of data visualization in Python.

---

## 1. Why Matplotlib?
While Pandas has built-in plotting functions, they are just wrappers around Matplotlib. Knowing Matplotlib allows you to create fully custom visualizations, modify axes, add annotations, and build multi-plot dashboards.

---

## 2. Core Concepts & Operations

### The Object-Oriented Interface
Matplotlib has two interfaces: a MATLAB-style state-based interface (`plt.plot()`) and an object-oriented interface. We focus on the object-oriented interface because it gives you much more control.

* **Figure:** The overall window or page that everything is drawn on.
* **Axes:** The actual plot (the area with data, x/y labels, title). A Figure can contain multiple Axes.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 1. Create a Figure and an Axes
fig, ax = plt.subplots(figsize=(8, 4))

# 2. Plot data on the Axes
ax.plot(x, y, color='blue', linestyle='--', label='Sine Wave')

# 3. Customize the Axes
ax.set_title('My First Plot')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()
ax.grid(True)

# 4. Show the plot
plt.show()
```

### Common Plot Types
Different data requires different plot types.

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4)) # 1 row, 2 columns of plots

# --- Bar Chart (Categorical vs Numerical) ---
categories = ['A', 'B', 'C']
values = [10, 20, 15]
axes[0].bar(categories, values, color='skyblue')
axes[0].set_title('Bar Chart')

# --- Scatter Plot (Numerical vs Numerical) ---
x_scatter = np.random.rand(50)
y_scatter = x_scatter * 2 + np.random.randn(50) * 0.1
axes[1].scatter(x_scatter, y_scatter, color='red', alpha=0.5)
axes[1].set_title('Scatter Plot')

plt.tight_layout() # Adjusts spacing between plots
plt.show()
```

---

## 3. Reference Documentation
* [Matplotlib Pyplot tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
* [Matplotlib Object-Oriented API](https://matplotlib.org/stable/api/axes_api.html)
