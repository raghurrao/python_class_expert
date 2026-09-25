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

day23_cells = [
    create_markdown_cell("# PHASE 4 — UNSUPERVISED LEARNING"),
    create_markdown_cell("# Day 23 — Hierarchical Clustering"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain the concept of Agglomerative (Bottom-Up) Clustering.\n- Build and interpret a **Dendrogram** to visualize the grouping of data.\n- Understand how to \"cut\" the dendrogram tree to get your final clusters.\n- Contrast Hierarchical Clustering with K-Means and DBSCAN."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 21 & 22 (K-Means, DBSCAN, Silhouette Score)."),
    
    create_markdown_cell("## 3. Concept: Hierarchical Clustering\nYesterday we looked at DBSCAN (density). The day before, K-Means (Centroids). \nWhat if we don't want to guess the number of clusters upfront, and we want to see a visual map of how every single point relates to every other point?\n\n**Agglomerative (Hierarchical) Clustering** works \"bottom-up\":\n1. It starts by assuming every single data point is its own tiny cluster (If you have 100 points, you have 100 clusters).\n2. It finds the 2 closest clusters and merges them together (Now you have 99 clusters).\n3. It repeats this process over and over, merging the closest clusters until there is only 1 massive cluster left that contains everything.\n\nIt records every single merge along the way!"),
    
    create_markdown_cell("## 4. Concept: The Dendrogram\nBecause it records every merge, we can plot the entire history as a massive family tree called a **Dendrogram**. \nThe height of the branches on the tree represents the physical distance between the clusters that were merged. \n\nBy looking at the tree, you can visually spot where the major splits occur, and simply draw a horizontal line across the tree to \"cut\" it into whatever number of clusters makes visual sense!"),
    
    create_markdown_cell("## 5. Scikit-learn API\n```python\nfrom sklearn.cluster import AgglomerativeClustering\nmodel = AgglomerativeClustering(n_clusters=3, linkage='ward')\n```\n*Note: Scikit-learn doesn't draw Dendrograms. We use the `scipy` library to draw the tree.*"),
    
    create_markdown_cell("## 6. Simple Example: The Dendrogram\nLet's generate some blob data, scale it, and then use `scipy` to draw the entire hierarchical tree before we even build our Scikit-learn model."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_blobs",
        "from sklearn.preprocessing import StandardScaler",
        "from scipy.cluster.hierarchy import dendrogram, linkage",
        "",
        "# 1. Generate 3 distinct blobs of data",
        "X, y = make_blobs(n_samples=50, centers=3, cluster_std=0.8, random_state=42)",
        "",
        "# 2. Scale the data (Mandatory for distance-based clustering!)",
        "scaler = StandardScaler()",
        "X_scaled = scaler.fit_transform(X)",
        "",
        "# 3. Calculate the linkage (the merging history)",
        "# 'ward' minimizes the variance of the clusters being merged",
        "Z = linkage(X_scaled, method='ward')",
        "",
        "# 4. Plot the Dendrogram",
        "plt.figure(figsize=(10, 5))",
        "plt.title('Hierarchical Clustering Dendrogram')",
        "plt.xlabel('Data Point Index (or cluster size)')",
        "plt.ylabel('Distance (Height)')",
        "dendrogram(Z)",
        "plt.axhline(y=5, color='r', linestyle='--', label='Cut Line (3 Clusters)')",
        "plt.legend()",
        "plt.show()"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We only used 50 samples so the tree is readable.\n- `linkage(X_scaled, 'ward')` did all the math to merge the points step-by-step.\n- `dendrogram(Z)` drew the tree.\n- Notice how the tree naturally splits into exactly 3 major branches (colored orange and green). The vertical lines are very tall, meaning there is a large distance between these 3 major groups. This perfectly matches the `centers=3` we asked for!"),
    
    create_markdown_cell("## 8. Experiment: Training the Model\nNow that we visually see 3 is the correct number of clusters, let's use Scikit-learn to actually assign the labels to the data."),
    create_code_cell([
        "from sklearn.cluster import AgglomerativeClustering",
        "",
        "# 1. Train the Model",
        "agg = AgglomerativeClustering(n_clusters=3, linkage='ward')",
        "labels = agg.fit_predict(X_scaled)",
        "",
        "# 2. Plot the resulting clusters",
        "plt.figure(figsize=(6, 4))",
        "plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis', s=50)",
        "plt.title('Agglomerative Clustering (K=3)')",
        "plt.show()"
    ]),
    create_markdown_cell("> It perfectly identified the 3 groups. Unlike K-Means, it didn't need to randomly drop Centroids and move them around. It just followed the tree structure down from the top!"),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "agg_2 = AgglomerativeClustering(n_clusters=2, linkage='ward')",
        "labels_2 = agg_2.fit_predict(X_scaled)"
    ]),
    create_markdown_cell("> **Question:** Look back at the Dendrogram in Section 6. If we tell the model to find `n_clusters=2`, what will the tree do?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('If n_clusters=2, the algorithm simply moves the horizontal cut line higher up the tree.')",
        "print('It will merge the two closest major branches (likely the two on the right side of the dendrogram) into a single massive cluster, leaving the left branch as the second cluster.')"
    ]),
    
    create_markdown_cell("## 10. Coding Exercise\nProve the concept above. Plot the scatter plot of `X_scaled`, colored by `labels_2`. You will see two of the blobs merged into one."),
    create_code_cell([
        "# YOUR CODE HERE",
        "plt.figure(figsize=(6, 4))",
        "plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels_2, cmap='viridis', s=50)",
        "plt.title('Agglomerative Clustering (K=2)')",
        "plt.show()",
        "print('As predicted, the horizontal cut line moved up, merging two distinct blobs into a single cluster.')"
    ]),
    
    create_markdown_cell("## 11. Debugging Challenge\nA scientist is trying to use Agglomerative Clustering on an astronomical dataset of 5,000,000 stars to find constellations. The code crashes with an `Out of Memory (OOM)` error. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: Agglomerative Clustering requires a massive distance matrix.')",
        "print('To merge the closest clusters, it has to know the exact distance between EVERY single point and EVERY other point.')",
        "print('For 5,000,000 stars, the distance matrix requires (5M * 5M) / 2 calculations. That takes terabytes of RAM!')"
    ]),
    create_markdown_cell("> **Rule:** Hierarchical Clustering is brilliant for visualization, but it scales terribly. Do not use it on datasets larger than a few thousand rows. Stick to K-Means for massive datasets."),
    
    create_markdown_cell("## 12. Clustering Algorithm Comparison\nYou now know three clustering algorithms:\n1. **K-Means**: Fast, scalable, forces everything into a circle. Good default.\n2. **DBSCAN**: Finds weird shapes, automatically tags outliers (`-1`). Hard to tune `eps`. Fails if densities vary.\n3. **Hierarchical**: Gives a beautiful visual tree (Dendrogram) to help you pick K. Horrible for large datasets."),
    
    create_markdown_cell("## 13. Real-World Example\n**Biology (Genetics)**: Hierarchical clustering is the absolute standard in biology for DNA analysis. If you have the genetic sequences of 100 different species, you run Agglomerative Clustering. The resulting Dendrogram is literally the Evolutionary Tree of Life! It shows exactly which species mutated from which ancestors based on genetic distance."),
    
    create_markdown_cell("## 14. Mini Project\nBuild a Pipeline with `StandardScaler` and `AgglomerativeClustering(n_clusters=4)`. Test it on the data below and print the final Silhouette Score."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.metrics import silhouette_score",
        "",
        "X_proj, _ = make_blobs(n_samples=500, centers=4, cluster_std=0.5, random_state=42)",
        "",
        "agg_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('agg', AgglomerativeClustering(n_clusters=4, linkage='ward'))",
        "])",
        "",
        "# Note: Unsupervised models don't have a .predict() for new data (unless it's K-means).",
        "# We must use .fit_predict() on the exact data we want to label.",
        "labels_proj = agg_pipe.fit_predict(X_proj)",
        "",
        "score = silhouette_score(X_proj, labels_proj)",
        "print(f'Hierarchical Clustering Silhouette Score: {score:.3f}')"
    ]),
    
    create_markdown_cell("## 15. Common Mistakes\n- **Not Scaling Data**: Like all distance-based models, `StandardScaler` is required.\n- **Calling `.predict()`**: Agglomerative Clustering cannot predict new, unseen data points. It doesn't learn an equation or save a Centroid. It only groups the data it is currently looking at. You must use `.fit_predict()`.\n- **Using on Big Data**: Crashing the server because the distance matrix exceeds RAM."),
    
    create_markdown_cell("## 16. Interview Questions\n- **Beginner**: How does a Dendrogram help you choose the number of clusters? (Answer: You look for the longest vertical lines and cut horizontally through them).\n- **Intermediate**: Why can K-Means predict on new data, but Agglomerative Clustering cannot? (Answer: K-Means saves the physical coordinates of its Centroids. Agglomerative only remembers the merging history of the specific data it trained on).\n- **Advanced**: Explain the 'ward' linkage method. (Answer: Instead of merging the two clusters that are physically closest, 'ward' merges the two clusters that will result in the smallest increase in overall variance)."),
    
    create_markdown_cell("## 17. Knowledge Check\n- What is the tree diagram used in Hierarchical Clustering called? (Dendrogram)\n- Does Agglomerative clustering scale well to 1 million rows? (No, it causes memory errors)"),
    
    create_markdown_cell("## 18. Summary\n- **Agglomerative Clustering** is a bottom-up approach that merges points step-by-step.\n- It builds a **Dendrogram** showing the entire history of the dataset.\n- It is fantastic for visualization and choosing $K$.\n- It does not have a `.predict()` method for new data.\n- It is extremely computationally expensive on large datasets."),
    
    create_markdown_cell("## 19. Homework\nLoad the `load_wine` dataset. Scale it. Run `AgglomerativeClustering(n_clusters=3)` and get the labels. Calculate the `silhouette_score` and compare it to the score you got when you ran K-Means on the wine dataset in Day 21!")
]

# Read existing notebook and update cells
filename = "Day_23_Hierarchical_Clustering_and_DBSCAN.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day23_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
