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

day28_cells = [
    create_markdown_cell("# PHASE 5 — ADVANCED WORKFLOWS & PRODUCTION"),
    create_markdown_cell("# Day 28 — Feature Engineering and Selection"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Construct new columns of data mathematically using **Feature Engineering**.\n- Extract importance scores from models using `.feature_importances_`.\n- Automatically drop useless data using **RFE** (Recursive Feature Elimination)."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 12 & 13 (Decision Trees & Random Forests)."),
    
    create_markdown_cell("## 3. Concept: Feature Engineering\nMachine Learning models can only learn from the data you give them. If you give a model the `Width` and `Length` of a house, a simple linear model might struggle to predict the price. \nBut if YOU mathematically create a new column called `Square_Footage = Width * Length`, you instantly hand the model the exact relationship it needs to succeed. \n**Feature Engineering** is the art of creating new features out of thin air using human domain knowledge."),
    
    create_markdown_cell("## 4. Concept: Feature Selection (Dropping Data)\nJust as adding good features helps, adding bad features hurts. If you feed a model `House_Price`, `Square_Footage`, and `Owner_Favorite_Color`, the model might accidentally learn that \"Blue\" means expensive. \nThis is \"Noise\". We need to mathematically prove which features are useless and delete them from the dataset."),
    
    create_markdown_cell("## 5. Scikit-learn API\n```python\nfrom sklearn.feature_selection import RFE\n# Create a tool that eliminates the worst features until only 5 remain\nselector = RFE(estimator=RandomForestClassifier(), n_features_to_select=5)\n# X_reduced is now just the 5 best columns!\nX_reduced = selector.fit_transform(X, y)\n```"),
    
    create_markdown_cell("## 6. Simple Example: Engineering Features\nLet's generate a pandas DataFrame representing a car dataset. We will engineer new features that a human knows are important, but a machine might not figure out immediately."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "",
        "# 1. Raw Data",
        "data = {",
        "    'Weight_lbs': [3000, 4500, 2500, 5000, 2000],",
        "    'Horsepower': [150, 300, 120, 400, 90],",
        "    'Year_Made': [2010, 2018, 2005, 2022, 1999]",
        "}",
        "df = pd.DataFrame(data)",
        "print('Original Data:')",
        "print(df)",
        "",
        "# 2. Feature Engineering",
        "CURRENT_YEAR = 2024",
        "df['Age_Years'] = CURRENT_YEAR - df['Year_Made']",
        "df['Power_to_Weight_Ratio'] = df['Horsepower'] / df['Weight_lbs']",
        "",
        "print('\\nEngineered Data:')",
        "print(df[['Age_Years', 'Power_to_Weight_Ratio']])"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We created `Age_Years`. Why? Because `2010` is an arbitrary number to a machine. But knowing the car is `14` years old is a direct, linear metric of wear-and-tear.\n- We created `Power_to_Weight_Ratio`. A 300-horsepower truck isn't fast because it weighs 5,000 lbs. A 150-horsepower motorcycle is a rocket because it weighs 500 lbs. We explicitly handed this physics concept to the model!"),
    
    create_markdown_cell("## 8. Experiment: Feature Importance\nNow let's see how we can ask a model which features are actually useful. Decision Trees and Random Forests are incredible at this. When they build their trees, they keep track of which columns caused the biggest drops in Gini Impurity."),
    create_code_cell([
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_classification",
        "from sklearn.ensemble import RandomForestClassifier",
        "",
        "# 1. Generate 10 features. ONLY 3 are actually useful. The other 7 are pure random noise.",
        "X, y = make_classification(n_samples=1000, n_features=10, n_informative=3, n_redundant=0, random_state=42)",
        "feature_names = [f'Feature_{i}' for i in range(10)]",
        "",
        "# 2. Train a Random Forest",
        "rf = RandomForestClassifier(random_state=42)",
        "rf.fit(X, y)",
        "",
        "# 3. Extract the Importances!",
        "importances = rf.feature_importances_",
        "",
        "# 4. Plot them",
        "plt.figure(figsize=(10, 5))",
        "plt.bar(feature_names, importances, color='teal')",
        "plt.title('Random Forest Feature Importances')",
        "plt.xticks(rotation=45)",
        "plt.ylabel('Importance Score')",
        "plt.show()"
    ]),
    create_markdown_cell("> Wow! The Random Forest mathematically sniffed out the fake data. It completely ignored 7 of the features and built almost all of its logic using `Feature_3`, `Feature_7`, and `Feature_8`."),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.feature_selection import RFE",
        "from sklearn.linear_model import LogisticRegression",
        "",
        "selector = RFE(estimator=LogisticRegression(), n_features_to_select=3)",
        "X_clean = selector.fit_transform(X, y)"
    ]),
    create_markdown_cell("> **Question:** We just passed a `LogisticRegression` model into the Recursive Feature Eliminator (RFE). RFE works by training the model, checking which features have the lowest weights (coefficients), deleting the worst feature, and training the model again. It repeats this until only 3 features are left.\n> What will the shape of `X_clean` be?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print(f'Original X shape: {X.shape}')",
        "print(f'Cleaned X shape:  {X_clean.shape}')",
        "print('\\nRFE successfully deleted the 7 useless columns of noise!')",
        "print('This will make our final model smaller, faster, and far less likely to overfit.')"
    ]),
    
    create_markdown_cell("## 10. Coding Exercise\nWe can ask RFE which features it decided to keep by looking at the boolean mask `selector.support_`.\nWrite a loop that zips `feature_names` and `selector.support_` together, and print out only the names of the features that were kept (where support is `True`)."),
    create_code_cell([
        "# YOUR CODE HERE",
        "print('Features kept by RFE:')",
        "for name, kept in zip(feature_names, selector.support_):",
        "    if kept:",
        "        print(f'- {name}')"
    ]),
    
    create_markdown_cell("## 11. Debugging Challenge\nA data analyst is trying to do Feature Selection on an SVM. They write `RFE(estimator=SVC(kernel='rbf'), n_features_to_select=5)`. It crashes with a `RuntimeError: The classifier does not expose \"coef_\" or \"feature_importances_\"`. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: RFE requires the model to be able to rank the features.')",
        "print('Linear models (like Logistic Regression or SVC with kernel=\"linear\") have `.coef_` which ranks the features by slope.')",
        "print('Tree models (like Random Forest) have `.feature_importances_`.')",
        "print('An RBF (Radial) SVM warps data into infinite dimensions. It is physically impossible to rank the importance of the original features. Therefore, RFE crashes.')"
    ]),
    create_markdown_cell("> **Rule:** You can only use `RFE` with models that expose `.coef_` or `.feature_importances_`."),
    
    create_markdown_cell("## 12. PCA vs Feature Selection\nWhat is the difference between Day 24 (PCA) and Day 28 (Feature Selection)?\n- **PCA (Dimensionality Reduction)**: Mathematically *combines* features into unreadable equations (e.g., $PC1 = 0.5 * Age + 0.5 * Income$). It changes the data.\n- **Feature Selection (RFE)**: Simply deletes the bad columns and leaves the good columns completely intact and readable. It does not change the data."),
    
    create_markdown_cell("## 13. Real-World Example\n**Financial Fraud Detection**: A bank has a dataset of 5,000 transaction properties. If they train a model on all 5,000, it overfits and memorizes the dataset, performing terribly in real life. They run `RFE` using a Random Forest to select the top 200 features. The model's accuracy immediately jumps by 15% because the algorithm is no longer being distracted by 4,800 columns of absolute noise."),
    
    create_markdown_cell("## 14. Mini Project\nBuild a Pipeline that uses `RFE` with a `DecisionTreeClassifier` to select the top 4 features, and then passes those 4 features into a `RandomForestClassifier` for final training! Evaluate it using `cross_val_score(cv=3)`. (Use the `X` and `y` from section 8)."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.model_selection import cross_val_score",
        "from sklearn.tree import DecisionTreeClassifier",
        "",
        "advanced_pipe = Pipeline([",
        "    ('feature_selection', RFE(estimator=DecisionTreeClassifier(random_state=42), n_features_to_select=4)),",
        "    ('classifier', RandomForestClassifier(random_state=42))",
        "])",
        "",
        "scores = cross_val_score(advanced_pipe, X, y, cv=3, scoring='accuracy')",
        "print(f'Pipeline Accuracy with 4 features: {scores.mean() * 100:.2f}%')"
    ]),
    
    create_markdown_cell("## 15. Common Mistakes\n- **Data Leakage during Selection**: If you use RFE on your entire dataset *before* `train_test_split` or `cross_val_score`, you have committed data leakage. The feature selector \"saw\" the test data. That's why we put it inside the Pipeline in Section 14!\n- **Over-engineering**: Creating $X^2$, $X^3$, $X^4$ for every feature usually just leads to massive overfitting. Stick to domain knowledge.\n- **Not Scaling**: If you use `LogisticRegression` for RFE, you MUST scale the data first! A feature with massive numbers (like Salary) will have a tiny coefficient (slope), and RFE will accidentally think it's useless and delete it!"),
    
    create_markdown_cell("## 16. Interview Questions\n- **Beginner**: Why is Feature Engineering often more important than choosing the algorithm? (Answer: Because if you explicitly hand the model the exact mathematical relationship it needs, even a basic linear model can solve complex problems).\n- **Intermediate**: How does a Random Forest know which features are important? (Answer: It tracks which features cause the largest decreases in Gini Impurity (or Entropy) across all the nodes in all the trees).\n- **Advanced**: Explain how Recursive Feature Elimination (RFE) works. (Answer: It trains a model, ranks the features by importance/coefficients, drops the absolute worst feature, and then retrains the model from scratch. It repeats this until the desired number of features remains)."),
    
    create_markdown_cell("## 17. Knowledge Check\n- What property stores the importance scores in a Random Forest? (`.feature_importances_`)\n- True or False: You can use RFE with an `SVC(kernel='rbf')`. (False)"),
    
    create_markdown_cell("## 18. Summary\n- **Feature Engineering** is using math to create domain-specific columns (e.g., Ratios, Ages).\n- **Feature Importances** allow us to peek into the brain of a Tree model to see what it values.\n- **RFE** recursively trains and deletes features to remove noise.\n- **RFE** does not alter the data (unlike PCA); it just drops columns.\n- You must put RFE inside a **Pipeline** to prevent data leakage during Cross Validation."),
    
    create_markdown_cell("## 19. Homework\nLoad the `load_breast_cancer` dataset (which has 30 features). \nBuild a Pipeline with `StandardScaler` and `LogisticRegression`. \nUse `RFE(estimator=LogisticRegression(), n_features_to_select=5)` as the middle step of the pipeline. \nTrain the pipeline, and print out the 5 features the Logistic Regression model decided were the most critical for detecting cancer!")
]

# Read existing notebook and update cells
filename = "Day_28_Feature_Engineering_and_Selection.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day28_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
