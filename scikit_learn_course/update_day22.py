import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

def create_code_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

day22_cells = [
    create_markdown_cell("# PHASE 4 — UNSUPERVISED LEARNING"),
    create_markdown_cell("# Day 22 — Evaluation & DBSCAN"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Use the **Silhouette Score** to evaluate clusters mathematically.\n- Explain why K-Means fails on complex geometric shapes.\n- Understand the **DBSCAN** algorithm (Density-Based Spatial Clustering of Applications with Noise).\n- Use DBSCAN to automatically find anomalies/outliers."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 21 (K-Means Clustering)."),
    
    create_markdown_cell("## 3. Concept: The Silhouette Score\nYesterday we used the Elbow Method (Inertia) to find $K$. But Inertia only tells us how tightly packed the clusters are. \n\nThe **Silhouette Score** measures two things simultaneously:\n1. **Cohesion**: How close is a point to the other points in its OWN cluster?\n2. **Separation**: How far is a point from the points in the NEAREST OTHER cluster?\n\nThe score ranges from `-1` to `1`.\n- `1`: The point is perfectly assigned. It is far from other clusters.\n- `0`: The point is sitting directly on the border between two clusters.\n- `-1`: The point was assigned to the wrong cluster!"),
    
    create_markdown_cell("## 4. Concept: The Weakness of K-Means\nK-Means mathematically assumes that all clusters are perfect circles (or spheres in 3D). If your data is shaped like a crescent moon or a long thin line, K-Means will completely fail, arbitrarily chopping the shapes in half.\nFurthermore, K-Means *forces* every single data point into a cluster, even if the point is an extreme outlier (noise)."),
    
    create_markdown_cell("## 5. Concept: DBSCAN (Density-Based Clustering)\n**DBSCAN** fixes both of these problems. \nInstead of dropping Centroids, DBSCAN acts like an infectious virus:\n1. You define a radius (`eps`).\n2. It picks a random point. If there are enough neighboring points (`min_samples`) within its radius, they form a cluster.\n3. It then checks the neighbors of the neighbors, expanding the cluster organically in whatever shape the data takes.\n4. If a point is too far away from everything, DBSCAN doesn't force it into a cluster. It labels it as `-1` (Noise/Outlier)!"),
    
    create_markdown_cell("## 6. Scikit-learn API\n```python\nfrom sklearn.metrics import silhouette_score\nfrom sklearn.cluster import DBSCAN\n\n# Calculate score (closer to 1 is better)\nscore = silhouette_score(X, kmeans.labels_)\n\n# DBSCAN\nmodel = DBSCAN(eps=0.5, min_samples=5)\n```"),
    
    create_markdown_cell("## 7. Simple Example: K-Means Failure\nLet's generate the \"Moons\" dataset (which we used for KNN). Let's see what K-Means does to it."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_moons",
        "from sklearn.cluster import KMeans, DBSCAN",
        "from sklearn.metrics import silhouette_score",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "# 1. Generate Non-Linear Data (Moons)",
        "X, _ = make_moons(n_samples=300, noise=0.05, random_state=42)",
        "",
        "# 2. We MUST scale for DBSCAN and K-Means",
        "scaler = StandardScaler()",
        "X_scaled = scaler.fit_transform(X)",
        "",
        "# 3. Train K-Means (K=2)",
        "kmeans = KMeans(n_clusters=2, random_state=42)",
        "kmeans.fit(X_scaled)",
        "",
        "print('K-Means Silhouette Score:', silhouette_score(X_scaled, kmeans.labels_))"
    ]),
    
    create_markdown_cell("## 8. Code Walkthrough\n- We scaled the data so distances are calculated fairly.\n- K-Means found two clusters and yielded a Silhouette Score of ~0.49. That sounds decent, but let's visualize it."),
    
    create_markdown_cell("## 9. Experiment: Plotting the Failure\nLet's plot the K-Means labels, and then train DBSCAN and plot its labels side-by-side."),
    create_code_cell([
        "# Train DBSCAN",
        "dbscan = DBSCAN(eps=0.3, min_samples=5)",
        "dbscan.fit(X_scaled)",
        "",
        "fig, axes = plt.subplots(1, 2, figsize=(12, 5))",
        "",
        "# Plot K-Means",
        "axes[0].scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans.labels_, cmap='viridis')",
        "axes[0].set_title('K-Means (Failed to capture moons)')",
        "",
        "# Plot DBSCAN",
        "axes[1].scatter(X_scaled[:, 0], X_scaled[:, 1], c=dbscan.labels_, cmap='viridis')",
        "axes[1].set_title('DBSCAN (Perfectly captured moons)')",
        "",
        "plt.show()"
    ]),
    create_markdown_cell("> Look at the left plot! K-Means literally drew a straight line down the middle, chopping both moons in half. \n> Look at the right plot! DBSCAN's \"density virus\" perfectly crawled along the curve of each moon."),
    
    create_markdown_cell("## 10. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "X_outliers = np.vstack([X_scaled, [[5, 5], [-5, -5]]])",
        "",
        "db_outlier = DBSCAN(eps=0.3, min_samples=5)",
        "db_outlier.fit(X_outliers)",
        "",
        "labels = db_outlier.labels_"
    ]),
    create_markdown_cell("> **Question:** We added two extreme outlier points `[5, 5]` and `[-5, -5]`. \n> Since they have no neighbors within `eps=0.3`, what cluster label will DBSCAN assign them?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Outlier 1 Label:', labels[-2])",
        "print('Outlier 2 Label:', labels[-1])",
        "print('\\nDBSCAN assigns the label `-1` to any point it considers Noise/Outlier!')",
        "print('This makes DBSCAN incredibly useful for Anomaly Detection.')"
    ]),
    
    create_markdown_cell("## 11. Coding Exercise\nThe Silhouette Score requires at least 2 clusters to calculate. What happens if you run `silhouette_score(X, db_outlier.labels_)`?\nTry it. Write a `try-except` block to catch the error it throws."),
    create_code_cell([
        "# YOUR CODE HERE",
        "try:",
        "    silhouette_score(X_outliers, db_outlier.labels_)",
        "    print('Success!')",
        "except Exception as e:",
        "    print('Error caught:', e)",
        "    print('\\nWhy? Because DBSCAN might classify the entire dataset as a single cluster (0) and a bunch of noise (-1). The Silhouette Score mathematically requires at least two actual clusters to compute distance between them.')"
    ]),
    
    create_markdown_cell("## 12. Debugging Challenge\nA Junior Developer wants to use DBSCAN. They set `eps = 100.0`. Their data is standard scaled (meaning most values are between -2 and 2). What will happen?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: The model will put every single data point into one massive cluster (Label 0).')",
        "print('Why? If eps=100, the radius is so large that every point is considered a \"neighbor\" to every other point.')",
        "print('Conversely, if eps=0.0001, the radius is so tiny that nobody has neighbors, and EVERY point becomes an outlier (Label -1).')"
    ]),
    create_markdown_cell("> **Rule:** Tuning `eps` is the hardest part of DBSCAN. You usually have to try several values between `0.1` and `2.0` on scaled data."),
    
    create_markdown_cell("## 13. Model Evaluation (Pros and Cons)\n- **K-Means**: Fast, mathematically simple, forces everything into a cluster. Terrible for weird shapes or data with heavy outliers.\n- **DBSCAN**: Handles weird shapes beautifully, natively identifies outliers (Label `-1`). But it struggles if clusters have varying densities (e.g., one cluster is super tight, another is very loose) because `eps` is fixed globally."),
    
    create_markdown_cell("## 14. Real-World Example\n**Anomaly Detection in Manufacturing**: A factory sensors monitor the vibration and heat of a machine. 99.9% of the time, the machine operates normally, creating a massive dense blob of data. When the machine is about to break, the sensors output weird readings. You don't know what a \"broken\" reading looks like, so you can't use Supervised Classification.\nYou run DBSCAN. It lumps the 99.9% of data into Cluster `0`. The weird readings are assigned `-1`. The system instantly sends an alert to a mechanic to check the machine!"),
    
    create_markdown_cell("## 15. Mini Project\nLet's prove DBSCAN is great for Anomaly Detection. Generate a massive blob of data and manually inject 3 extreme outliers. Use DBSCAN to find and print the coordinates of the 3 outliers!"),
    create_code_cell([
        "from sklearn.datasets import make_blobs",
        "",
        "# 1. Dense blob + 3 extreme outliers",
        "X_blob, _ = make_blobs(n_samples=500, centers=1, cluster_std=0.5, random_state=42)",
        "outliers = np.array([[10, 10], [-10, -10], [10, -10]])",
        "X_anomaly = np.vstack([X_blob, outliers])",
        "",
        "# 2. Scale and run DBSCAN",
        "scaler = StandardScaler()",
        "X_anomaly_scaled = scaler.fit_transform(X_anomaly)",
        "",
        "db = DBSCAN(eps=0.5, min_samples=5)",
        "db.fit(X_anomaly_scaled)",
        "",
        "# 3. Extract the outliers (Label == -1)",
        "found_outliers = X_anomaly[db.labels_ == -1] # Notice we use the original X_anomaly to print real coordinates",
        "",
        "print('Coordinates of detected Anomalies/Outliers:')",
        "print(found_outliers)"
    ]),
    
    create_markdown_cell("## 16. Common Mistakes\n- **Not Scaling before DBSCAN**: Since `eps` is a physical distance radius, it is completely meaningless if your features are on different scales (e.g., Age vs Salary).\n- **Ignoring the `-1` labels**: Beginners often treat `-1` as just \"Cluster 3\". It is not a cluster. It is Noise.\n- **Using Silhouette on DBSCAN blindly**: If DBSCAN finds 1 cluster and noise, `silhouette_score` will crash."),
    
    create_markdown_cell("## 17. Interview Questions\n- **Beginner**: What does a Silhouette Score of 1 mean? (Answer: The point is perfectly assigned to its cluster and far away from others).\n- **Intermediate**: When would you use DBSCAN instead of K-Means? (Answer: When the clusters are not spherical, or when you want the algorithm to identify outliers automatically).\n- **Advanced**: Explain what the `eps` and `min_samples` parameters do in DBSCAN. (Answer: `eps` is the physical radius of the \"neighborhood\". `min_samples` is the minimum number of data points that must exist within that radius for it to be considered a valid cluster)."),
    
    create_markdown_cell("## 18. Knowledge Check\n- What is the range of the Silhouette Score? (-1 to 1)\n- What label does DBSCAN assign to noise? (-1)"),
    
    create_markdown_cell("## 19. Summary\n- **Silhouette Score** measures Cohesion (tightness) and Separation (distance between clusters).\n- **K-Means** fails on non-circular data and forces outliers into clusters.\n- **DBSCAN** groups data based on density, organically wrapping around weird shapes.\n- **DBSCAN** inherently performs Anomaly Detection by labeling isolated points as `-1`.\n- You MUST scale data for DBSCAN."),
    
    create_markdown_cell("## 20. Homework\nLoad the `load_wine` dataset. Remove the `y` target. Scale the data. Write a `for` loop that tests `eps` values from `[1.0, 1.5, 2.0, 2.5]` in DBSCAN. Print how many outliers (Label `-1`) the model finds for each `eps` setting!")
]

# Read existing notebook and update cells
filename = "Day_22_Choosing_Number_of_Clusters.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day22_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
