# Day 64: Classification Metrics

In Week 8, we evaluated Regression models using MSE and R-Squared. How do we evaluate Classification models? You might think "Accuracy" is enough, but in the real world, accuracy is often a trap.

---

## 1. The Problem with Accuracy
Imagine you build a model to detect a rare disease that affects 1 in 100 people. 
If your model simply predicts "No Disease" for every single person, its **Accuracy is 99%**. But the model is completely useless! It missed every single sick person.

To get a true picture of performance, we need to look at True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN).

---

## 2. Core Metrics

### Precision
"Out of all the times the model predicted Positive, how many were *actually* positive?"
* **Formula:** $\frac{TP}{TP + FP}$
* **When to prioritize:** When False Positives are very costly. (e.g., A spam filter. You really don't want a crucial email from your boss classified as spam).

### Recall (Sensitivity)
"Out of all the *actual* Positives in the dataset, how many did the model find?"
* **Formula:** $\frac{TP}{TP + FN}$
* **When to prioritize:** When False Negatives are very costly. (e.g., Cancer detection. You'd rather have a few false alarms than miss a true cancer case).

### F1-Score
The harmonic mean of Precision and Recall. It gives you a single metric that balances both.
* **Formula:** $2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$

```python
from sklearn.metrics import precision_score, recall_score, f1_score
import numpy as np

# y_true: 1 means Sick, 0 means Healthy
y_true = np.array([0, 1, 0, 0, 1, 0, 1, 1])
y_pred = np.array([0, 1, 0, 0, 0, 1, 1, 1])

# Calculate metrics
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Precision: {precision:.2f}") # Predicted sick 4 times. 3 were correct. (3/4 = 0.75)
print(f"Recall: {recall:.2f}")       # 4 actual sick people. Found 3 of them. (3/4 = 0.75)
print(f"F1-Score: {f1:.2f}")         # Harmonic mean of 0.75 and 0.75 is 0.75
```

---

## 3. Reference Documentation
* [Scikit-Learn Classification Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
* [Precision and recall (Wikipedia)](https://en.wikipedia.org/wiki/Precision_and_recall)