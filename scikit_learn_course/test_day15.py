import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X_hours = np.sort(10 * np.random.rand(30, 1), axis=0)
y_pass = (X_hours > 5).astype(int).ravel()
y_pass[13:17] = [1, 0, 1, 0]

lin_reg = LinearRegression()
lin_reg.fit(X_hours, y_pass)

log_reg = LogisticRegression()
log_reg.fit(X_hours, y_pass)

# Test Linear Regression produces invalid probabilities
assert np.max(lin_reg.predict(X_hours)) > 1.0 or np.min(lin_reg.predict(X_hours)) < 0.0

# Test Logistic Regression probabilities are bounded [0, 1]
probs = log_reg.predict_proba(X_hours)[:, 1]
assert np.max(probs) <= 1.0 and np.min(probs) >= 0.0

student_hours = np.array([[4.5], [6.5]])
preds = log_reg.predict(student_hours)
assert len(preds) == 2

# Custom threshold test
custom_threshold = 0.90
probs_class_1 = log_reg.predict_proba(student_hours)[:, 1]
custom_preds = (probs_class_1 >= custom_threshold).astype(int)
assert len(custom_preds) == 2

# Test Pipeline accuracy
log_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42))
])
log_pipe.fit(X_hours, y_pass)
accuracy = log_pipe.score(X_hours, y_pass)
assert 0.0 <= accuracy <= 1.0

print("All Day 15 codes executed successfully!")
