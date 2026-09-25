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

day7_cells = [
    create_markdown_cell("# PHASE 1 — MACHINE LEARNING FOUNDATIONS"),
    create_markdown_cell("# Day 07 — Weekly Project: Customer Churn Prediction"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this project, you will be able to:\n- Integrate everything learned in Phase 1 (Splitting, Imputation, Scaling, Encoding, Pipelines).\n- Establish a **Baseline Model** to serve as a minimum performance benchmark.\n- Understand the concept of \"Customer Churn\" and why predicting it is a common real-world ML task."),
    
    create_markdown_cell("## 2. Prerequisites\n- Days 1 to 6 (The complete Scikit-learn foundational workflow)."),
    
    create_markdown_cell("## 3. Concept: The Baseline Model\nA **Baseline** is the simplest possible model you can build. It could be predicting the majority class (e.g., predicting that *no one* churns), or it could be a basic Logistic Regression model with default parameters.\n\nWhy build a baseline? Because if you spend 3 weeks building a complex Deep Neural Network that achieves 85% accuracy, but a 5-minute Logistic Regression baseline achieves 84% accuracy... your complex model is practically useless."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nMachine Learning is an iterative process. You never start by training the most complex model. \n1. Build a robust pipeline.\n2. Establish a simple baseline.\n3. Iterate and improve.\n4. Ensure every complex addition actually provides a measurable return on investment (ROI) over the baseline."),
    
    create_markdown_cell("## 5. Intuition\n**Customer Churn**: A customer stops doing business with a company. \nIf a Telecom company can predict *who* is going to cancel their subscription next month, they can proactively call them and offer a discount to stay. \nOur job today is to predict `Churn` (1 = Yes, 0 = No) based on customer profile data."),
    
    create_markdown_cell("## 6. Mathematical Foundation (Dummy Classifiers)\nBefore we build a Machine Learning model, let's consider a Zero-Intelligence model. Let the dataset have $N$ samples, where $N_0$ is the number of retained customers and $N_1$ is the number of churned customers. \nIf $N_0 > N_1$, a 'Most Frequent' dummy classifier will simply predict $0$ for every sample. \n\nIts accuracy will exactly equal: $\\frac{N_0}{N_0 + N_1}$. If 80% of customers don't churn, predicting 'No' for everyone gives 80% accuracy! This is why accuracy can be misleading (a topic we will deep dive into in Phase 3)."),
    
    create_markdown_cell("## 7. The Project Setup\nWe will generate a synthetic but highly realistic Telecom Churn dataset. It will contain numerical data (Tenure, MonthlyCharges) and categorical data (InternetService, ContractType)."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "",
        "# Generate synthetic Churn Data",
        "np.random.seed(42)",
        "n_samples = 2000",
        "",
        "data = {",
        "    'Tenure_Months': np.random.randint(1, 72, n_samples),",
        "    'Monthly_Charges': np.random.uniform(20.0, 120.0, n_samples),",
        "    'Total_Charges': np.random.uniform(20.0, 8000.0, n_samples),",
        "    'Internet_Service': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples, p=[0.3, 0.5, 0.2]),",
        "    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples, p=[0.5, 0.3, 0.2]),",
        "    'Payment_Method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer'], n_samples)",
        "}",
        "df = pd.DataFrame(data)",
        "",
        "# Introduce missing values realistically",
        "df.loc[np.random.choice(df.index, 50, replace=False), 'Total_Charges'] = np.nan",
        "",
        "# Create the target variable 'Churn' based on rules + noise",
        "# Higher probability of churn if month-to-month and high charges",
        "churn_prob = np.where(df['Contract'] == 'Month-to-month', 0.4, 0.05)",
        "churn_prob += np.where(df['Monthly_Charges'] > 80, 0.2, 0.0)",
        "churn_prob -= np.where(df['Tenure_Months'] > 40, 0.15, 0.0)",
        "churn_prob = np.clip(churn_prob, 0.05, 0.85) # Keep probs realistic",
        "",
        "df['Churn'] = np.random.binomial(1, churn_prob)",
        "",
        "print(df.head())",
        "print('\\nMissing values:\\n', df.isna().sum())",
        "print('\\nChurn Distribution:\\n', df['Churn'].value_counts(normalize=True))"
    ]),
    
    create_markdown_cell("## 8. Identifying Features and Target\nFirst, we separate `X` and `y`."),
    create_code_cell([
        "X = df.drop('Churn', axis=1)",
        "y = df['Churn']"
    ]),
    
    create_markdown_cell("## 9. Train / Test Split\nWe split the data. Notice we use `stratify=y` because the target is imbalanced (~67% No, ~33% Yes)."),
    create_code_cell([
        "from sklearn.model_selection import train_test_split",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)",
        "print(f'Training shape: {X_train.shape}, Test shape: {X_test.shape}')"
    ]),
    
    create_markdown_cell("## 10. Building the Preprocessing Pipeline\nNow, identify which columns are numeric and which are categorical, and build the `ColumnTransformer`."),
    create_code_cell([
        "from sklearn.compose import ColumnTransformer",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.impute import SimpleImputer",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder",
        "",
        "numeric_features = ['Tenure_Months', 'Monthly_Charges', 'Total_Charges']",
        "categorical_features = ['Internet_Service', 'Contract', 'Payment_Method']",
        "",
        "num_pipeline = Pipeline([",
        "    ('imputer', SimpleImputer(strategy='median')),",
        "    ('scaler', StandardScaler())",
        "])",
        "",
        "cat_pipeline = Pipeline([",
        "    ('imputer', SimpleImputer(strategy='most_frequent')),",
        "    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))",
        "])",
        "",
        "preprocessor = ColumnTransformer([",
        "    ('num', num_pipeline, numeric_features),",
        "    ('cat', cat_pipeline, categorical_features)",
        "])"
    ]),
    
    create_markdown_cell("## 11. Zero-Intelligence Baseline (Dummy Classifier)\nBefore running Logistic Regression, what happens if we just predict the majority class (No Churn) for everyone?"),
    create_code_cell([
        "from sklearn.dummy import DummyClassifier",
        "",
        "dummy_clf = DummyClassifier(strategy='most_frequent')",
        "dummy_clf.fit(X_train, y_train)",
        "dummy_acc = dummy_clf.score(X_test, y_test)",
        "",
        "print(f'Dummy Classifier (Always predicts No Churn) Accuracy: {dummy_acc * 100:.2f}%')"
    ]),
    create_markdown_cell("> This means any machine learning model we build MUST score higher than this, otherwise it is useless!"),
    
    create_markdown_cell("## 12. Training the Baseline ML Model\nLet's hook up our `preprocessor` to a `LogisticRegression` model."),
    create_code_cell([
        "from sklearn.linear_model import LogisticRegression",
        "",
        "ml_pipeline = Pipeline([",
        "    ('preprocessor', preprocessor),",
        "    ('model', LogisticRegression(random_state=42))",
        "])",
        "",
        "ml_pipeline.fit(X_train, y_train)",
        "ml_acc = ml_pipeline.score(X_test, y_test)",
        "print(f'Logistic Regression Baseline Accuracy: {ml_acc * 100:.2f}%')"
    ]),
    create_markdown_cell("> We successfully beat the Dummy Classifier! The ML model is actually learning patterns."),
    
    create_markdown_cell("## 13. Explaining Results (Error Analysis)\nLet's see what the model is predicting compared to reality."),
    create_code_cell([
        "import matplotlib.pyplot as plt",
        "from sklearn.metrics import ConfusionMatrixDisplay",
        "",
        "# We will cover this deeply in Phase 3, but let's take a sneak peek",
        "ConfusionMatrixDisplay.from_estimator(ml_pipeline, X_test, y_test, cmap='Blues')",
        "plt.title('Confusion Matrix (Baseline)')",
        "plt.show()"
    ]),
    create_markdown_cell("> The matrix shows:\n- True Positives (Churned and predicted Churn)\n- True Negatives (Stayed and predicted Stayed)\n- False Positives (Stayed but predicted Churn)\n- False Negatives (Churned but predicted Stayed)"),
    
    create_markdown_cell("## 14. Phase 1 Evaluation\nYou have just completed an end-to-end Machine Learning pipeline. You:\n1. Understood the problem (Churn).\n2. Splitted the data safely.\n3. Handled missing data.\n4. Handled categorical strings.\n5. Scaled numbers.\n6. Prevented data leakage using Pipelines.\n7. Established a Dummy baseline.\n8. Beat the baseline with a linear model."),
    
    create_markdown_cell("## 15. Real-World Application\nIn the real world, the data engineering team would schedule this pipeline to run every night on active customers. Anyone predicted as '1' (Churn) would be automatically emailed a 20% discount coupon the next morning."),
    
    create_markdown_cell("## 16. Capstone Exercise for Phase 1\nYour turn! The HR department wants to predict Employee Attrition (whether an employee will quit). \nThey gave you this dataframe. Build the full pipeline and baseline model."),
    create_code_cell([
        "# YOUR CODE HERE",
        "hr_df = pd.DataFrame({",
        "    'Age': [28, 45, 32, 50, 25, 40],",
        "    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'IT'],",
        "    'Distance_From_Home': [2.5, 15.0, np.nan, 5.0, 25.0, 1.0],",
        "    'Quits': [1, 0, 1, 0, 1, 0]",
        "})",
        "",
        "# Write your complete pipeline to predict 'Quits' below:",
        "X_hr = hr_df.drop('Quits', axis=1)",
        "y_hr = hr_df['Quits']",
        "",
        "hr_num = ['Age', 'Distance_From_Home']",
        "hr_cat = ['Department']",
        "",
        "hr_pre = ColumnTransformer([",
        "    ('n', Pipeline([('imp', SimpleImputer(strategy='mean')), ('scl', StandardScaler())]), hr_num),",
        "    ('c', OneHotEncoder(), hr_cat)",
        "])",
        "",
        "hr_pipe = Pipeline([('pre', hr_pre), ('clf', LogisticRegression())])",
        "hr_pipe.fit(X_hr, y_hr)",
        "print('HR Model Trained successfully on tiny dataset. Score:', hr_pipe.score(X_hr, y_hr))"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes (Phase 1 Review)\n- Memorize this: **NEVER fit your Scaler or Imputer on the Test Set!** Use Pipelines to guarantee you don't mess this up.\n- Never assume a 90% accuracy is good without checking the target distribution. If 99% of people don't click an ad, a model that predicts \"No Click\" for everyone is 99% accurate but completely useless."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What are the components of a Scikit-learn Pipeline?\n- **Intermediate**: Why is a Dummy Classifier important?\n- **Advanced**: In our churn pipeline, what would happen if we used `SimpleImputer` *after* the `StandardScaler`?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- What estimator always predicts the most frequent class? (`DummyClassifier`)"),
    
    create_markdown_cell("## 20. Summary of Phase 1\nYou now know the structural mechanics of Scikit-learn. In **Phase 2**, we will move beyond Logistic Regression and dive deep into the mathematics and algorithms behind powerful ML models (Decision Trees, Random Forests, Gradient Boosting) for Regression problems!"),
    
    create_markdown_cell("## 21. Homework / Phase 1 Assessment\nTake a break! Review the concepts from Days 1-7. Tomorrow we begin Regression modeling.")
]

# Read existing notebook and update cells
filename = "Day_07_Weekly_Project_Customer_Churn_Prediction.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day7_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
