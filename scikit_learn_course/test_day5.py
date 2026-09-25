import numpy as np
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1. Create messy data
X = np.array([[25.0], [np.nan], [30.0], [45.0], [50.0], [np.nan], [22.0], [60.0]])
y = np.array([0, 1, 0, 1, 1, 0, 0, 1])

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Build the Pipeline
pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

# 4. Fit the ENTIRE pipeline at once
pipe.fit(X_train, y_train)
predictions = pipe.predict(X_test)
assert len(predictions) == len(y_test)

# Experiment
learned_mean = pipe.named_steps['imputer'].statistics_
learned_coef = pipe.named_steps['classifier'].coef_
assert learned_mean is not None and learned_coef is not None

# make_pipeline test
pipe2 = make_pipeline(
    SimpleImputer(strategy='median'),
    StandardScaler(),
    LogisticRegression()
)
assert 'standardscaler' in pipe2.named_steps.keys()

# Coding exercise
my_pipe = make_pipeline(
    SimpleImputer(strategy='constant', fill_value=-1),
    MinMaxScaler(),
    DecisionTreeClassifier(random_state=42)
)
my_pipe.fit(X_train, y_train)
score = my_pipe.score(X_test, y_test)
assert score >= 0.0

# Debugging challenge
try:
    bad_pipe = Pipeline([
        ('model', LogisticRegression()),
        ('scaler', StandardScaler())
    ])
    bad_pipe.fit(X_train, y_train) # This should crash
    print("Buggy code executed without breaking, but it should have crashed!")
except TypeError:
    print('Caught expected bug: TypeError (Estimator must be last)')
except Exception as e:
    print('Caught expected bug:', type(e).__name__)

# Mini project
new_user_data = np.array([[np.nan]])
prediction = pipe.predict(new_user_data)
assert prediction.shape == (1,)

print("All Day 5 codes executed successfully!")
