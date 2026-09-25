import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
dt_model = DecisionTreeClassifier(random_state=1)

# 1. train_test_split variance
accs = []
for seed in [10, 42, 99, 123, 777]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    dt_model.fit(X_train, y_train)
    accs.append(accuracy_score(y_test, dt_model.predict(X_test)))
assert max(accs) - min(accs) > 0.10 # Verify high variance due to luck of draw

# 2. cross_val_score (Decision Tree vs Random Forest)
dt_scores = cross_val_score(dt_model, X, y, cv=5, scoring='accuracy')
assert len(dt_scores) == 5

rf_model = RandomForestClassifier(n_estimators=100, random_state=1)
rf_scores = cross_val_score(rf_model, X, y, cv=5, scoring='accuracy')

assert rf_scores.mean() > dt_scores.mean()
assert rf_scores.std() < dt_scores.std()

# 3. 10-fold CV
rf_10_scores = cross_val_score(rf_model, X, y, cv=10, scoring='accuracy')
assert len(rf_10_scores) == 10

# 4. Leak-Free Pipeline CV
svm_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', random_state=42))
])
safe_cv_scores = cross_val_score(svm_pipe, X, y, cv=5, scoring='accuracy')
assert len(safe_cv_scores) == 5
assert safe_cv_scores.mean() > 0.5

print("All Day 26 codes executed successfully!")
