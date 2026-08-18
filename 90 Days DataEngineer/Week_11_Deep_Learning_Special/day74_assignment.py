from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def extract_tfidf_features(documents: list) -> tuple:
    """
    Fit a TfidfVectorizer on documents list, transform,
    and return (vectorized_sparse_matrix, tfidf_model).
    """
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(documents)
    return matrix, vectorizer