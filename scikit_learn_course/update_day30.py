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

day30_cells = [
    create_markdown_cell("# THE FINAL PROJECT"),
    create_markdown_cell("# Day 30 — ML Capstone"),
    
    create_markdown_cell("## 1. Congratulations!\nYou have reached the end of the 30-Day Scikit-Learn course! \nOver the last month, you have transitioned from a beginner looking at raw spreadsheets to an ML Engineer capable of building, evaluating, tuning, and deploying production-grade Machine Learning pipelines.\n\nToday, you will build a complete end-to-end classification system, starting from raw data and ending with a saved `.joblib` file ready for a web server."),
    
    create_markdown_cell("## 2. The Business Problem\nA hospital wants a Machine Learning model to predict if a patient has heart disease based on their medical chart. \nThe data is messy. It contains both numbers (Age, Blood Pressure) and text categories (Gender, Chest Pain Type). \nYour goal is to build an absolute state-of-the-art Pipeline, tune its hyperparameters rigorously using Cross-Validation, and deliver a mathematically proven model."),
    
    create_markdown_cell("## 3. Step 1: The Raw Data\nFirst, we will generate a realistic, messy dataset representing 1,000 patients."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "",
        "np.random.seed(42)",
        "",
        "# 1. Generate numeric features",
        "ages = np.random.randint(30, 80, 1000)",
        "blood_pressure = np.random.randint(90, 180, 1000)",
        "cholesterol = np.random.randint(150, 350, 1000)",
        "",
        "# 2. Generate categorical features",
        "genders = np.random.choice(['Male', 'Female'], 1000)",
        "chest_pain = np.random.choice(['Typical', 'Atypical', 'Non-anginal', 'Asymptomatic'], 1000)",
        "",
        "# 3. Generate the Target (Heart Disease: 0 or 1)",
        "# We'll mathematically bias it so that older males with high BP are more likely to have disease",
        "risk_score = (ages / 80) + (blood_pressure / 180) + (genders == 'Male').astype(int) * 0.5",
        "y = (risk_score + np.random.normal(0, 0.5, 1000) > 1.8).astype(int)",
        "",
        "df = pd.DataFrame({",
        "    'Age': ages,",
        "    'Blood_Pressure': blood_pressure,",
        "    'Cholesterol': cholesterol,",
        "    'Gender': genders,",
        "    'Chest_Pain': chest_pain,",
        "    'Heart_Disease': y",
        "})",
        "",
        "print('Raw Data Shape:', df.shape)",
        "print(df.head())"
    ]),
    
    create_markdown_cell("## 4. Step 2: Train / Test Split\nThe absolute first rule of Machine Learning: Never look at the Test Data! Split it immediately."),
    create_code_cell([
        "from sklearn.model_selection import train_test_split",
        "",
        "X = df.drop('Heart_Disease', axis=1)",
        "y = df['Heart_Disease']",
        "",
        "# Reserve 20% of the data for the final FDA-style evaluation",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "",
        "print(f'Training Rows: {len(X_train)}')",
        "print(f'Testing Rows:  {len(X_test)}')"
    ]),
    
    create_markdown_cell("## 5. Step 3: ColumnTransformer\nMachine learning models only understand numbers. \nWe need to build a `ColumnTransformer` that:\n- Scales the numeric columns (`Age`, `Blood_Pressure`, `Cholesterol`) so distances are calculated fairly.\n- One-Hot Encodes the categorical columns (`Gender`, `Chest_Pain`) into binary 1s and 0s."),
    create_code_cell([
        "from sklearn.compose import ColumnTransformer",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder",
        "",
        "numeric_features = ['Age', 'Blood_Pressure', 'Cholesterol']",
        "categorical_features = ['Gender', 'Chest_Pain']",
        "",
        "# Build the Master Preprocessor",
        "preprocessor = ColumnTransformer([",
        "    ('num', StandardScaler(), numeric_features),",
        "    ('cat', OneHotEncoder(drop='first'), categorical_features)",
        "])",
        "",
        "print('Preprocessor constructed successfully!')"
    ]),
    
    create_markdown_cell("## 6. Step 4: The Pipeline\nNow we will attach the `preprocessor` to a `RandomForestClassifier`. This ensures that raw text data can flow directly into the model without crashing."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.ensemble import RandomForestClassifier",
        "",
        "master_pipe = Pipeline([",
        "    ('preprocessor', preprocessor),",
        "    ('classifier', RandomForestClassifier(random_state=42))",
        "])",
        "",
        "print('Master Pipeline constructed successfully!')"
    ]),
    
    create_markdown_cell("## 7. Step 5: Hyperparameter Tuning (GridSearchCV)\nInstead of guessing how deep the Random Forest trees should be, we will define a dictionary of hyperparameters and let `GridSearchCV` rigorously test all of them using 5-Fold Cross Validation. \n\n*Remember the double underscores `classifier__`!*"),
    create_code_cell([
        "from sklearn.model_selection import GridSearchCV",
        "",
        "# Define the grid",
        "param_grid = {",
        "    'classifier__n_estimators': [50, 100, 200],",
        "    'classifier__max_depth': [None, 5, 10],",
        "    'classifier__min_samples_split': [2, 10]",
        "}",
        "",
        "# 3 * 3 * 2 = 18 combinations. * 5 Folds = 90 models trained!",
        "grid_search = GridSearchCV(",
        "    estimator=master_pipe, ",
        "    param_grid=param_grid, ",
        "    cv=5, ",
        "    scoring='accuracy', ",
        "    n_jobs=-1",
        ")",
        "",
        "print('Running Grid Search (training 90 models)...')",
        "grid_search.fit(X_train, y_train)",
        "",
        "print('\\nBest Hyperparameters Found:')",
        "print(grid_search.best_params_)"
    ]),
    
    create_markdown_cell("## 8. Step 6: Final Evaluation\nWe now extract the absolute best model from the Grid Search. \nFor the very first time, we will let it look at the `X_test` data we hid in Step 2. We will generate the final Classification Report and Confusion Matrix to present to the hospital."),
    create_code_cell([
        "import matplotlib.pyplot as plt",
        "from sklearn.metrics import classification_report, ConfusionMatrixDisplay",
        "",
        "# 1. Extract the proven champion model",
        "best_model = grid_search.best_estimator_",
        "",
        "# 2. Make predictions on the hidden test set",
        "y_pred = best_model.predict(X_test)",
        "",
        "print('============= FINAL REPORT =============')",
        "print(classification_report(y_test, y_pred))",
        "",
        "# 3. Plot Confusion Matrix",
        "ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=['Healthy', 'Disease'], cmap='Blues')",
        "plt.title('Final Confusion Matrix')",
        "plt.show()"
    ]),
    
    create_markdown_cell("## 9. Step 7: Production (Joblib)\nThe hospital approves the model! Now we must save the entire Pipeline to a file so their web server can load it and make predictions on new patients."),
    create_code_cell([
        "import joblib",
        "import os",
        "",
        "# Save the model to the hard drive",
        "file_name = 'heart_disease_v1.joblib'",
        "joblib.dump(best_model, file_name)",
        "",
        "print(f'Model saved successfully as {file_name}!')",
        "print(f'File Size: {os.path.getsize(file_name) / 1024:.1f} KB')"
    ]),
    
    create_markdown_cell("## 10. Step 8: Simulated Inference\nLet's prove it works. We will simulate the hospital's Web Server. We will load the file, create a raw Pandas DataFrame representing a new patient (with text data!), and get an instant prediction."),
    create_code_cell([
        "# The Web Server Code",
        "server_model = joblib.load('heart_disease_v1.joblib')",
        "",
        "# A new patient walks into the hospital",
        "new_patient = pd.DataFrame({",
        "    'Age': [65],",
        "    'Blood_Pressure': [160],",
        "    'Cholesterol': [250],",
        "    'Gender': ['Male'],",
        "    'Chest_Pain': ['Typical']",
        "})",
        "",
        "prediction = server_model.predict(new_patient)",
        "probability = server_model.predict_proba(new_patient)[0][1]",
        "",
        "print('--- SERVER INFERENCE ---')",
        "if prediction[0] == 1:",
        "    print(f'ALERT: Patient flagged for Heart Disease! (Confidence: {probability * 100:.1f}%)')",
        "else:",
        "    print(f'Patient cleared. No Heart Disease detected. (Confidence: {(1 - probability) * 100:.1f}%)')"
    ]),
    
    create_markdown_cell("## 11. Final Thoughts\nYou have done it. \nYou generated raw data, split it, scaled the math, encoded the text, piped it into a Random Forest, cross-validated 18 different hyperparameter configurations simultaneously, evaluated the absolute best model, analyzed its confusion matrix, mathematically serialized the pipeline to the hard drive, simulated a web server, loaded the byte-stream, and ran raw text inference in under a second.\n\n**You are now a Machine Learning Engineer.** \n\nThank you for taking this 30-Day journey!")
]

# Read existing notebook and update cells
filename = "Day_30_ML_Capstone.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day30_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
