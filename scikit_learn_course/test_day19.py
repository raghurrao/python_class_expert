import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.pipeline import Pipeline

# 1. Text Classification (MultinomialNB)
emails = [
    'hey mom call me later',
    'meeting at 3pm tomorrow',
    'win a free rolex watch now',
    'get cheap viagra pills free',
    'lunch is ready',
    'click here for free money'
]
y = np.array([0, 0, 1, 1, 0, 1])

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

nb_model = MultinomialNB()
nb_model.fit(X, y)
assert accuracy_score(y, nb_model.predict(X)) >= 0.8

new_email = ['mom wants to win a free rolex']
new_X = vectorizer.transform(new_email)
prediction = nb_model.predict(new_X)
probability = nb_model.predict_proba(new_X)
assert prediction[0] in [0, 1]

# 2. Continuous Data (GaussianNB vs MultinomialNB crash)
X_continuous, y_cont = make_classification(n_samples=100, n_features=4, random_state=42)

try:
    bad_nb = MultinomialNB()
    bad_nb.fit(X_continuous, y_cont)
    # Depending on make_classification, it might not crash if all are > 0.
    # But standard scaling/make_classification usually creates negatives.
    # Let's force a negative to be absolutely sure the test validates the concept.
    X_continuous[0,0] = -1.0
    bad_nb.fit(X_continuous, y_cont)
    assert False, "MultinomialNB should crash on negative continuous data"
except ValueError:
    pass

gauss_nb = GaussianNB()
gauss_nb.fit(X_continuous, y_cont)
assert accuracy_score(y_cont, gauss_nb.predict(X_continuous)) > 0.0

# 3. Pipeline Fix
nlp_pipe = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

nlp_pipe.fit(emails, y)
safe_prediction = nlp_pipe.predict(new_email)
assert safe_prediction[0] in [0, 1]

print("All Day 19 codes executed successfully!")
