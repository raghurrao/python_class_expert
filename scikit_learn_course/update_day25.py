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

day25_cells = [
    create_markdown_cell("# PHASE 4 — UNSUPERVISED LEARNING"),
    create_markdown_cell("# Day 25 — Unsupervised Project: Customer Segmentation"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this project, you will be able to:\n- Execute an end-to-end Unsupervised Machine Learning pipeline.\n- Combine PCA and K-Means to compress and cluster data simultaneously.\n- Use the Elbow Method to scientifically determine the optimal number of clusters.\n- Profile clusters to create actionable business \"Personas\"."),
    
    create_markdown_cell("## 2. Prerequisites\n- Phase 4 Concepts (K-Means, Silhouette Score, PCA, StandardScaler)."),
    
    create_markdown_cell("## 3. The Business Problem\nA retail supermarket has collected basic data on 2,000 customers who own membership cards. They have no idea how to market to these people. \nThe Chief Marketing Officer (CMO) asks you: *\"Can you group these customers into distinct 'personas' so we can run targeted ad campaigns? Also, can you show me a visual map of these groups?\"*"),
    
    create_markdown_cell("## 4. The Dataset\nWe have 5 features: Age, Annual Income ($), Spending Score (1-100), Family Size, and Distance to Store (miles).\nNotice there is no `y` target variable!"),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_blobs",
        "",
        "# 1. Generate underlying personas (we will act like we don't know these exist)",
        "np.random.seed(42)",
        "X_mock, _ = make_blobs(n_samples=2000, centers=4, n_features=5, cluster_std=1.5, random_state=42)",
        "",
        "# Give the features realistic scales",
        "df = pd.DataFrame(X_mock, columns=['Age', 'Annual_Income', 'Spending_Score', 'Family_Size', 'Distance_to_Store'])",
        "df['Age'] = np.abs(df['Age'] * 5 + 40).astype(int)              # 20 to 70",
        "df['Annual_Income'] = np.abs(df['Annual_Income'] * 15000 + 60000) # $40k to $120k",
        "df['Spending_Score'] = np.clip(np.abs(df['Spending_Score'] * 10 + 50), 1, 100) # 1 to 100",
        "df['Family_Size'] = np.clip(np.abs(df['Family_Size'] + 3), 1, 6).astype(int)",
        "df['Distance_to_Store'] = np.abs(df['Distance_to_Store'] * 2 + 5)",
        "",
        "print('Dataset Shape:', df.shape)",
        "print('\\nFirst 5 rows:')",
        "print(df.head())"
    ]),
    
    create_markdown_cell("## 5. Step 1: Preprocessing and PCA\nWe have 5 features. We cannot visualize 5 dimensions for the CMO. \nWe must scale the data, then use PCA to crush the 5 features down to 2 Principal Components."),
    create_code_cell([
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.decomposition import PCA",
        "from sklearn.pipeline import Pipeline",
        "",
        "# 2. Pipeline for scaling and PCA",
        "prep_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('pca', PCA(n_components=2, random_state=42))",
        "])",
        "",
        "# We transform the data",
        "X_2d = prep_pipe.fit_transform(df)",
        "",
        "pca_step = prep_pipe.named_steps['pca']",
        "variance_kept = sum(pca_step.explained_variance_ratio_)",
        "print(f'Variance kept by 2 components: {variance_kept * 100:.1f}%')"
    ]),
    
    create_markdown_cell("## 6. Step 2: The Elbow Method\nNow that we have compressed the data into `X_2d`, we need to figure out how many distinct customer groups exist. We will test K=1 through K=10 and plot the Inertia."),
    create_code_cell([
        "from sklearn.cluster import KMeans",
        "",
        "inertias = []",
        "K_range = range(1, 11)",
        "",
        "for k in K_range:",
        "    km = KMeans(n_clusters=k, random_state=42)",
        "    km.fit(X_2d)",
        "    inertias.append(km.inertia_)",
        "",
        "plt.figure(figsize=(8, 4))",
        "plt.plot(K_range, inertias, marker='o', linestyle='--')",
        "plt.xlabel('Number of Clusters (K)')",
        "plt.ylabel('Inertia (Tightness)')",
        "plt.title('The Elbow Method for Customer Segments')",
        "plt.xticks(K_range)",
        "plt.show()"
    ]),
    create_markdown_cell("> Look at the graph. The massive drops stop clearly at **K = 4**. We will tell the CMO there are 4 distinct customer personas."),
    
    create_markdown_cell("## 7. Step 3: Final Clustering and Visualization\nLet's train our final K-Means model with $K=4$ on our 2D data, and plot the customer map!"),
    create_code_cell([
        "from sklearn.metrics import silhouette_score",
        "",
        "final_kmeans = KMeans(n_clusters=4, random_state=42)",
        "cluster_labels = final_kmeans.fit_predict(X_2d)",
        "",
        "print(f'Final Silhouette Score: {silhouette_score(X_2d, cluster_labels):.2f}\\n')",
        "",
        "plt.figure(figsize=(10, 6))",
        "scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=cluster_labels, cmap='Set1', alpha=0.6)",
        "plt.scatter(final_kmeans.cluster_centers_[:, 0], final_kmeans.cluster_centers_[:, 1], ",
        "            c='black', s=300, marker='X', label='Centroids')",
        "plt.title('Customer Segments (PCA 2D Projection)')",
        "plt.xlabel('Principal Component 1')",
        "plt.ylabel('Principal Component 2')",
        "plt.legend()",
        "plt.show()"
    ]),
    
    create_markdown_cell("## 8. Step 4: Profiling the Personas\nThe CMO loves the graph, but asks: *\"What do the red dots actually mean? Are they young? Old? Rich? Poor?\"*\n\nBecause Principal Components are just math equations, we must attach the `cluster_labels` back to the **original raw dataset** to figure out what each group represents!"),
    create_code_cell([
        "df['Persona_ID'] = cluster_labels",
        "",
        "# Calculate the average statistics for each Persona",
        "persona_profiles = df.groupby('Persona_ID').mean().round(1)",
        "print(persona_profiles)"
    ]),
    
    create_markdown_cell("## 9. Business Conclusion\nBy looking at the averages above, we can name our Personas for the marketing team!\n*(Note: Your numbers may vary slightly due to randomness, but the distinct splits will remain).*\n\n1. **Persona 0 (The Wealthy Introverts)**: High Income, Small Family Size, Far from store.\n2. **Persona 1 (The Suburban Families)**: Average Income, Very Large Family Size, Medium distance.\n3. **Persona 2 (The Bargain Hunters)**: Low Income, Low Spending Score, Very close to store.\n4. **Persona 3 (The Big Spenders)**: Very High Spending Score, Medium Income.\n\nThe CMO can now send bulk discount diaper coupons to Persona 1, and luxury brand advertisements to Persona 0!"),
    
    create_markdown_cell("## 10. Phase 4 Evaluation\nYou have just completed Phase 4! You:\n1. Mastered Unsupervised Learning (no `y` target).\n2. Built **K-Means** clustering models to find hidden groups.\n3. Defeated complex geometry using **DBSCAN** density rules.\n4. Evaluated models blindly using the **Elbow Method** and **Silhouette Scores**.\n5. Defeated the Curse of Dimensionality using **PCA** compression.\n6. Combined PCA and K-Means to execute a real-world Marketing Segmentation pipeline!"),
    
    create_markdown_cell("## 11. Summary of Phase 4\nUnsupervised Learning is the \"Wild West\" of Machine Learning. It is highly experimental. The algorithms do exactly what you tell them mathematically, but it is ultimately up to the human Data Scientist to look at the resulting clusters, calculate their original feature averages, and derive actual business value from them.\n\nTomorrow, we begin our final week: **Phase 5 (Advanced Workflows)**, where we will learn Cross-Validation, Hyperparameter Tuning, and how to put these models into Production!")
]

# Read existing notebook and update cells
filename = "Day_25_Unsupervised_Project_Customer_Segmentation.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day25_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
