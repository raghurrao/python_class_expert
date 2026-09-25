import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

reviews = [
    'I loved the movie',
    'The movie was okay',
    'I hated the movie',
    'The movie was terrible and I hated it'
]

# 1. CountVectorizer
cv = CountVectorizer()
X_cv = cv.fit_transform(reviews)
assert X_cv.shape[0] == 4
assert 'movie' in cv.get_feature_names_out()

# 2. TfidfVectorizer with stop words
tfidf = TfidfVectorizer(stop_words='english')
X_tfidf = tfidf.fit_transform(reviews)
assert X_tfidf.shape[0] == 4
assert 'the' not in tfidf.get_feature_names_out()

# 3. N-grams
advanced_tfidf = TfidfVectorizer(ngram_range=(1, 2))
X_advanced = advanced_tfidf.fit_transform(['not good'])
assert 'not good' in advanced_tfidf.get_feature_names_out()
assert len(advanced_tfidf.get_feature_names_out()) == 3 # 'not', 'good', 'not good'

# 4. Pipeline execution
nlp_pipe = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words='english')),
    ('classifier', MultinomialNB())
])

labels = [1, 1, 0, 0]
nlp_pipe.fit(reviews, labels)

new_review = ['I really hated that terrible movie']
pred = nlp_pipe.predict(new_review)
assert pred[0] in [0, 1]

print("All Day 34 codes executed successfully!")
