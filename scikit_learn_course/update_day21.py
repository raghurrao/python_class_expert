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

day21_cells = [
    create_markdown_cell("# PHASE 4 — UNSUPERVISED LEARNING"),
    create_markdown_cell("# Day 21 — K-Means Clustering"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain the difference between Supervised and Unsupervised learning.\n- Understand how K-Means finds hidden groups without any labels.\n- Explain Centroids and Inertia.\n- Use the **Elbow Method** to figure out how many clusters exist in unknown data."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 17 (K-Nearest Neighbors / Distance Math).\n- Day 4 (StandardScaler)."),
    
    create_markdown_cell("## 3. Concept: Unsupervised Learning\nUp until today, every dataset had a target `y` (Price, Fraud, Spam). We trained models to predict `y` from `X`. This is called **Supervised Learning**.\n\nWhat if there is no `y`? What if I just hand you 10,000 customer records (Age, Salary, Spending Score) and say: *\"Find some interesting patterns in here.\"*\nThis is **Unsupervised Learning**. You are exploring the data blindly to discover hidden structures."),
    
    create_markdown_cell("## 4. Concept: K-Means Clustering\n**Clustering** is the task of grouping similar data points together. The most famous algorithm is **K-Means**.\n\nHow it works:\n1. You tell the algorithm how many clusters you want (e.g., $K=3$).\n2. It drops 3 random pins (called **Centroids**) onto the dataset.\n3. Every data point looks to see which Centroid it is closest to and joins that Centroid's team.\n4. The Centroid then moves to the exact mathematical center of all the points on its team.\n5. Repeat steps 3 and 4 until the Centroids stop moving. \n\n*Because K-Means uses physical distance to determine which team a point belongs to, you MUST scale your data!*"),
    
    create_markdown_cell("## 5. Scikit-learn API\n```python\nfrom sklearn.cluster import KMeans\nmodel = KMeans(n_clusters=3)\nmodel.fit(X) # Notice there is no 'y' !!\n```"),
    
    create_markdown_cell("## 6. Simple Example\nLet's generate a dataset that clearly has 4 blobs of data, but we won't tell the algorithm that. We will ask it to find 4 clusters."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_blobs",
        "from sklearn.cluster import KMeans",
        "",
        "# 1. Generate Data (We throw away the 'y' labels!)",
        "X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)",
        "",
        "# 2. Train K-Means (Notice we ONLY pass X)",
        "kmeans = KMeans(n_clusters=4, random_state=42)",
        "kmeans.fit(X)",
        "",
        "# 3. Get the Labels (The team assignments)",
        "team_labels = kmeans.labels_",
        "",
        "# 4. Get the Centroid coordinates",
        "centroids = kmeans.cluster_centers_",
        "",
        "print('First 10 team assignments:', team_labels[:10])"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We called `kmeans.fit(X)`. No `y` was provided.\n- The algorithm assigned every row an integer (0, 1, 2, or 3) indicating which cluster it belongs to. These are accessed via `.labels_`.\n- It also stored the final resting place of the 4 pins inside `.cluster_centers_`."),
    
    create_markdown_cell("## 8. Experiment\nLet's plot the data and color it based on the teams K-Means discovered. We'll also draw red X's where the final Centroids landed."),
    create_code_cell([
        "plt.figure(figsize=(8, 5))",
        "",
        "# Plot the data points, colored by their K-Means label",
        "plt.scatter(X[:, 0], X[:, 1], c=team_labels, cmap='viridis', s=50, alpha=0.6)",
        "",
        "# Plot the Centroids",
        "plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')",
        "",
        "plt.title('K-Means Clustering (K=4)')",
        "plt.legend()",
        "plt.show()"
    ]),
    create_markdown_cell("> It perfectly identified the 4 distinct blobs and placed a Centroid exactly in the middle of each one!"),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "kmeans_k2 = KMeans(n_clusters=2, random_state=42)",
        "kmeans_k2.fit(X)"
    ]),
    create_markdown_cell("> **Question:** We know there are 4 distinct blobs. What happens if we force K-Means to find only 2 clusters?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "plt.figure(figsize=(5, 3))",
        "plt.scatter(X[:, 0], X[:, 1], c=kmeans_k2.labels_, cmap='viridis', alpha=0.6)",
        "plt.scatter(kmeans_k2.cluster_centers_[:, 0], kmeans_k2.cluster_centers_[:, 1], c='red', s=200, marker='X')",
        "plt.title('Forced to find K=2')",
        "plt.show()",
        "print('It grouped the two left blobs into one massive cluster, and the two right blobs into another.')",
        "print('K-Means will ALWAYS find exactly the number of clusters you ask it to, even if that number is wrong.')"
    ]),
    
    create_markdown_cell("## 10. The Elbow Method (Finding the true K)\nIn the real world, you don't know how many clusters exist. How do you find the right $K$?\n\nWe look at **Inertia** (`kmeans.inertia_`). Inertia measures how tightly packed the clusters are. \nIf Inertia is 0, every data point is sitting directly on top of a Centroid. \nAs $K$ increases, Inertia always decreases. But we don't want $K=300$. \n\nWe train the model for $K=1, 2, 3... 10$ and plot the Inertia. The graph will look like an arm. The \"Elbow\" of the arm represents the optimal $K$ — the point where adding more clusters stops providing massive improvements."),
    
    create_markdown_cell("## 11. Coding Exercise\nWrite a `for` loop that trains a KMeans model for every $K$ from 1 to 10. Append the `.inertia_` of each model to a list. Finally, plot the list. Where is the elbow?"),
    create_code_cell([
        "# YOUR CODE HERE",
        "inertias = []",
        "K_range = range(1, 11)",
        "",
        "for k in K_range:",
        "    km = KMeans(n_clusters=k, random_state=42)",
        "    km.fit(X)",
        "    inertias.append(km.inertia_)",
        "",
        "plt.figure(figsize=(8, 4))",
        "plt.plot(K_range, inertias, marker='o', linestyle='--')",
        "plt.xlabel('Number of Clusters (K)')",
        "plt.ylabel('Inertia (Tightness)')",
        "plt.title('The Elbow Method')",
        "plt.xticks(K_range)",
        "plt.grid(True)",
        "plt.show()",
        "",
        "print('Notice how the massive drops stop at K=4. That is the elbow! This mathematically proves there are 4 clusters.')"
    ]),
    
    create_markdown_cell("## 12. Debugging Challenge\nA data analyst is trying to group customers based on Age (18-90) and Salary ($20,000 - $200,000). The model is completely ignoring the Age variable and only grouping people based on Salary. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: The model is ignoring Age entirely.')",
        "print('Why? K-Means uses physical Euclidean distance.')",
        "print('A difference of 50 years in Age is mathematically crushed by a difference of $50,000 in Salary.')"
    ]),
    create_markdown_cell("> **Rule:** You MUST use `StandardScaler` or `MinMaxScaler` before running K-Means so that all features contribute equally to the distance calculation."),
    
    create_markdown_cell("## 13. Model Evaluation\nEvaluating unsupervised models is notoriously difficult because there is no \"ground truth\" to compare against. \n- **Inertia**: Lower is better, but it's heavily influenced by the number of clusters.\n- **Silhouette Score**: We will learn this advanced metric tomorrow."),
    
    create_markdown_cell("## 14. Real-World Example\n**Customer Segmentation**: A marketing team has a database of 1 million users. They don't know anything about them. They run K-Means (K=5) on their purchasing habits. \nThe algorithm blindly creates 5 clusters. The analysts look at the clusters and realize:\n- Cluster 0: \"Bargain Hunters\" (only buy on sale)\n- Cluster 1: \"Whales\" (spend massive amounts)\n- Cluster 2: \"Window Shoppers\" (browse a lot, buy nothing)\nThe marketing team then creates 3 totally different email campaigns tailored specifically to those exact personas!"),
    
    create_markdown_cell("## 15. Mini Project\nBuild a Pipeline with `StandardScaler` and `KMeans(n_clusters=3)`. Generate a random dataset with 3 features and heavily distorted scales. Fit the pipeline and print the cluster centers (Centroids) for the scaled data."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "X_distorted = np.random.rand(150, 3)",
        "X_distorted[:, 0] *= 10000 # Feature 0 is massive",
        "",
        "kmeans_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('kmeans', KMeans(n_clusters=3, random_state=42))",
        "])",
        "",
        "kmeans_pipe.fit(X_distorted)",
        "",
        "# To get the centers, you have to extract the trained kmeans model from the pipeline",
        "trained_kmeans = kmeans_pipe.named_steps['kmeans']",
        "print('Scaled Centroid Coordinates:\\n', trained_kmeans.cluster_centers_)"
    ]),
    
    create_markdown_cell("## 16. Common Mistakes\n- **Not Scaling Data**: The #1 mistake. K-Means will fail spectacularly on unscaled data.\n- **Choosing K arbitrarily**: Always use the Elbow Method to justify your choice of K.\n- **Interpreting Clusters**: K-Means doesn't know *what* it found. It just groups numbers. It is up to human intuition to look at the groups and give them meaning (e.g., \"Ah, these are the Bargain Hunters\")."),
    
    create_markdown_cell("## 17. Interview Questions\n- **Beginner**: What is the difference between Supervised and Unsupervised Learning? (Answer: Supervised has labels/targets, Unsupervised explores raw data without labels).\n- **Intermediate**: Explain the Elbow Method. (Answer: Plot Inertia for various Ks. Find the \"elbow\" where adding more clusters yields diminishing returns in tightness).\n- **Advanced**: Why does K-Means scale poorly to massive datasets? (Answer: Because in every single iteration, it has to calculate the physical distance between *every* point and *every* centroid. For millions of rows, this becomes extremely slow)."),
    
    create_markdown_cell("## 18. Knowledge Check\n- What property stores the assignments of every data point? (`.labels_`)\n- What metric measures how tightly packed the clusters are? (Inertia)"),
    
    create_markdown_cell("## 19. Summary\n- **Unsupervised Learning** finds hidden structures without labels.\n- **K-Means** finds clusters by moving Centroids to the middle of data groupings.\n- **Inertia** measures tightness.\n- **The Elbow Method** is the standard way to find the optimal $K$.\n- **Scaling** is absolutely mandatory."),
    
    create_markdown_cell("## 20. Homework\nLoad the `load_iris` dataset, but throw away the `target` array entirely! Build a pipeline with `StandardScaler` and `KMeans`. Run the Elbow method on the iris data. Does the elbow appear at $K=3$? (Spoiler: It should, since there are 3 species of Iris flowers!).")
]

# Read existing notebook and update cells
filename = "Day_21_Clustering.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day21_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
