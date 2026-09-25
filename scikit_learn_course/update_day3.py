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

day3_cells = [
    create_markdown_cell("# PHASE 1 — MACHINE LEARNING FOUNDATIONS"),
    create_markdown_cell("# Day 03 — Dataset Splitting"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Use `train_test_split()` effectively.\n- Differentiate between the Training Set, Validation Set, and Test Set.\n- Explain Data Leakage and why evaluating on training data is dangerous.\n- Use `random_state` for reproducibility.\n- Apply stratification to handle imbalanced datasets."),
    
    create_markdown_cell("## 2. Prerequisites\n- Basic understanding of the Scikit-learn API (`fit`, `predict`).\n- A conceptual grasp of features (`X`) and targets (`y`)."),
    
    create_markdown_cell("## 3. Concept\nMachine learning models are prone to **memorizing** data rather than learning general patterns. If a model simply memorizes the data, it will perform perfectly on the data it has seen but fail miserably on new, unseen data.\n\nTo prevent this, we split our data:\n- **Training Set**: Used to fit the model (study).\n- **Validation Set**: Used to tune the model (practice exams).\n- **Test Set**: Used exactly once to evaluate the final model (final exam)."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nIf you evaluate a model on the same data you used to train it, you get an overly optimistic score. This is called **Data Leakage** (specifically, train/test contamination). \n\n**Rule of Thumb**: NEVER touch the test set until you are 100% finished training and tuning your model."),
    
    create_markdown_cell("## 5. Intuition\nImagine taking a math test where the teacher gave you the exact test questions the night before to study. If you score 100%, does it mean you are good at math, or does it mean you just memorized those specific questions? \n\nBy withholding a portion of the data (the test set), we evaluate the model's true ability to **generalize** to new situations."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nWhen we evaluate a model, we want to estimate the expected out-of-sample error:\n\n$$ Err_{T} = E[L(Y, \\hat{f}(X)) | T] $$\n\nWhere $T$ is the training set. If we estimate this error using the training set itself, the estimate is downward-biased (too low) because the model parameters were chosen specifically to minimize the error on $T$.\n\nThe test set provides an unbiased estimate of this error because it is independent of $T$."),
    
    create_markdown_cell("## 7. Scikit-learn API\nScikit-learn provides `train_test_split` inside the `model_selection` module."),
    create_code_cell([
        "from sklearn.model_selection import train_test_split",
        "# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
    ]),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate an imbalanced classification dataset and see what happens when we split it."),
    create_code_cell([
        "from sklearn.datasets import make_classification",
        "import numpy as np",
        "",
        "# Create imbalanced data (90% class 0, 10% class 1)",
        "X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, weights=[0.9], random_state=42)",
        "print('Original Target Distribution:')",
        "print(f'Class 0: {np.mean(y==0)*100:.1f}%')",
        "print(f'Class 1: {np.mean(y==1)*100:.1f}%\\n')",
        "",
        "# Basic split",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "print('Test Set Distribution (Without Stratification):')",
        "print(f'Class 0: {np.mean(y_test==0)*100:.1f}%')",
        "print(f'Class 1: {np.mean(y_test==1)*100:.1f}%')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- `make_classification(..., weights=[0.9])`: Creates a dataset where 90% of samples belong to Class 0.\n- `train_test_split`: Shuffles the data and splits 80% to train, 20% to test.\n- Note that in the output, the test set distribution might not perfectly match the original 90/10 split due to random chance."),
    
    create_markdown_cell("## 10. Experiment\nChange the code to use **stratification**. Stratification ensures the train and test sets have the exact same proportion of classes as the original dataset."),
    create_code_cell([
        "X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)",
        "print('Test Set Distribution (With Stratification):')",
        "print(f'Class 0: {np.mean(y_test_s==0)*100:.1f}%')",
        "print(f'Class 1: {np.mean(y_test_s==1)*100:.1f}%')"
    ]),
    create_markdown_cell("> Notice how it perfectly matches the original 90/10 split!"),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.2, random_state=99)",
        "X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.2, random_state=99)"
    ]),
    create_markdown_cell("> **Question:** Are `X_train1` and `X_train2` identical arrays? What happens if you remove `random_state=99`?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Are X_train1 and X_train2 identical?', np.array_equal(X_train1, X_train2))",
        "print('\\nWhy? `random_state` seeds the random number generator. Using the same seed guarantees the exact same shuffle and split every time. If you remove it, you get a different split every time you run the code.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nCreate a **Train / Validation / Test** split.\n1. Split `X` and `y` into `X_temp, X_test, y_temp, y_test` (Test size = 20%).\n2. Split `X_temp` and `y_temp` into `X_train, X_val, y_train, y_val` (Validation size = 25% of the temporary set)."),
    create_code_cell([
        "# YOUR CODE HERE",
        "X_temp, X_test_final, y_temp, y_test_final = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)",
        "# 25% of 80% is 20% of the total dataset.",
        "X_train_final, X_val_final, y_train_final, y_val_final = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp)",
        "",
        "print(f'Train shape: {X_train_final.shape}')",
        "print(f'Val shape: {X_val_final.shape}')",
        "print(f'Test shape: {X_test_final.shape}')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe junior data scientist tried to split the data, but the model crashed during training. Find the bug!"),
    create_code_cell([
        "from sklearn.linear_model import LogisticRegression",
        "",
        "# Buggy code",
        "try:",
        "    X_train_bug, X_test_bug, y_train_bug = train_test_split(X, y, test_size=0.2)",
        "    model = LogisticRegression()",
        "    model.fit(X_train_bug, y_train_bug)",
        "except Exception as e:",
        "    print('Error:', type(e).__name__)",
        "    print('Message:', e)"
    ]),
    create_markdown_cell("> **Hint:** Look at how many variables `train_test_split` unpacks into. Count them carefully!"),
    
    create_markdown_cell("## 14. Model Evaluation\nLet's prove why we split data. We will train a Decision Tree that is highly prone to memorizing data (overfitting)."),
    create_code_cell([
        "from sklearn.tree import DecisionTreeClassifier",
        "",
        "model = DecisionTreeClassifier(random_state=42)",
        "model.fit(X_train_s, y_train_s)",
        "",
        "train_score = model.score(X_train_s, y_train_s)",
        "test_score = model.score(X_test_s, y_test_s)",
        "",
        "print(f'Training Accuracy (Memorized): {train_score*100:.2f}%')",
        "print(f'Test Accuracy (Generalization): {test_score*100:.2f}%')"
    ]),
    create_markdown_cell("> If we didn't have a test set, we would think our model is 100% perfect!"),
    
    create_markdown_cell("## 15. Real-World Example\nIn real-world finance (e.g., predicting stock prices), random splitting is actually a bad idea! Since time matters, you must use **Time-Series Splitting** (e.g., train on 2018-2022, test on 2023). Random splitting would cause future data to leak into the training set!"),
    
    create_markdown_cell("## 16. Mini Project\nWrite a function `evaluate_split_impact(test_size)` that:\n1. Splits `X` and `y` (the imbalanced dataset from above) using the given `test_size` (no stratify).\n2. Trains a Logistic Regression model.\n3. Returns the test accuracy."),
    create_code_cell([
        "from sklearn.linear_model import LogisticRegression",
        "def evaluate_split_impact(test_size):",
        "    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=test_size, random_state=42)",
        "    model = LogisticRegression(random_state=42)",
        "    model.fit(X_tr, y_tr)",
        "    return model.score(X_te, y_te)",
        "",
        "print('Test Size 0.1:', evaluate_split_impact(0.1))",
        "print('Test Size 0.9:', evaluate_split_impact(0.9))"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Forgetting `random_state`**: Causes your results to change every time you run the notebook, making debugging impossible.\n- **Not using `stratify` on imbalanced data**: You might randomly get a test set that contains zero instances of the minority class!\n- **Leaking information**: E.g., scaling the data *before* splitting it. (We will cover this in depth tomorrow)."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: Why do we need a test set?\n- **Intermediate**: What is the difference between a validation set and a test set?\n- **Advanced**: When would you avoid using `train_test_split` with `shuffle=True`?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- What parameter ensures reproducible splits? (`random_state`)\n- What parameter ensures class proportions are maintained? (`stratify`)"),
    
    create_markdown_cell("## 20. Summary\n- Never evaluate on training data.\n- **Train** = Study. **Validation** = Practice Exam. **Test** = Final Exam.\n- Use `stratify=y` for classification problems.\n- Memorization is not Learning. Evaluation on unseen data proves generalization."),
    
    create_markdown_cell("## 21. Homework\nLoad the `load_digits()` dataset. Split it into 70% train and 30% test using stratification. Verify that the distributions of the digits (0-9) are equal in both sets using `np.bincount()`.")
]

# Read existing notebook and update cells
filename = "Day_03_Dataset_Splitting.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day3_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
