import json
import os

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

def generate_notebook(filename, title, phase, day_num, is_fleshed_out=False):
    cells = []
    
    # Title
    cells.append(create_markdown_cell(f"# {phase}"))
    cells.append(create_markdown_cell(f"# Day {day_num:02d} — {title}"))
    
    if is_fleshed_out:
        # Generate fully fleshed out content for Day 1
        cells.extend([
            create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Define Machine Learning and distinguish it from traditional programming.\n- Differentiate between Supervised, Unsupervised, and Semi-supervised learning.\n- Categorize problems into Regression, Classification, and Clustering.\n- Understand the terminology: Features (X), Target (y), Samples, Training, and Inference.\n- Set up and understand the Scikit-learn ecosystem."),
            
            create_markdown_cell("## 2. Prerequisites\n- Basic Python programming.\n- Fundamental NumPy (arrays, shapes).\n- Basic Pandas (DataFrames)."),
            
            create_markdown_cell("## 3. Concept\n**Machine Learning (ML)** is a subset of AI where systems learn from data to make predictions or decisions without being explicitly programmed.\n\nTypes of ML:\n- **Supervised Learning**: The dataset has labels (features `X` and target `y`). The goal is to learn a mapping from `X` to `y`.\n  - *Regression*: Predicting a continuous value (e.g., house price).\n  - *Classification*: Predicting a categorical value (e.g., spam vs. not spam).\n- **Unsupervised Learning**: The dataset has no labels. The goal is to find hidden structures.\n  - *Clustering*: Grouping similar data points together.\n- **Semi-supervised Learning**: A mix of a small amount of labeled data and a large amount of unlabeled data."),
            
            create_markdown_cell("## 4. Why Does This Matter?\nTraditional programming requires you to write the rules: `Data + Rules -> Answers`.\n\nMachine learning flips this paradigm: `Data + Answers -> Rules`.\n\nWithout ML, solving complex problems like image recognition, language translation, or predicting customer churn would require an impossible number of `if/else` statements."),
            
            create_markdown_cell("## 5. Intuition\nImagine teaching a child to recognize an apple.\nYou don't write rules like `if color == red and shape == round`. Instead, you show them dozens of apples and say \"This is an apple.\" Over time, they learn the pattern.\n\nIn ML:\n- The examples you show are the **Samples**.\n- The characteristics (color, shape, weight) are the **Features (X)**.\n- The label (\"apple\") is the **Target (y)**.\n- The learning process is **Training**.\n- When they correctly identify a new apple, that's **Inference**."),
            
            create_markdown_cell("## 6. Mathematical Foundation\nAt its core, supervised machine learning is about approximating a function $f$ such that:\n\n$$y \\approx f(X)$$\n\nWhere:\n- $X$ is an $n \\times p$ matrix ($n$ samples, $p$ features).\n- $y$ is an $n$-dimensional vector of targets.\n- The algorithm estimates $\\hat{f}$ to minimize some error between the predicted $\\hat{y}$ and true $y$."),
            
            create_markdown_cell("## 7. Scikit-learn API\nScikit-learn (imported as `sklearn`) is the industry-standard ML library in Python. It provides a clean, consistent API:"),
            create_code_cell("import sklearn\nprint(f'Scikit-learn version: {sklearn.__version__}')"),
            
            create_markdown_cell("## 8. Simple Example\nLet's generate a synthetic dataset and fit a simple classification model."),
            create_code_cell([
                "from sklearn.datasets import make_classification",
                "from sklearn.linear_model import LogisticRegression",
                "import matplotlib.pyplot as plt",
                "",
                "# 1. Create data (Features X, Target y)",
                "X, y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)",
                "",
                "# 2. Initialize the model",
                "model = LogisticRegression()",
                "",
                "# 3. Train the model",
                "model.fit(X, y)",
                "",
                "# 4. Inference (Predict)",
                "predictions = model.predict(X[:5])",
                "print('First 5 true targets:', y[:5])",
                "print('First 5 predictions: ', predictions)"
            ]),
            
            create_markdown_cell("## 9. Code Walkthrough\n- `make_classification()`: Generates a synthetic dataset for classification.\n- `X`: A 2D array of shape `(100, 2)` representing 100 samples and 2 features.\n- `y`: A 1D array of shape `(100,)` representing the class labels (0 or 1).\n- `LogisticRegression()`: Instantiates a classification algorithm.\n- `model.fit(X, y)`: The model looks at X and y and learns the relationship (Training).\n- `model.predict(X[:5])`: The model predicts the target for the first 5 samples (Inference)."),
            
            create_markdown_cell("## 10. Experiment\nChange `n_samples` to `1000` and observe if the model's accuracy changes. Visualize the data points."),
            create_code_cell([
                "plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolor='k')",
                "plt.title('Synthetic Classification Data')",
                "plt.xlabel('Feature 1')",
                "plt.ylabel('Feature 2')",
                "plt.show()"
            ]),
            
            create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
            create_code_cell([
                "model2 = LogisticRegression()",
                "model2.fit(X, y)",
                "predictions2 = model2.predict(X)",
                "proba = model2.predict_proba(X)"
            ]),
            create_markdown_cell("> **Question:** What is the shape of `predictions2`? What is the shape of `proba`?\n\n**Think before running the next cell!**"),
            create_code_cell([
                "print('Shape of predictions2:', predictions2.shape)",
                "print('Shape of proba:', proba.shape)",
                "print('\\nWhy? `predict` outputs a 1D array of class labels. `predict_proba` outputs a 2D array of probabilities for each class.')"
            ]),
            
            create_markdown_cell("## 12. Coding Exercise\nCreate a synthetic **regression** dataset using `make_regression(n_samples=200, n_features=1, noise=15)`. Then, train a `LinearRegression` model on it."),
            create_code_cell([
                "# YOUR CODE HERE",
                "from sklearn.datasets import make_regression",
                "from sklearn.linear_model import LinearRegression",
                "#"
            ]),
            
            create_markdown_cell("## 13. Debugging Challenge\nThe following code has a bug. Run it, read the error, diagnose it, and fix it!"),
            create_code_cell([
                "from sklearn.linear_model import LinearRegression",
                "import numpy as np",
                "",
                "X_bug = np.array([1, 2, 3, 4, 5]) # 1D array",
                "y_bug = np.array([2, 4, 6, 8, 10])",
                "",
                "model_bug = LinearRegression()",
                "# Uncomment to see the error:",
                "# model_bug.fit(X_bug, y_bug)"
            ]),
            create_markdown_cell("> **Hint:** Scikit-learn always expects `X` to be a 2D array (samples, features). How can you reshape `X_bug`?"),
            
            create_markdown_cell("## 14. Model Evaluation\nHow do we know if our model is good? We score it!"),
            create_code_cell([
                "accuracy = model.score(X, y)",
                "print(f'Model Accuracy: {accuracy * 100:.2f}%')"
            ]),
            create_markdown_cell("*(Note: Evaluating on the same data you trained on is a bad idea! We will learn why in Day 3.)*"),
            
            create_markdown_cell("## 15. Real-World Example\nIn the real world, machine learning is used to:\n- **Classification**: Detect fraudulent credit card transactions.\n- **Regression**: Predict tomorrow's stock price or temperature.\n- **Clustering**: Segment customers into groups for targeted marketing."),
            
            create_markdown_cell("## 16. Mini Project\n**Task**: Classify real-world problems.\nFor each of the following, state whether it is Regression, Classification, or Clustering:\n1. Predicting whether an email is spam or not.\n2. Grouping news articles by topic without knowing the topics beforehand.\n3. Predicting the exact sales revenue for next month.\n4. Identifying handwritten digits (0-9)."),
            create_markdown_cell("### Mini Project Answers\n1. Classification\n2. Clustering\n3. Regression\n4. Classification"),
            
            create_markdown_cell("## 17. Common Mistakes\n- **Confusing Features and Targets**: `X` is always your input data (features), `y` is the outcome you want to predict (target).\n- **Shape Errors**: Passing 1D arrays to models. `X` must be 2D `(n_samples, n_features)`.\n- **Import Errors**: Forgetting which module a class belongs to (e.g., `sklearn.linear_model`)."),
            
            create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What is the difference between supervised and unsupervised learning?\n- **Beginner**: In Scikit-learn, what do `X` and `y` conventionally represent?"),
            
            create_markdown_cell("## 19. Knowledge Check\n- What function do you call to train a model? (`fit`)\n- What function do you call to make new predictions? (`predict`)"),
            
            create_markdown_cell("## 20. Summary\n- Machine learning finds patterns in data.\n- **Supervised learning** uses labels; **unsupervised learning** does not.\n- `X` = features (2D), `y` = target (1D).\n- Scikit-learn models share a consistent `.fit()` and `.predict()` API."),
            
            create_markdown_cell("## 21. Homework\nExplore the `sklearn.datasets` module. Try loading the Iris dataset (`load_iris()`). Examine the shapes of `iris.data` and `iris.target`.")
        ])
    else:
        # Generate skeleton for other days
        sections = [
            "## 1. Learning Objectives",
            "## 2. Prerequisites",
            "## 3. Concept",
            "## 4. Why Does This Matter?",
            "## 5. Intuition",
            "## 6. Mathematical Foundation",
            "## 7. Scikit-learn API",
            "## 8. Simple Example",
            "## 9. Code Walkthrough",
            "## 10. Experiment",
            "## 11. Prediction Exercise",
            "## 12. Coding Exercise",
            "## 13. Debugging Challenge",
            "## 14. Model Evaluation",
            "## 15. Real-World Example",
            "## 16. Mini Project",
            "## 17. Common Mistakes",
            "## 18. Interview Questions",
            "## 19. Knowledge Check",
            "## 20. Summary",
            "## 21. Homework"
        ]
        for section in sections:
            cells.append(create_markdown_cell(f"{section}\n\n*Placeholder content for {title}*"))
            # Add an empty code cell after coding sections for user convenience
            if "Example" in section or "Exercise" in section or "Challenge" in section or "Project" in section:
                cells.append(create_code_cell("# YOUR CODE HERE\n"))

    notebook = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

