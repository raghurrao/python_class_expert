import pandas as pd
import joblib
import os
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# 1. Generate and Train
X_train, y_train = make_classification(n_samples=1000, n_features=5, random_state=42)

production_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(n_estimators=50, random_state=42))
])
production_pipe.fit(X_train, y_train)

# 2. Save
filename = 'spam_detector_v1.joblib'
joblib.dump(production_pipe, filename)
assert os.path.exists(filename)
assert os.path.getsize(filename) > 100 # Should be at least a few KB

# 3. Load and Predict
server_model = joblib.load(filename)
user_input = pd.DataFrame([[0.5, -1.2, 3.4, 0.1, -0.9]])

prediction = server_model.predict(user_input)
assert prediction[0] in [0, 1]

# 4. Check internal scaler state
saved_means = server_model.named_steps['scaler'].mean_
assert len(saved_means) == 5

# 5. Clean up
os.remove(filename)
assert not os.path.exists(filename)

print("All Day 29 codes executed successfully!")
