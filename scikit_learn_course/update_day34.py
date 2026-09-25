import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

def create_code_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

day34_cells = [
    create_markdown_cell("# BONUS CONTENT"),
    create_markdown_cell("# Day 34 — Natural Language Processing (NLP)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Understand how to convert unstructured text (like Tweets or Reviews) into a mathematical matrix.\n- Use `CountVectorizer` to build a Bag-of-Words.\n- Use `TfidfVectorizer` to mathematically heavily weight rare, important words and down-weight common fluff words.\n- Implement Stop Words and N-Grams."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 20 (Naive Bayes - often used with text).\n- Day 5 (Pipelines)."),
    
    create_markdown_cell("## 3. Concept: The Text Problem\nMachine Learning models can only do math. If you give a model the sentence `\"This movie was terrible\"`, it has no idea what to do. \nWe need a way to transform sentences into a matrix of numbers. This is called **Vectorization**."),
    
    create_markdown_cell("## 4. Concept: Bag of Words (CountVectorizer)\nThe simplest approach is the **Bag of Words**. \nImagine reading 10,000 movie reviews and making a giant list of every unique word used across all reviews (the Vocabulary). \nFor each review, you simply create an array of 0s, and place a 1 (or a 2, 3) in the column for every word that appears in that review. \n\n*Drawback*: A sentence like `\"The movie was great\"` will put equal mathematical weight on the word `\"The\"` and the word `\"great\"`. That is bad."),
    
    create_markdown_cell("## 5. Concept: TF-IDF\n**Term Frequency - Inverse Document Frequency (TF-IDF)** solves the Bag of Words problem.\n- **TF (Term Frequency)**: How often does the word appear in *this specific review*? (More is better).\n- **IDF (Inverse Document Frequency)**: How often does the word appear in *every single review in the dataset*? (More is worse).\n\nIf the word `\"the\"` appears 10 times in a review, TF goes up. But since `\"the\"` appears in all 10,000 reviews, IDF crushes the math down to almost 0. \nIf the word `\"masterpiece\"` appears 2 times in a review, TF goes up. Since it rarely appears across the 10,000 reviews, IDF stays high. The model learns that `\"masterpiece\"` is highly important!"),
    
    create_markdown_cell("## 6. Scikit-learn API\n```python\nfrom sklearn.feature_extraction.text import TfidfVectorizer\n\n# Create the mathematical text-to-numbers engine\nvectorizer = TfidfVectorizer(stop_words='english')\n\n# Convert an array of raw strings into a mathematical matrix\nX_matrix = vectorizer.fit_transform([\"Sentence one\", \"Sentence two\"])\n```"),
    
    create_markdown_cell("## 7. Simple Example: From Text to Math\nLet's take 4 tiny movie reviews and watch what `CountVectorizer` does to them."),
    create_code_cell([
        "import pandas as pd",
        "from sklearn.feature_extraction.text import CountVectorizer",
        "",
        "reviews = [",
        "    'I loved the movie',",
        "    'The movie was okay',",
        "    'I hated the movie',",
        "    'The movie was terrible and I hated it'",
        "]",
        "",
        "cv = CountVectorizer()",
        "X_cv = cv.fit_transform(reviews)",
        "",
        "# Convert the output matrix back into a DataFrame so we can read it!",
        "df_cv = pd.DataFrame(X_cv.toarray(), columns=cv.get_feature_names_out())",
        "print('CountVectorizer Bag of Words:')",
        "print(df_cv)"
    ]),
    
    create_markdown_cell("## 8. Code Walkthrough\n- `CountVectorizer` automatically tokenized (split) the text into words.\n- It automatically lowercased everything.\n- It created 9 unique columns (the Vocabulary).\n- Look at the row for `\"I loved the movie\"`. It correctly placed a `1` in the `loved` column, the `movie` column, and the `the` column."),
    
    create_markdown_cell("## 9. Experiment: Stop Words and TF-IDF\nLet's upgrade to `TfidfVectorizer` and tell it to drop \"Stop Words\" (common English words like 'the', 'was', 'and', 'it'). Watch how the math changes!"),
    create_code_cell([
        "from sklearn.feature_extraction.text import TfidfVectorizer",
        "",
        "# We tell it to strip out common english fluff",
        "tfidf = TfidfVectorizer(stop_words='english')",
        "X_tfidf = tfidf.fit_transform(reviews)",
        "",
        "df_tfidf = pd.DataFrame(X_tfidf.toarray(), columns=tfidf.get_feature_names_out())",
        "print('TF-IDF Matrix (Notice the floats instead of ints!):')",
        "print(df_tfidf)"
    ]),
    create_markdown_cell("> - Notice that 'the', 'was', 'and', 'i', and 'it' have been completely deleted from the columns!\n> - The math is no longer 1s and 0s. The word `loved` in the first review has a massive score of `0.79`, proving to the model that it is the most critical word in that sentence."),
    
    create_markdown_cell("## 10. Prediction Exercise\nRead the following scenario, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "advanced_tfidf = TfidfVectorizer(ngram_range=(1, 2))",
        "X_advanced = advanced_tfidf.fit_transform(['not good'])"
    ]),
    create_markdown_cell("> **Question:** By default, vectorizers look at 1 word at a time (`ngram_range=(1,1)`). If a review says `\"not good\"`, the model sees the word `not` and the word `good` completely separately, which destroys the context.\n> By setting `ngram_range=(1, 2)`, we tell the vectorizer to create columns for single words (unigrams) AND pairs of words (bigrams). \n> What exact columns will `X_advanced` have?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print(advanced_tfidf.get_feature_names_out())",
        "print('\\nThe model now has a column specifically for the concept of \"not good\"!')"
    ]),
    
    create_markdown_cell("## 11. Coding Exercise\nLet's build a full NLP Pipeline! \n1. Create a `Pipeline` containing `TfidfVectorizer(stop_words='english')` and `MultinomialNB()` (Naive Bayes).\n2. Train the pipeline on the `reviews` list from above, predicting these sentiment labels: `[1, 1, 0, 0]`.\n3. Make a prediction on a brand new review: `\"I really hated that terrible movie\"`.\n\n*(Note: Naive Bayes is extremely popular for NLP because it calculates probabilities incredibly fast even when TF-IDF generates matrices with 50,000 columns!)*"),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.naive_bayes import MultinomialNB",
        "",
        "nlp_pipe = Pipeline([",
        "    ('vectorizer', TfidfVectorizer(stop_words='english')),",
        "    ('classifier', MultinomialNB())",
        "])",
        "",
        "# Train on the 4 reviews",
        "labels = [1, 1, 0, 0]",
        "nlp_pipe.fit(reviews, labels)",
        "",
        "# Predict a new raw string",
        "new_review = ['I really hated that terrible movie']",
        "pred = nlp_pipe.predict(new_review)",
        "",
        "print(f'Review: {new_review[0]}')",
        "print(f'Predicted Sentiment: {\"Positive\" if pred[0] == 1 else \"Negative\"}')"
    ]),
    
    create_markdown_cell("## 12. Summary of Bonus Day 34\n- **Vectorizers** turn raw text into mathematical matrices.\n- **CountVectorizer** simply counts word occurrences (Bag of Words).\n- **TfidfVectorizer** calculates importance, heavily weighting rare/unique words and crushing common words.\n- **Stop Words** are common fluff ('the', 'a', 'is') that should be deleted.\n- **N-grams** allow the model to learn pairs of words (like 'very bad') to preserve context.\n- Vectorizers slide perfectly into **Pipelines** as the first step before classification.")
]

notebook = {
    "cells": day34_cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

filename = "Day_34_Natural_Language_Processing.ipynb"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Created {filename} successfully!")
