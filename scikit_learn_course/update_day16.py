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

day16_cells = [
    create_markdown_cell("# PHASE 3 — CLASSIFICATION"),
    create_markdown_cell("# Day 16 — Classification Metrics"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain why Accuracy is a terrible metric for imbalanced datasets.\n- Read and interpret a Confusion Matrix.\n- Calculate and explain Precision, Recall, and the F1 Score.\n- Use `classification_report` to instantly evaluate a model."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 15 (Logistic Regression)."),
    
    create_markdown_cell("## 3. Concept: The Accuracy Trap\nYesterday we used **Accuracy** (`Correct / Total`). \nImagine a dataset of 1,000 credit card transactions where only 1 transaction is Fraud (1) and 999 are Normal (0). This is called an **Imbalanced Dataset**.\n\nIf you build a \"dumb\" model that simply hardcodes `return 0` for every single transaction, it will correctly identify all 999 normal transactions and miss the 1 fraud. \nIts Accuracy is `999 / 1000 = 99.9%`!\n\nThe bank just deployed a 99.9% accurate model that catches absolutely zero fraud. Accuracy is a dangerous trap."),
    
    create_markdown_cell("## 4. The Confusion Matrix\nTo understand what our model is actually doing, we break its predictions into 4 buckets:\n1. **True Positives (TP)**: Model predicted Fraud, and it WAS Fraud. (Good!)\n2. **True Negatives (TN)**: Model predicted Normal, and it WAS Normal. (Good!)\n3. **False Positives (FP)**: Model predicted Fraud, but it was Normal. (Annoying - Customer gets angry SMS).\n4. **False Negatives (FN)**: Model predicted Normal, but it WAS Fraud. (Catastrophic - Money is stolen)."),
    
    create_markdown_cell("## 5. Precision vs Recall\nFrom the Confusion Matrix, we calculate two critical metrics:\n\n**Precision**: Out of all the times the model *yelled* \"Fraud!\", how many times was it actually right?\n$$ Precision = \\frac{TP}{TP + FP} $$\n*High Precision means you don't cry wolf. You rarely annoy customers with false alarms.*\n\n**Recall (Sensitivity)**: Out of all the *actual* Frauds that happened, how many did the model catch?\n$$ Recall = \\frac{TP}{TP + FN} $$\n*High Recall means you catch almost all the bad guys, even if you accidentally annoy some normal customers in the process.*"),
    
    create_markdown_cell("## 6. The F1 Score\nYou cannot have 100% Precision and 100% Recall (unless the model is perfect). \nIf you want to catch every fraud (High Recall), you have to lower your decision boundary to 0.1, which will flag tons of normal transactions (Low Precision).\n\nThe **F1 Score** is the harmonic mean of Precision and Recall. It is a single number that punishes extreme imbalances. If your Precision is 0.99 but your Recall is 0.01, your F1 Score will be terrible (unlike Accuracy)."),
    
    create_markdown_cell("## 7. Scikit-learn API\n```python\nfrom sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate a highly imbalanced dataset representing a rare disease (10 sick patients out of 100)."),
    create_code_cell([
        "import numpy as np",
        "import pandas as pd",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report",
        "",
        "# 1. Generate Imbalanced Data",
        "np.random.seed(42)",
        "X = np.random.rand(100, 2)",
        "y = np.zeros(100)",
        "y[:10] = 1 # Only 10 positive cases (10% prevalence)",
        "np.random.shuffle(y)",
        "",
        "# Make the positive cases somewhat distinct but overlapping",
        "X[y == 1] += 0.5 ",
        "",
        "# 2. Train Model",
        "model = LogisticRegression()",
        "model.fit(X, y)",
        "y_pred = model.predict(X)"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We created 100 patients. 90 are Healthy (0), 10 are Sick (1).\n- We trained a standard `LogisticRegression` on it and generated predictions."),
    
    create_markdown_cell("## 10. Experiment\nLet's calculate the Accuracy, Confusion Matrix, and our new metrics."),
    create_code_cell([
        "from sklearn.metrics import accuracy_score",
        "from sklearn.metrics import ConfusionMatrixDisplay",
        "import matplotlib.pyplot as plt",
        "",
        "print(f'Accuracy:  {accuracy_score(y, y_pred):.2f}')",
        "print(f'Precision: {precision_score(y, y_pred):.2f}')",
        "print(f'Recall:    {recall_score(y, y_pred):.2f}')",
        "print(f'F1 Score:  {f1_score(y, y_pred):.2f}\\n')",
        "",
        "print('Confusion Matrix:')",
        "cm = confusion_matrix(y, y_pred)",
        "disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Healthy (0)', 'Sick (1)'])",
        "disp.plot(cmap='Blues')",
        "plt.show()"
    ]),
    create_markdown_cell("> Look at the matrix! The model got an Accuracy of ~90%... but it only caught 2 out of the 10 sick patients (Recall = 0.20)! It missed 8 sick people (False Negatives). This model is dangerous, despite its high accuracy."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "y_true_mock = [1, 1, 1, 0, 0]",
        "y_pred_dumb = [0, 0, 0, 0, 0] # A dumb model that just says 0 to everything"
    ]),
    create_markdown_cell("> **Question:** What is the Recall of this dumb model? What is its Precision?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Recall of dumb model:   ', recall_score(y_true_mock, y_pred_dumb, zero_division=0))",
        "print('Precision of dumb model:', precision_score(y_true_mock, y_pred_dumb, zero_division=0))",
        "print('\\nWhy? It caught 0 out of the 3 real positives (Recall = 0/3).')",
        "print('It never predicted 1, so Precision is mathematically 0/0 (Scikit-learn defaults to 0).')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nScikit-learn provides a magical function called `classification_report` that calculates all of this instantly for both classes. \nPass `y` and `y_pred` into `classification_report()` and print the result."),
    create_code_cell([
        "# YOUR CODE HERE",
        "report = classification_report(y, y_pred)",
        "print(report)",
        "print('\\nNotice how Class 0 (Healthy) has near perfect scores, but Class 1 (Sick) has terrible scores. This is exactly what the F1 score reveals!')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA Machine Learning engineer at a hospital is trying to maximize Recall because they don't want to miss a single tumor. They set the probability threshold to `0.0001`. They achieved 100% Recall! \nHowever, the doctors are furious and refuse to use the software. Why?"),
    create_code_cell([
        "# Buggy business logic",
        "probs = model.predict_proba(X)[:, 1]",
        "extreme_recall_preds = (probs > 0.0001).astype(int)",
        "print('Recall:   ', recall_score(y, extreme_recall_preds))",
        "print('Precision:', precision_score(y, extreme_recall_preds))"
    ]),
    create_markdown_cell("> **Hint:** If you set the threshold to 0.0001, the model will classify almost EVERYONE as having a tumor. \n> Recall hits 100%, but Precision plummets to ~10%. The doctors are furious because the model is screaming \"TUMOR!\" at 90 healthy people, forcing them to do unnecessary, expensive, and stressful biopsies on healthy patients. \n> **Rule:** There is always a tradeoff between Precision and Recall."),
    
    create_markdown_cell("## 14. Model Evaluation (Tradeoff)\nYou can mathematically slide your Precision and Recall up and down by changing the decision boundary threshold. \n- **Increase Threshold (e.g., 0.9)**: Precision goes up, Recall goes down. (Conservative model).\n- **Decrease Threshold (e.g., 0.1)**: Recall goes up, Precision goes down. (Aggressive model)."),
    
    create_markdown_cell("## 15. Real-World Example\n- **YouTube Recommendations**: Google wants to recommend a video you'll click. If they recommend a video you don't like (False Positive), you just ignore it. No big deal. But they want to make sure out of the 5 videos they show, all 5 are highly relevant. They optimize for **High Precision**.\n- **Self-Driving Cars**: The car's camera thinks a shadow *might* be a pedestrian. A False Positive means the car slams on the brakes for a shadow (annoying). A False Negative means the car runs over a human (fatal). Tesla optimizes for **High Recall**."),
    
    create_markdown_cell("## 16. Mini Project\nWrite a loop that calculates the F1 score for thresholds: `[0.2, 0.5, 0.8]`. Which threshold gives the highest F1 score for our sick patients?"),
    create_code_cell([
        "thresholds = [0.2, 0.5, 0.8]",
        "for t in thresholds:",
        "    custom_p = (probs > t).astype(int)",
        "    f1 = f1_score(y, custom_p)",
        "    print(f'Threshold {t:.1f} -> F1 Score: {f1:.2f}')",
        "",
        "print('\\nDropping the threshold to 0.2 made the model slightly more aggressive, which drastically improved its F1 score on this imbalanced dataset!')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Using Accuracy on Imbalanced Data**: The #1 mistake junior data scientists make. Always check `value_counts()` on your target variable first!\n- **Confusing Precision and Recall**: \n  - Precision = \"When you *say* positive, are you right?\"\n  - Recall = \"Did you *find* all the positives?\""),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: Why is Accuracy a bad metric for detecting credit card fraud?\n- **Intermediate**: Explain the difference between a False Positive and a False Negative.\n- **Advanced**: If your spam filter is putting important emails from your boss into the Spam folder, is your model suffering from low Precision or low Recall? (Answer: Low Precision. It predicted Spam (Positive) when it was actually Normal (Negative). This is a False Positive)."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What metric is the harmonic mean of Precision and Recall? (F1 Score)\n- What function prints all metrics for all classes instantly? (`classification_report`)"),
    
    create_markdown_cell("## 20. Summary\n- **Accuracy** is dangerously misleading on imbalanced datasets.\n- **Confusion Matrix** shows TP, TN, FP, FN.\n- **Precision**: Focuses on minimizing False Positives (Don't cry wolf).\n- **Recall**: Focuses on minimizing False Negatives (Don't miss the bad guys).\n- **F1 Score**: Balances both.\n- Use `classification_report` for a complete breakdown."),
    
    create_markdown_cell("## 21. Homework\nLoad the `load_wine` dataset. It has 3 classes. Train a Logistic Regression model and use `classification_report`. Notice how the report beautifully handles multi-class classification by providing Precision and Recall for *each* of the 3 wine types separately!")
]

# Read existing notebook and update cells
filename = "Day_16_Classification_Metrics.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day16_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