def main():
    curriculum = [
        # Phase 1
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 1, "What_Is_Machine_Learning"),
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 2, "Scikit_learn_API_and_ML_Workflow"),
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 3, "Dataset_Splitting"),
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 4, "Preprocessing"),
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 5, "Pipelines"),
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 6, "ColumnTransformer"),
        ("PHASE 1 — MACHINE LEARNING FOUNDATIONS", 7, "Weekly_Project_Customer_Churn_Prediction"),
        
        # Phase 2
        ("PHASE 2 — REGRESSION", 8, "Linear_Regression"),
        ("PHASE 2 — REGRESSION", 9, "Regression_Evaluation"),
        ("PHASE 2 — REGRESSION", 10, "Regularization"),
        ("PHASE 2 — REGRESSION", 11, "Decision_Trees"),
        ("PHASE 2 — REGRESSION", 12, "Ensemble_Learning"),
        ("PHASE 2 — REGRESSION", 13, "Gradient_Boosting"),
        ("PHASE 2 — REGRESSION", 14, "Regression_Project_House_Price_Prediction"),
        
        # Phase 3
        ("PHASE 3 — CLASSIFICATION", 15, "Logistic_Regression"),
        ("PHASE 3 — CLASSIFICATION", 16, "Classification_Metrics"),
        ("PHASE 3 — CLASSIFICATION", 17, "K_Nearest_Neighbors"),
        ("PHASE 3 — CLASSIFICATION", 18, "Support_Vector_Machines"),
        ("PHASE 3 — CLASSIFICATION", 19, "Naive_Bayes"),
        ("PHASE 3 — CLASSIFICATION", 20, "Classification_Project_Fraud_Detection"),
        
        # Phase 4
        ("PHASE 4 — UNSUPERVISED LEARNING", 21, "Clustering"),
        ("PHASE 4 — UNSUPERVISED LEARNING", 22, "Choosing_Number_of_Clusters"),
        ("PHASE 4 — UNSUPERVISED LEARNING", 23, "Hierarchical_Clustering_and_DBSCAN"),
        ("PHASE 4 — UNSUPERVISED LEARNING", 24, "Dimensionality_Reduction"),
        ("PHASE 4 — UNSUPERVISED LEARNING", 25, "Unsupervised_Project_Customer_Segmentation"),
        
        # Phase 5
        ("PHASE 5 — MODEL SELECTION & ADVANCED ML", 26, "Cross_Validation"),
        ("PHASE 5 — MODEL SELECTION & ADVANCED ML", 27, "Hyperparameter_Tuning"),
        ("PHASE 5 — MODEL SELECTION & ADVANCED ML", 28, "Feature_Engineering_and_Selection"),
        ("PHASE 5 — MODEL SELECTION & ADVANCED ML", 29, "Model_Interpretation_and_Production"),
        ("PHASE 5 — MODEL SELECTION & ADVANCED ML", 30, "ML_Capstone"),
    ]
    
    out_dir = r"g:\Backup Fdrive\Python\scikit_learn_course"
    os.makedirs(out_dir, exist_ok=True)
    
    for phase, day_num, title in curriculum:
        filename = os.path.join(out_dir, f"Day_{day_num:02d}_{title}.ipynb")
        is_fleshed_out = (day_num == 1)
        generate_notebook(filename, title.replace('_', ' '), phase, day_num, is_fleshed_out)
        print(f"Created: {filename}")

if __name__ == "__main__":
    main()
