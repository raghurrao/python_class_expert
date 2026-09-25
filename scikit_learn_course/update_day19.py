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

day19_cells = [
    create_markdown_cell("# PHASE 3 — CLASSIFICATION"),
    create_markdown_cell("# Day 19 — Naive Bayes"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain Bayes' Theorem in simple terms.\n- Understand why the algorithm is called \"Naive\".\n- Implement `MultinomialNB` for Text Classification (Spam vs Ham).\n- Implement `GaussianNB` for continuous numerical data."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 15 (Classification Concepts)."),
    
    create_markdown_cell("## 3. Concept: Probability over Geometry\nLogistic Regression draws lines. KNN measures physical distance. SVMs draw streets.\n**Naive Bayes** does absolutely no geometry. It is a purely probabilistic algorithm based on **Bayes' Theorem**.\n\nBayes' Theorem asks: *\"What is the probability of A happening, given that we know B just happened?\"*\nExample: *\"What is the probability an email is Spam, given that the word 'Viagra' is in it?\"*"),
    
    create_markdown_cell("## 4. Why Does This Matter?\nNaive Bayes is blindingly fast. It requires almost zero training time (it just counts frequencies). For decades, it was the absolute gold standard for Text Classification and Spam Filtering because it scales effortlessly to millions of rows and hundreds of thousands of features (words)."),
    
    create_markdown_cell("## 5. Intuition\nIf you see an animal that is yellow, has a long neck, and eats leaves, what is it?\n- P(Yellow | Giraffe) = High\n- P(Long Neck | Giraffe) = High\n- P(Eats Leaves | Giraffe) = High\n\nBy multiplying those probabilities together, the model concludes there is a 99.9% chance the animal is a Giraffe. \n\n**Why is it \"Naive\"?** \nBecause it naively assumes that every feature is completely independent. It assumes the fact that the animal is \"yellow\" has absolutely nothing to do with the fact it has a \"long neck\". Even though this assumption is usually false in the real world, the math still works incredibly well!"),
    
    create_markdown_cell("## 6. Scikit-learn API\nScikit-learn has different versions of Naive Bayes depending on your data:\n- `GaussianNB`: Used when your features are continuous numbers (like salary, age, height).\n- `MultinomialNB`: Used when your features are discrete counts (like the number of times a word appears in an email).\n\n```python\nfrom sklearn.naive_bayes import MultinomialNB, GaussianNB\nmodel = MultinomialNB()\n```"),
    
    create_markdown_cell("## 7. Simple Example: Spam Filtering\nWe will build a simple Spam Filter. First, we need to convert text into numbers so the model can read it. We use `CountVectorizer` which just counts how many times each word appears."),
    create_code_cell([
        "import numpy as np",
        "import pandas as pd",
        "from sklearn.feature_extraction.text import CountVectorizer",
        "from sklearn.naive_bayes import MultinomialNB",
        "from sklearn.metrics import accuracy_score",
        "",
        "# 1. Mock Dataset (0 = Normal, 1 = Spam)",
        "emails = [",
        "    'hey mom call me later',",
        "    'meeting at 3pm tomorrow',",
        "    'win a free rolex watch now',",
        "    'get cheap viagra pills free',",
        "    'lunch is ready',",
        "    'click here for free money'",
        "]",
        "y = np.array([0, 0, 1, 1, 0, 1])",
        "",
        "# 2. Convert Text to Numbers (Word Counts)",
        "vectorizer = CountVectorizer()",
        "X = vectorizer.fit_transform(emails)",
        "",
        "# 3. Train Naive Bayes",
        "nb_model = MultinomialNB()",
        "nb_model.fit(X, y)",
        "",
        "print('Accuracy on Training Data:', accuracy_score(y, nb_model.predict(X)))"
    ]),
    
    create_markdown_cell("## 8. Code Walkthrough\n- `CountVectorizer` looked at all 6 emails, built a massive dictionary of every unique word, and created a grid of 0s and 1s representing whether a word appeared in a specific email.\n- `MultinomialNB` just counted probabilities. It realized that 100% of the times the word 'free' appeared, the label was `1`. \n- It \"learned\" that $P(Spam \\mid 'free') = High$."),
    
    create_markdown_cell("## 9. Experiment\nLet's write a brand new email the model has never seen before and see if it can catch it."),
    create_code_cell([
        "new_email = ['mom wants to win a free rolex']",
        "",
        "# We MUST transform the new email using the EXACT SAME vectorizer we fit earlier!",
        "new_X = vectorizer.transform(new_email)",
        "",
        "prediction = nb_model.predict(new_X)",
        "probability = nb_model.predict_proba(new_X)",
        "",
        "print(f'Email: \"{new_email[0]}\"')",
        "print(f'Prediction: {prediction[0]} (1=Spam, 0=Normal)')",
        "print(f'Confidence: {probability[0][1]*100:.1f}%')"
    ]),
    create_markdown_cell("> Notice that even though the word 'mom' usually implies Normal, the words 'win', 'free', and 'rolex' overwhelmingly pushed the Naive Bayes probability math into the Spam category!"),
    
    create_markdown_cell("## 10. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.naive_bayes import GaussianNB",
        "from sklearn.datasets import make_classification",
        "",
        "X_continuous, y_cont = make_classification(n_samples=100, n_features=4, random_state=42)",
        "",
        "# If we try to use MultinomialNB on continuous, negative numbers...",
        "try:",
        "    bad_nb = MultinomialNB()",
        "    bad_nb.fit(X_continuous, y_cont)",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Question:** Why will `MultinomialNB` crash if given standard continuous data (which often contains negative numbers)?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('MultinomialNB is mathematically designed for COUNTS (e.g., this word appeared 3 times).')",
        "print('You cannot have a negative count. Therefore, MultinomialNB crashes if it sees negative numbers.')",
        "print('For continuous data with negatives, you MUST use GaussianNB.')"
    ]),
    
    create_markdown_cell("## 11. Coding Exercise\nProve the concept above. Instantiate a `GaussianNB()` model, fit it on `X_continuous` and `y_cont`, and print its training accuracy."),
    create_code_cell([
        "# YOUR CODE HERE",
        "gauss_nb = GaussianNB()",
        "gauss_nb.fit(X_continuous, y_cont)",
        "print('GaussianNB Accuracy:', accuracy_score(y_cont, gauss_nb.predict(X_continuous)))"
    ]),
    
    create_markdown_cell("## 12. Debugging Challenge\nA junior developer tried to use a pipeline to process new emails. The code works for training, but crashes when predicting on new data. Why?"),
    create_code_cell([
        "# Buggy Code",
        "try:",
        "    train_emails = ['win money', 'call mom']",
        "    test_emails = ['win a car']",
        "    ",
        "    vec = CountVectorizer()",
        "    X_train_bad = vec.fit_transform(train_emails)",
        "    ",
        "    # THE BUG IS HERE:",
        "    X_test_bad = vec.fit_transform(test_emails)",
        "    ",
        "    model = MultinomialNB()",
        "    model.fit(X_train_bad, [1, 0])",
        "    model.predict(X_test_bad)",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** They called `.fit_transform()` on the test set! `fit` means \"learn a new vocabulary\". The training set learned a vocabulary of 3 words (win, money, call, mom). The test set learned a brand new vocabulary of 3 words (win, a, car). \n> **Rule:** You must ALWAYS use `.transform()` (NEVER `fit_transform`) on test data. Using a Scikit-learn `Pipeline` automatically prevents this bug."),
    
    create_markdown_cell("## 13. Model Evaluation (The Zero-Frequency Problem)\nWhat happens if Naive Bayes encounters a word it has *never* seen before in the training set? \nMathematically, the probability of that word is `0`. Because Naive Bayes multiplies all probabilities together, a single `0` destroys the entire equation ($0.9 \\times 0.8 \\times 0 = 0$). \nScikit-learn automatically fixes this by adding `1` to every count behind the scenes. This is called **Laplace Smoothing** (`alpha=1.0`)."),
    
    create_markdown_cell("## 14. Real-World Example\nBeyond Spam Filters, Naive Bayes is heavily used in **Sentiment Analysis**. Companies scrape Twitter for millions of tweets mentioning their brand. Naive Bayes learns the probability that a tweet is Positive, Negative, or Neutral based on the frequencies of words like 'love', 'terrible', 'broken', etc. Because it is so fast, it can process millions of live tweets per second."),
    
    create_markdown_cell("## 15. Mini Project\nBuild a bullet-proof Pipeline that combines `CountVectorizer` and `MultinomialNB`. Train it on the `emails` array. Predict on the `new_email` array. This prevents the bug from Section 12 permanently!"),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "",
        "nlp_pipe = Pipeline([",
        "    ('vectorizer', CountVectorizer()),",
        "    ('nb', MultinomialNB())",
        "])",
        "",
        "nlp_pipe.fit(emails, y)",
        "safe_prediction = nlp_pipe.predict(new_email)",
        "print('Pipeline Prediction:', safe_prediction[0])",
        "print('The Pipeline ensures the test data is safely .transform()\\'d, never fitted!')"
    ]),
    
    create_markdown_cell("## 16. Common Mistakes\n- **Applying MultinomialNB to continuous data**: Causes errors or terrible accuracy. Use GaussianNB.\n- **Data Leakage in Text**: Calling `fit_transform` on the entire dataset *before* running `train_test_split`. The Vectorizer will \"cheat\" by learning words that only appear in the Test set.\n- **Not using a Pipeline**: Text processing pipelines are mandatory to avoid dimension mismatch errors between train and test."),
    
    create_markdown_cell("## 17. Interview Questions\n- **Beginner**: Why is Naive Bayes so fast? (Answer: It doesn't use complex calculus or gradient descent; it just counts frequencies and calculates basic probabilities).\n- **Intermediate**: Why is it called \"Naive\"? (Answer: Because it naively assumes every single feature is completely independent of the others).\n- **Advanced**: Explain Laplace Smoothing and why it is necessary. (Answer: It prevents the Zero-Frequency problem where an unseen word drops the entire probability equation to zero)."),
    
    create_markdown_cell("## 18. Knowledge Check\n- Which version of Naive Bayes do you use for text/word counts? (`MultinomialNB`)\n- Which version do you use for continuous numbers? (`GaussianNB`)"),
    
    create_markdown_cell("## 19. Summary\n- **Naive Bayes** is a probabilistic classifier based on Bayes' Theorem.\n- It is blindingly fast and excellent for **Text Classification** (NLP).\n- It assumes all features are mathematically independent.\n- `MultinomialNB` for discrete counts (text).\n- `GaussianNB` for continuous numbers.\n- Always use `CountVectorizer` inside a `Pipeline`."),
    
    create_markdown_cell("## 20. Homework\nLoad the `fetch_20newsgroups` dataset from Scikit-learn (it's a massive dataset of 1990s forum posts). Build a Pipeline with `CountVectorizer` and `MultinomialNB`. See how quickly it can accurately classify thousands of text documents!")
]

# Read existing notebook and update cells
filename = "Day_19_Naive_Bayes.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day19_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")
