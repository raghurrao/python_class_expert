# Day 68: Principal Component Analysis (PCA)

Real-world datasets often have hundreds or thousands of features (high dimensionality). This makes models slow, prone to overfitting, and impossible to visualize. We need a way to compress the data while keeping the important information.

---

## 1. What is PCA?
Principal Component Analysis (PCA) is an unsupervised dimensionality reduction technique. It transforms your original features into a brand new set of features called **Principal Components**.

* The 1st component captures the most variance (information) possible.
* The 2nd component captures the most remaining variance, and is completely uncorrelated (orthogonal) to the 1st.
* And so on.

By keeping only the first few components, you can reduce 100 features down to 2 or 3, making it easy to plot on a graph and much faster to train on, while retaining 90%+ of the original information!

---

## 2. Core Concepts & Operations

### Running PCA
*Crucial Note:* You **must** scale your data (e.g., `StandardScaler`) before running PCA, or features with larger numbers (like Salary vs Age) will dominate the components.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample Data (10 samples, 5 features)
X = np.random.rand(10, 5)

# 1. Scale the data (Mandatory for PCA!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Initialize PCA
# Let's reduce our 5 features down to just 2 components
pca = PCA(n_components=2)

# 3. Fit and Transform the data
X_projected = pca.fit_transform(X_scaled)

print("Original shape:", X_scaled.shape)
print("Projected shape:", X_projected.shape) # Now it's 10x2!

# 4. Check how much information we kept
# explained_variance_ratio_ tells us what percentage of the original variance each component holds
variance_kept = sum(pca.explained_variance_ratio_)
print(f"Variance retained by 2 components: {variance_kept:.2%}")
```

---

## 3. Reference Documentation
* [Scikit-Learn PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
* [Principal component analysis (Wikipedia)](https://en.wikipedia.org/wiki/Principal_component_analysis)
