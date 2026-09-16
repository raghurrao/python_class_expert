# Day 67: K-Means Clustering (Unsupervised Learning)

So far, all our models have been **Supervised**—we provided the answers ($y$) during training. But what if we have a massive dataset of customer behavior and no labels? How do we find patterns? Welcome to **Unsupervised Learning**.

---

## 1. What is Clustering?
Clustering algorithms group similar data points together based solely on their features ($X$). 

**K-Means** is the most popular clustering algorithm. 
1. You tell it how many clusters ($K$) you want.
2. It randomly places $K$ "centroids" (center points) in the data.
3. Every data point is assigned to its closest centroid.
4. The centroids move to the average position of all the points assigned to them.
5. Steps 3 and 4 repeat until the centroids stop moving.

---

## 2. Core Concepts & Operations

### Running K-Means
```python
from sklearn.cluster import KMeans
import numpy as np

# Sample Data (e.g., Customer Annual Income and Spending Score)
# We can clearly see two "groups" here
X = np.array([
    [15, 39], [15, 81], [16, 6], [16, 77], # Group 1
    [80, 20], [85, 25], [90, 10], [100, 15] # Group 2
])

# Initialize the model (We want to find 2 clusters)
# n_init='auto' is the modern scikit-learn standard for how many times it restarts
model = KMeans(n_clusters=2, random_state=42, n_init='auto')

# Fit the model (Notice there is no 'y' passed in!)
model.fit(X)

# See which cluster each point was assigned to
print("Cluster Labels:", model.labels_)

# See the coordinates of the center of each cluster
print("Cluster Centers:\n", model.cluster_centers_)

# Predict the cluster for a new customer
new_customer = np.array([[50, 50]])
print("New Customer Assigned to Cluster:", model.predict(new_customer))
```

### Choosing K
Since you don't have labels, how do you know if $K=2$ or $K=5$ is better? You can use the **Elbow Method**, plotting the "Inertia" (sum of squared distances from points to their centroid) for various values of $K$. You look for the "elbow" where adding more clusters doesn't significantly reduce the inertia.

---

## 3. Reference Documentation
* [Scikit-Learn KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
* [K-means clustering (Wikipedia)](https://en.wikipedia.org/wiki/K-means_clustering)
