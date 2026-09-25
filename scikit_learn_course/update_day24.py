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

day24_cells = [
    create_markdown_cell("# PHASE 4 — UNSUPERVISED LEARNING"),
    create_markdown_cell("# Day 24 — Dimensionality Reduction (PCA)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain the \"Curse of Dimensionality\".\n- Understand how Principal Component Analysis (PCA) crushes 100 features into 2 while preserving information.\n- Interpret the `explained_variance_ratio_`.\n- Explain why `StandardScaler` is absolutely mandatory before running PCA."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 4 (StandardScaler)."),
    
    create_markdown_cell("## 3. Concept: The Curse of Dimensionality\nAs you add more features (columns) to your dataset, the mathematical space grows exponentially. If you have 500 features, data points become incredibly far apart in that 500-dimensional space. \nModels like KNN and SVM (which rely on measuring distance) break down entirely. Furthermore, having hundreds of features leads to massive overfitting and agonizingly slow training times.\n\nWe need a way to **reduce the number of dimensions** without throwing away the data."),
    
    create_markdown_cell("## 4. Concept: PCA (Principal Component Analysis)\nImagine holding a 3D coffee mug and shining a flashlight on it. The shadow cast on the wall is a 2D representation of the 3D mug. If you hold it from the top, the shadow is just a circle (you lose the handle). If you hold it from the side, the shadow shows the cup and the handle perfectly. \n\n**PCA** mathematically rotates your massive, multi-dimensional dataset until it finds the \"angle\" that casts the most informative shadow. \nIt then projects the data down onto that shadow (e.g., crushing 100 features into just 2 Principal Components)."),
    
    create_markdown_cell("## 5. What is \"Information\"?\nTo PCA, \"Information\" = **Variance**. \nIf every house in a dataset has 3 bedrooms, the `Bedrooms` feature has 0 variance. It tells us nothing useful. If `Square_Footage` ranges from 500 to 10,000, it has huge variance and is highly informative.\nPCA finds new mathematical axes (Components) that capture the maximum possible variance in the data."),
    
    create_markdown_cell("## 6. Scikit-learn API\n```python\nfrom sklearn.decomposition import PCA\n# You can tell it how many components you want (e.g., 2 for a 2D scatter plot)\n# Or tell it how much variance you want to keep (e.g., 0.95 for 95% of information)\npca = PCA(n_components=2)\npca = PCA(n_components=0.95)\n```"),
    
    create_markdown_cell("## 7. Simple Example: Crushing Data\nLet's generate a dataset with 50 features. We will use PCA to crush it down to just 2 features so we can visualize it on a standard 2D scatter plot."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_classification",
        "from sklearn.decomposition import PCA",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "# 1. Generate 50-dimensional data",
        "X, y = make_classification(n_samples=500, n_features=50, n_informative=10, random_state=42)",
        "",
        "# 2. Scale the data (CRITICAL!)",
        "scaler = StandardScaler()",
        "X_scaled = scaler.fit_transform(X)",
        "",
        "# 3. Run PCA to crush 50 features into 2 Principal Components",
        "pca_2d = PCA(n_components=2, random_state=42)",
        "X_pca_2d = pca_2d.fit_transform(X_scaled)",
        "",
        "print(f'Original Shape: {X.shape}')",
        "print(f'New Shape:      {X_pca_2d.shape}')"
    ]),
    
    create_markdown_cell("## 8. Code Walkthrough\n- We started with an `X` that was 50 columns wide. You cannot plot a 50-dimensional graph.\n- We ran `pca.fit_transform()`. It analyzed the 50 columns, found the best \"angle\" to cast a shadow, and returned `X_pca_2d`, which is only 2 columns wide!"),
    
    create_markdown_cell("## 9. Experiment: Visualizing the Un-visualizable\nSince the data is now exactly 2 columns, we can plot it! Let's color the dots using the original `y` labels to see if PCA successfully kept the classes separated even after destroying 48 dimensions."),
    create_code_cell([
        "plt.figure(figsize=(8, 5))",
        "plt.scatter(X_pca_2d[:, 0], X_pca_2d[:, 1], c=y, cmap='coolwarm', alpha=0.7)",
        "plt.xlabel('Principal Component 1 (PC1)')",
        "plt.ylabel('Principal Component 2 (PC2)')",
        "plt.title('50 Features crushed into 2D using PCA')",
        "plt.show()"
    ]),
    create_markdown_cell("> Look at that! The blue and red dots are largely separated. This means PCA successfully extracted the core \"meaning\" of those 50 features and condensed it into just 2 math equations!"),
    
    create_markdown_cell("## 10. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "variance_kept = sum(pca_2d.explained_variance_ratio_)"
    ]),
    create_markdown_cell("> **Question:** We crushed 50 features down to 2. Did we keep 100% of the information? Did we keep 50%? \n> `pca.explained_variance_ratio_` tells us exactly what percentage of the original data's variance was captured by each Principal Component.\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Variance captured by PC1:', pca_2d.explained_variance_ratio_[0])",
        "print('Variance captured by PC2:', pca_2d.explained_variance_ratio_[1])",
        "print(f'Total Information Kept:   {variance_kept * 100:.1f}%')",
        "print('\\nWe threw away 85% of the information! 2 components was clearly not enough for this dataset.')"
    ]),
    
    create_markdown_cell("## 11. Coding Exercise\nWe don't want to throw away 85% of our data. We want to keep 90% of the variance, and we don't care how many components it takes. \nInstantiate a new `PCA` model, but pass `n_components=0.90`. Fit it on `X_scaled`, and print out `pca_90.n_components_` to see how many components were required."),
    create_code_cell([
        "# YOUR CODE HERE",
        "pca_90 = PCA(n_components=0.90, random_state=42)",
        "X_pca_90 = pca_90.fit_transform(X_scaled)",
        "",
        "print(f'Original features: 50')",
        "print(f'Features needed to keep 90% of variance: {pca_90.n_components_}')",
        "print('\\nWe successfully compressed the dataset by ~25% while keeping 90% of its predictive power!')"
    ]),
    
    create_markdown_cell("## 12. Debugging Challenge\nA data analyst runs PCA on a housing dataset to compress `Bedrooms` (1 to 5) and `Price` ($100,000 to $1,000,000). \nPCA assigns 99.9% of the \"importance\" to the `Price` variable, completely ignoring `Bedrooms`. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: The model was not StandardScaled.')",
        "print('Why? PCA defines \"Information\" as \"Variance\".')",
        "print('The variance of Bedrooms is tiny (varies from 1 to 5).')",
        "print('The variance of Price is massive (varies by millions).')",
        "print('To PCA, Price looks infinitely more informative, so it builds the Principal Components almost entirely out of Price.')"
    ]),
    create_markdown_cell("> **Rule:** PCA is completely useless if you do not `StandardScale` your data first! Every feature must have a variance of 1 so that PCA evaluates them fairly."),
    
    create_markdown_cell("## 13. Model Evaluation\nWhat is a Principal Component?\nIf PC1 = `0.8 * Square_Footage + 0.2 * Bedrooms`, it is a mathematical Frankenstein feature. \nThis is the biggest downside of PCA: **Loss of Interpretability**. \nIf your boss asks, *\"Why did the model reject this loan?\"*, you cannot say *\"Because his income was too low.\"* You have to say *\"Because his PC1 was too low,\"* which means nothing to a human."),
    
    create_markdown_cell("## 14. Real-World Example\n**Facial Recognition**: An image of a face is 100x100 pixels (10,000 features). Running SVM on 10,000 features is slow. Researchers use PCA to crush those 10,000 pixels down into 150 Principal Components (often called \"Eigenfaces\"). These 150 components capture 95% of the structural variance of a human face. The SVM then trains on those 150 components in a fraction of a second!"),
    
    create_markdown_cell("## 15. Mini Project\nLet's prove the importance of Scaling. Generate data where one feature is artificially massive. Run PCA *without* scaling and print PC1's components. Then use a Pipeline to scale it first, and print PC1's components again."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "",
        "# 1. Create data where Feature 1 is massive",
        "np.random.seed(42)",
        "X_bad = np.random.rand(100, 3)",
        "X_bad[:, 1] *= 1000000",
        "",
        "# 2. Unscaled PCA (Terrible)",
        "bad_pca = PCA(n_components=2)",
        "bad_pca.fit(X_bad)",
        "print('Unscaled PC1 formula:', bad_pca.components_[0])",
        "print('Notice how Feature 1 is literally 1.0 (100%), and the others are exactly 0.0. PCA completely ignored them!')",
        "",
        "# 3. Scaled PCA (Good)",
        "good_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('pca', PCA(n_components=2))",
        "])",
        "good_pipe.fit(X_bad)",
        "good_pca = good_pipe.named_steps['pca']",
        "print('\\nScaled PC1 formula:  ', good_pca.components_[0])",
        "print('With scaling, PCA actually looks at all the features fairly to build the Component.')"
    ]),
    
    create_markdown_cell("## 16. Common Mistakes\n- **Not Scaling Data**: The absolute quickest way to fail an interview regarding PCA.\n- **Worrying about interpretability**: If your stakeholders need to know *exactly* which original features drove the prediction, do not use PCA.\n- **Using PCA to prevent overfitting**: PCA is for *compression* and *speed*. Using it solely to prevent overfitting is a bad practice (use Ridge/Lasso Regularization for that)."),
    
    create_markdown_cell("## 17. Interview Questions\n- **Beginner**: Why do we use PCA? (Answer: To reduce the number of features/dimensions in a dataset while keeping most of the information, which speeds up training and allows visualization).\n- **Intermediate**: What does it mean if `pca.explained_variance_ratio_` for PC1 is 0.80? (Answer: It means that a single mathematical component contains 80% of the variance/information of the entire original dataset).\n- **Advanced**: Why is `StandardScaler` absolutely mandatory for PCA? (Answer: Because PCA maximizes variance. If a feature has large units (like salary in dollars vs age in years), its raw variance will mathematically dominate the PCA calculation, causing PCA to ignore the other features)."),
    
    create_markdown_cell("## 18. Knowledge Check\n- What does PCA stand for? (Principal Component Analysis)\n- If `n_components = 0.95`, what does the 0.95 represent? (Keep 95% of the variance)"),
    
    create_markdown_cell("## 19. Summary\n- **Curse of Dimensionality**: Too many features breaks algorithms and causes overfitting.\n- **PCA** mathematically compresses features into Principal Components.\n- **Explained Variance**: The percentage of original information a component captured.\n- **Loss of Interpretability**: Principal Components are unreadable math equations.\n- You MUST use `StandardScaler`."),
    
    create_markdown_cell("## 20. Homework\nLoad the `load_digits` dataset from Scikit-learn (it has 64 features representing an 8x8 pixel image). Build a Pipeline with `StandardScaler` and `PCA(n_components=2)`. Plot the 2D scatter plot and color it by the actual digit `y`. See if PCA can visually separate handwritten numbers into blobs!")
]

# Read existing notebook and update cells
filename = "Day_24_Dimensionality_Reduction.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day24_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
