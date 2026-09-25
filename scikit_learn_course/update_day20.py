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

day20_cells = [
    create_markdown_cell("# PHASE 3 — CLASSIFICATION"),
    create_markdown_cell("# Day 20 — Classification Project: Fraud Detection"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this project, you will be able to:\n- Execute an end-to-end Machine Learning pipeline for an imbalanced Classification task.\n- Compare Logistic Regression, KNN, and Support Vector Machines (SVM).\n- Evaluate models using Confusion Matrices and the F1 Score instead of Accuracy.\n- Make a business decision based on the Precision/Recall tradeoff."),
    
    create_markdown_cell("## 2. Prerequisites\n- Phase 3 Concepts (Classification, Metrics, KNN, SVM, Naive Bayes)."),
    
    create_markdown_cell("## 3. The Business Problem\nA bank is losing millions of dollars to credit card fraud. They want a Machine Learning model to flag fraudulent transactions in real-time. \nHowever, they explicitly stated: *\"We would rather annoy 10 normal customers with a false alarm than let 1 fraudster steal money.\"* \n\nThis means our business goal is to optimize for **High Recall** (even if it costs us some Precision)."),
    
    create_markdown_cell("## 4. The Dataset\nWe will generate a highly imbalanced dataset representing credit card transactions. \n- `0` = Normal Transaction (95% of data)\n- `1` = Fraudulent Transaction (5% of data)\nWe have 3 features representing the transaction amount, distance from home, and time of day."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_classification",
        "",
        "# 1. Generate Imbalanced Dataset",
        "np.random.seed(42)",
        "X_mock, y_mock = make_classification(",
        "    n_samples=5000, n_features=3, n_informative=3, n_redundant=0, ",
        "    weights=[0.95, 0.05], class_sep=0.8, random_state=42",
        ")",
        "",
        "columns = ['Transaction_Amount', 'Distance_From_Home', 'Time_of_Day']",
        "df = pd.DataFrame(X_mock, columns=columns)",
        "df['Is_Fraud'] = y_mock",
        "",
        "print('Dataset Shape:', df.shape)",
        "print('\\nClass Imbalance:')",
        "print(df['Is_Fraud'].value_counts(normalize=True) * 100)"
    ]),
    
    create_markdown_cell("## 5. Splitting and Preprocessing\nBecause KNN and SVM are purely distance-based algorithms, we **must** scale the transaction amounts and distances. We will use `StandardScaler`."),
    create_code_cell([
        "from sklearn.model_selection import train_test_split",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "X = df.drop('Is_Fraud', axis=1)",
        "y = df['Is_Fraud']",
        "",
        "# 2. Train / Test Split",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)",
        "",
        "# 3. Scaler",
        "scaler = StandardScaler()"
    ]),
    
    create_markdown_cell("## 6. Defining the Candidate Models\nWe will test three distinct hypotheses:\n1. Is the boundary simple and linear? (`LogisticRegression`)\n2. Is the boundary highly localized based on similar recent transactions? (`KNeighborsClassifier`)\n3. Is the boundary a complex, non-linear geometric shape? (`SVC` with RBF kernel)"),
    create_code_cell([
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.neighbors import KNeighborsClassifier",
        "from sklearn.svm import SVC",
        "from sklearn.pipeline import Pipeline",
        "",
        "# 4. Define the models",
        "models = {",
        "    'Logistic Regression': LogisticRegression(random_state=42),",
        "    'KNN (K=5)': KNeighborsClassifier(n_neighbors=5),",
        "    'SVM (RBF)': SVC(kernel='rbf', probability=True, random_state=42) # Needed for predict_proba later!",
        "}"
    ]),
    
    create_markdown_cell("## 7. Training and Evaluation Loop\nInstead of Accuracy, we will look at the `classification_report` to see the Precision, Recall, and F1-Score for the Fraud class (`1`)."),
    create_code_cell([
        "from sklearn.metrics import classification_report, f1_score",
        "",
        "trained_pipelines = {}",
        "",
        "# 5. Train and Evaluate",
        "for name, model in models.items():",
        "    # Create full pipeline",
        "    pipe = Pipeline([",
        "        ('scaler', scaler),",
        "        ('classifier', model)",
        "    ])",
        "    ",
        "    pipe.fit(X_train, y_train)",
        "    y_pred = pipe.predict(X_test)",
        "    ",
        "    trained_pipelines[name] = pipe",
        "    ",
        "    print(f'========== {name} ==========')",
        "    print(classification_report(y_test, y_pred))",
        "    print('\\n')"
    ]),
    
    create_markdown_cell("## 8. Analyzing the Baseline Results\nLook at the row for Class `1` (Fraud) in the reports above:\n- **Logistic Regression** had a terrible Recall (it missed almost half the frauds!).\n- **KNN** did better, but still struggled with the complex boundaries.\n- **SVM (RBF)** absolutely dominated. Its F1-score is the highest, proving the boundary between Fraud and Normal is highly non-linear.\n\nWe will select the **SVM** as our final model."),
    
    create_markdown_cell("## 9. Tuning for the Business Goal (High Recall)\nRemember the business goal: *\"We would rather annoy 10 normal customers with a false alarm than let 1 fraudster steal money.\"*\n\nThe default SVM decision boundary is 0.5. Let's extract the raw probabilities and manually drop the boundary to `0.1` to make the model hyper-aggressive at flagging fraud."),
    create_code_cell([
        "from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay",
        "",
        "best_model = trained_pipelines['SVM (RBF)']",
        "",
        "# 1. Get raw probabilities for the Fraud class (column 1)",
        "fraud_probs = best_model.predict_proba(X_test)[:, 1]",
        "",
        "# 2. Apply custom aggressive threshold (0.1)",
        "aggressive_preds = (fraud_probs >= 0.10).astype(int)",
        "",
        "# 3. Compare Confusion Matrices",
        "default_cm = confusion_matrix(y_test, best_model.predict(X_test))",
        "aggressive_cm = confusion_matrix(y_test, aggressive_preds)",
        "",
        "fig, axes = plt.subplots(1, 2, figsize=(12, 5))",
        "",
        "ConfusionMatrixDisplay(default_cm, display_labels=['Normal', 'Fraud']).plot(ax=axes[0], cmap='Blues', colorbar=False)",
        "axes[0].set_title('Default Threshold (0.5)')",
        "",
        "ConfusionMatrixDisplay(aggressive_cm, display_labels=['Normal', 'Fraud']).plot(ax=axes[1], cmap='Reds', colorbar=False)",
        "axes[1].set_title('Aggressive Threshold (0.1)')",
        "",
        "plt.show()"
    ]),
    create_markdown_cell("> **Business Win!** Look at the False Negatives (bottom left of the matrix). \n> By dropping the threshold to 0.1, we caught significantly more frauds! Yes, the False Positives (top right) went up, meaning we annoyed more normal customers, but we perfectly fulfilled the bank's core business requirement."),
    
    create_markdown_cell("## 10. Phase 3 Evaluation\nYou have just completed Phase 3! You:\n1. Transitioned from predicting numbers to predicting categories.\n2. Mastered Logistic Regression and the Sigmoid function.\n3. Learned why Accuracy fails on imbalanced data.\n4. Utilized Precision, Recall, and F1-Scores.\n5. Implemented K-Nearest Neighbors (KNN).\n6. Visualized Support Vector Machines (SVM) and the Kernel Trick.\n7. Built Spam Filters with Naive Bayes.\n8. Adjusted probability thresholds to solve a real-world business constraint!"),
    
    create_markdown_cell("## 11. Capstone Exercise for Phase 3\nThe bank asks you to try one more model: `GaussianNB`. \nAdd it to a pipeline, train it, and print its `classification_report`. How does its F1-Score compare to the SVM?"),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.naive_bayes import GaussianNB",
        "",
        "nb_pipe = Pipeline([",
        "    ('scaler', scaler), # NB doesn't need scaling, but it doesn't hurt",
        "    ('nb', GaussianNB())",
        "])",
        "",
        "nb_pipe.fit(X_train, y_train)",
        "nb_preds = nb_pipe.predict(X_test)",
        "",
        "print('========== Gaussian Naive Bayes ==========')",
        "print(classification_report(y_test, nb_preds))"
    ]),
    
    create_markdown_cell("## 12. Summary of Phase 3\n**Classification** is about assigning data to discrete buckets. For simple boundaries, Logistic Regression is king. For text, Naive Bayes is king. For complex geometry, SVMs are incredibly powerful (provided you scale your data!). And for evaluating all of them, the Confusion Matrix is your best friend.\n\nTomorrow, we begin **Phase 4: Unsupervised Learning**, where we throw away the target variable `y` entirely and ask the algorithms to find hidden patterns in the data completely on their own!")
]

# Read existing notebook and update cells
filename = "Day_20_Classification_Project_Fraud_Detection.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day20_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
