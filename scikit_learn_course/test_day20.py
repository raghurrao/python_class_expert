import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, f1_score, confusion_matrix

np.random.seed(42)
X_mock, y_mock = make_classification(
    n_samples=5000, n_features=3, n_informative=3, n_redundant=0, 
    weights=[0.95, 0.05], class_sep=0.8, random_state=42
)
columns = ['Transaction_Amount', 'Distance_From_Home', 'Time_of_Day']
df = pd.DataFrame(X_mock, columns=columns)
df['Is_Fraud'] = y_mock

X = df.drop('Is_Fraud', axis=1)
y = df['Is_Fraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()

models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'KNN (K=5)': KNeighborsClassifier(n_neighbors=5),
    'SVM (RBF)': SVC(kernel='rbf', probability=True, random_state=42) 
}

trained_pipelines = {}
for name, model in models.items():
    pipe = Pipeline([
        ('scaler', scaler),
        ('classifier', model)
    ])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    trained_pipelines[name] = pipe

# Assert SVM RBF trained correctly and has a non-zero F1 score
svm_preds = trained_pipelines['SVM (RBF)'].predict(X_test)
assert f1_score(y_test, svm_preds) > 0.0

best_model = trained_pipelines['SVM (RBF)']
fraud_probs = best_model.predict_proba(X_test)[:, 1]
aggressive_preds = (fraud_probs >= 0.10).astype(int)

# Assert that dropping the threshold to 0.1 increases the number of positive predictions (higher recall, lower precision)
assert np.sum(aggressive_preds) > np.sum(svm_preds)

# Capstone Exercise
nb_pipe = Pipeline([
    ('scaler', scaler),
    ('nb', GaussianNB())
])
nb_pipe.fit(X_train, y_train)
nb_preds = nb_pipe.predict(X_test)
assert f1_score(y_test, nb_preds) > 0.0

print("All Day 20 codes executed successfully!")
