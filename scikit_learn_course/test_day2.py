from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Load Data
data = load_breast_cancer()
X, y = data.data, data.target

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize Estimator/Predictor
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 4. Fit (Learn)
model.fit(X_train, y_train)

# 5. Predict
y_pred = model.predict(X_test)

# 6. Evaluate
accuracy = model.score(X_test, y_test)
print(f'Test Accuracy: {accuracy * 100:.2f}%')

X_train_half, X_test_half, y_train_half, y_test_half = train_test_split(X, y, test_size=0.5, random_state=42)
model.fit(X_train_half, y_train_half)
print(f'Test Accuracy (50% split): {model.score(X_test_half, y_test_half) * 100:.2f}%')

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("StandardScaler passed!")

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
X_reg, y_reg = make_regression(n_samples=500, n_features=3, noise=10, random_state=42)
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
reg_model = LinearRegression()
reg_model.fit(X_train_r, y_train_r)
print(f'Regression R^2 Score: {reg_model.score(X_test_r, y_test_r):.4f}')

from sklearn.datasets import make_classification
X_bug, y_bug = make_classification(n_samples=100, random_state=42)
model_bug = RandomForestClassifier()
try:
    predictions_bug = model_bug.predict(X_bug)
except Exception as e:
    print("Caught expected bug:", type(e).__name__)

def train_and_evaluate(model, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    return model.score(X_test, y_test)

from sklearn.tree import DecisionTreeClassifier
score = train_and_evaluate(DecisionTreeClassifier(random_state=42), X, y)
print(f'Decision Tree Score: {score:.4f}')

print("All Day 2 codes executed successfully!")
