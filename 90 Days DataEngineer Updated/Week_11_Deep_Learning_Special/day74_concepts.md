# Day 74: Natural Language Processing (TF-IDF)

Machine learning models cannot read text. They only understand numbers. If we want to build a spam classifier or analyze sentiment, we must first convert our text into numerical vectors. 

---

## 1. What is TF-IDF?
One simple way to convert text to numbers is a "Count Vectorizer" (just count how many times each word appears in the document). But this gives too much weight to common words like "the", "is", and "and".

**TF-IDF (Term Frequency - Inverse Document Frequency)** solves this.
* **Term Frequency (TF):** How often does the word appear in *this specific* document? (More is better).
* **Inverse Document Frequency (IDF):** How rare is the word across *all* documents in the dataset? (Rarer is better).

TF-IDF multiplies these together. A word gets a high score if it appears frequently in a document, but rarely in the rest of the corpus. This highlights the *unique, important* words in a specific text.

---

## 2. Core Concepts & Operations

### Using TF-IDF in Scikit-Learn

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample corpus (3 short documents)
documents = [
    "Machine learning is great.",
    "Natural language processing is a part of machine learning.",
    "I love learning about artificial intelligence."
]

# Initialize the vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# The result is a "Sparse Matrix" (because most documents don't contain most words, 
# it saves memory by only storing the non-zero values).
print("TF-IDF Matrix Shape:", tfidf_matrix.shape)
# Output will be (3, N) where N is the total number of unique words across all documents.

# Let's see the actual vocabulary learned
print("\nVocabulary Mapping (Word -> Column Index):")
print(vectorizer.vocabulary_)

# Look at the TF-IDF scores for the first document
# We convert the first row of the sparse matrix to a dense array to view it
print("\nTF-IDF scores for Document 1:")
print(tfidf_matrix.toarray()[0])
```

Once you have this `tfidf_matrix`, you can feed it directly into a `LogisticRegression` or `RandomForest` model to predict categories!

---

## 3. Reference Documentation
* [Scikit-Learn TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
* [Tf-idf (Wikipedia)](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
