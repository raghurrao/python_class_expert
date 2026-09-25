import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import joblib
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Generate Data
np.random.seed(42)
ages = np.random.randint(30, 80, 1000)
blood_pressure = np.random.randint(90, 180, 1000)
cholesterol = np.random.randint(150, 350, 1000)
genders = np.random.choice(['Male', 'Female'], 1000)
chest_pain = np.random.choice(['Typical', 'Atypical', 'Non-anginal', 'Asymptomatic'], 1000)
risk_score = (ages / 80) + (blood_pressure / 180) + (genders == 'Male').astype(int) * 0.5
y = (risk_score + np.random.normal(0, 0.5, 1000) > 1.8).astype(int)

df = pd.DataFrame({
    'Age': ages,
    'Blood_Pressure': blood_pressure,
    'Cholesterol': cholesterol,
    'Gender': genders,
    'Chest_Pain': chest_pain,
    'Heart_Disease': y
})

# 2. Split
X = df.drop('Heart_Disease', axis=1)
y = df['Heart_Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Preprocessor
numeric_features = ['Age', 'Blood_Pressure', 'Cholesterol']
categorical_features = ['Gender', 'Chest_Pain']
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first'), categorical_features)
])

# 4. Pipeline
master_pipe = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# 5. GridSearchCV (we'll make the grid small for the test script to run fast)
param_grid = {
    'classifier__n_estimators': [10, 50],
    'classifier__max_depth': [None, 5]
}
grid_search = GridSearchCV(
    estimator=master_pipe, 
    param_grid=param_grid, 
    cv=3, 
    scoring='accuracy', 
    n_jobs=-1
)
grid_search.fit(X_train, y_train)
assert grid_search.best_score_ > 0.5

# 6. Evaluation
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
assert len(y_pred) == 200

# 7. Production Save
file_name = 'heart_disease_v1.joblib'
joblib.dump(best_model, file_name)
assert os.path.exists(file_name)

# 8. Production Inference
server_model = joblib.load(file_name)
new_patient = pd.DataFrame({
    'Age': [65],
    'Blood_Pressure': [160],
    'Cholesterol': [250],
    'Gender': ['Male'],
    'Chest_Pain': ['Typical']
})
prediction = server_model.predict(new_patient)
assert prediction[0] in [0, 1]

# 9. Cleanup
os.remove(file_name)

print("All Day 30 codes executed successfully!")
