import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, classification_report, accuracy_score

# Generate Data
np.random.seed(42)
X = np.random.rand(100, 2)
y = np.zeros(100)
y[:10] = 1 
np.random.shuffle(y)
X[y == 1] += 0.5 

model = LogisticRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Test that precision, recall, f1 work
acc = accuracy_score(y, y_pred)
prec = precision_score(y, y_pred)
rec = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)
assert acc > 0.0
assert prec >= 0.0
assert rec >= 0.0
assert f1 >= 0.0

# Confusion Matrix
cm = confusion_matrix(y, y_pred)
assert cm.shape == (2, 2)

# Dumb model prediction
y_true_mock = [1, 1, 1, 0, 0]
y_pred_dumb = [0, 0, 0, 0, 0]
assert recall_score(y_true_mock, y_pred_dumb, zero_division=0) == 0.0
assert precision_score(y_true_mock, y_pred_dumb, zero_division=0) == 0.0

# Report
report = classification_report(y, y_pred)
assert 'precision' in report
assert 'recall' in report

# Extreme Recall Test
probs = model.predict_proba(X)[:, 1]
extreme_recall_preds = (probs > 0.0001).astype(int)
assert recall_score(y, extreme_recall_preds) == 1.0
assert precision_score(y, extreme_recall_preds) < 0.5

# Threshold loop
thresholds = [0.2, 0.5, 0.8]
f1_scores = []
for t in thresholds:
    custom_p = (probs > t).astype(int)
    f1_scores.append(f1_score(y, custom_p))
assert len(f1_scores) == 3

print("All Day 16 codes executed successfully!")
