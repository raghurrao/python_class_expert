# Data Science Mastery Curriculum: Day-by-Day 90-Day Learning Plan

This curriculum provides a structured, daily learning path to elevate you to a Data Science expert. Each day contains a concise **Concept Guide** (`dayX_concepts.md`), an **Assignment Template** with inline exercises (`dayX_assignment.py` or `.ipynb`), and a **Test Runner** (`dayX_test.py`) to automatically verify your solutions.

All learning materials, exercises, and projects will be structured under [DataEngineer](file:///g:/30%20days%20Leaarning/DataEngineer).

---

## User Review Required

> [!IMPORTANT]
> 1. **Time Commitment:** Spanning 90 days allows us to go deep into the mathematical foundations, core algorithms, advanced model tuning, deep learning, NLP/Time-Series, and MLOps.
> 2. **Structure:** Each week has 5 days of structured lessons (Concepts + Assignment + Tests) and a 2-day weekend dedicated to reviews, self-study, and a comprehensive weekly coding challenge.
> 3. **Verification:** Automatic unit tests will continue to run for the coding/algorithm days, and notebook verification will ensure stability for visualizations and projects.

---

## Proposed Curriculum & Changes

### Directory Structure

```
DataEngineer/
├── requirements.txt
├── Week_01_NumPy/
│   ├── day1_concepts.md        # NumPy creation, indexing, slicing, vectorization
│   ├── day1_assignment.py      # Exercise placeholders for Day 1
│   ├── day1_test.py            # Automated tests using unittest for Day 1
│   ├── ...
│   └── week1_challenge.py      # NumPy image processing challenge
├── Week_02_Pandas_Basics/
│   ├── day8_...
│   └── week2_challenge.py      # Data cleaning pipeline challenge
├── Week_03_Advanced_Pandas_SQL/
│   ├── day15_...
│   └── week3_challenge.py      # Relational database analytics report
├── Week_04_EDA_Visualization/
├── Week_05_Math_For_ML/
├── Week_06_Probability_Stats/
├── Week_07_Hypothesis_Testing/
├── Week_08_ML_Regression/
├── Week_09_ML_Classification/
├── Week_10_Evaluation_Unsupervised/
├── Week_11_Deep_Learning_Special/
├── Week_12_MLOps_Serving/
└── Capstone_Project/            # Days 85-90: Containerized predictive FastAPI project
```

---

### Day-by-Day Breakdown

#### **Month 1: Data Analytics, SQL, & Mathematics (Days 1–35)**

##### **Week 1: NumPy Foundations (Days 1–7)**
*   **Day 1: NumPy Array Basics, Slicing & Shapes**
    *   *Concept:* Creating arrays, memory layout (contiguous blocks), array attributes, indexing, slicing.
    *   *Assignment:* temperature converter, Boolean slicing, min-max normalizer.
    *   *Test:* `day1_test.py` (Assert conversions and normalization formulas).
*   **Day 2: Array Manipulation & Attributes**
    *   *Concept:* Shape manipulation (reshape, flatten, ravel), joining arrays (stack, concat), splitting.
    *   *Assignment:* Re-arranging dimensional sensor records and stacking features.
    *   *Test:* `day2_test.py`
*   **Day 3: NumPy Vectorization & Math Operations**
    *   *Concept:* Ufuncs (universal functions), speed comparison, algebraic operations, trigonometric functions.
    *   *Assignment:* Matrix scaling and array element-wise arithmetic comparisons.
    *   *Test:* `day3_test.py`
*   **Day 4: NumPy Broadcasting Rules**
    *   *Concept:* Broadcasting dimensions, conditions for alignment, axis manipulation.
    *   *Assignment:* Normalizing matrices by row/column vectors.
    *   *Test:* `day4_test.py`
*   **Day 5: Boolean Indexing & Filtering**
    *   *Concept:* Conditional selection, boolean operators (`&`, `|`, `~`), `np.where`.
    *   *Assignment:* Outlier filtering on stock prices.
    *   *Test:* `day5_test.py`
*   **Day 6-7: Week 1 Challenge: NumPy Image Processing**
    *   *Challenge:* Load an image as a matrix, apply grayscale transformation, crop, and adjust brightness without loops.

##### **Week 2: Tabular Data with Pandas (Days 8–14)**
*   **Day 8: Pandas Series & DataFrames**
    *   *Concept:* Pandas data structures, loading files (CSV, JSON, Excel), index manipulation.
    *   *Assignment:* Loading and examining dataset shapes and heads.
    *   *Test:* `day8_test.py`
*   **Day 9: Data Cleaning & Type Casting**
    *   *Concept:* Drop/fill nulls, handling duplicates, type conversion (string to numeric, categorical).
    *   *Assignment:* Cleaning a messy raw customer contact dataset.
    *   *Test:* `day9_test.py`
*   **Day 10: Slicing, Filtering & Querying**
    *   *Concept:* `.loc` vs `.iloc`, conditional filters, multi-condition querying, renaming columns.
    *   *Assignment:* Filter customer datasets by criteria (e.g. location, order value).
    *   *Test:* `day10_test.py`
*   **Day 11: String & Datetime Processing**
    *   *Concept:* `.str` accessors, datetime conversions, extract month/day/year, timezone handling.
    *   *Assignment:* Parse dates and extract marketing campaign metrics from text strings.
    *   *Test:* `day11_test.py`
*   **Day 12: Data Aggregation & Value Counts**
    *   *Concept:* Aggregation methods (mean, median, standard deviation), `value_counts`, unique values.
    *   *Assignment:* Analyze user activity records to determine usage frequencies.
    *   *Test:* `day12_test.py`
*   **Day 13-14: Week 2 Challenge: E-commerce Order Cleaning Pipeline**
    *   *Challenge:* Construct an automated pipeline function that takes a raw, messy Excel sheet and outputs a clean Pandas DataFrame.

##### **Week 3: Advanced Pandas & SQL (Days 15–21)**
*   **Day 15: Table Joins & Merges**
    *   *Concept:* Inner, outer, left, right merges; concatenating data along axes.
    *   *Assignment:* Combine customer metadata with order transactions.
    *   *Test:* `day15_test.py`
*   **Day 16: Reshaping Data & Pivots**
    *   *Concept:* `pivot_table`, `melt`, `stack`, `unstack`.
    *   *Assignment:* Convert wide sales data to long format and build summary reports.
    *   *Test:* `day16_test.py`
*   **Day 17: Introduction to SQLite in Python**
    *   *Concept:* Connecting to databases using SQLite3, executing queries from Python, converting outputs to Pandas.
    *   *Assignment:* Create tables, insert records, and query statistics.
    *   *Test:* `day17_test.py`
*   **Day 18: SQL Aggregations & Grouping**
    *   *Concept:* SELECT, WHERE, GROUP BY, HAVING, COUNT, SUM, AVG.
    *   *Assignment:* Write query analytics for employee salary datasets.
    *   *Test:* `day18_test.py`
*   **Day 19: Advanced SQL: Subqueries, Joins, & Windows**
    *   *Concept:* Subqueries, CTEs (Common Table Expressions), Window functions (ROW_NUMBER, RANK, LAG/LEAD).
    *   *Assignment:* Calculate rolling cumulative sales and customer purchase intervals in SQL.
    *   *Test:* `day19_test.py`
*   **Day 20-21: Week 3 Challenge: Business Analytics Relational Database**
    *   *Challenge:* Write a complete Python dashboard script querying SQLite with advanced windows and exporting metrics to Pandas.

##### **Week 4: Exploratory Data Analysis & Visualization (Days 22–28)**
*   **Day 22: Matplotlib Fundamentals**
    *   *Concept:* Anatomy of a figure, axes objects, subplots, line plots, bar charts, custom labels.
    *   *Assignment:* Plot product pricing trend variations over a year.
    *   *Test:* `day22_test.py`
*   **Day 23: Seaborn Statistical Visualization**
    *   *Concept:* Relational plots (scatterplot), distributions (histplot, kdeplot), categories (boxplot, violinplot).
    *   *Assignment:* Generate statistical distributions of marketing campaign conversions.
    *   *Test:* `day23_test.py`
*   **Day 24: Outlier Detection & Treatment**
    *   *Concept:* Visualizing outliers, IQR (Interquartile Range) formula, Z-score, capping vs. dropping outliers.
    *   *Assignment:* Implement IQR detection and clean outliers in a housing price dataset.
    *   *Test:* `day24_test.py`
*   **Day 25: Correlation Analysis & Heatmaps**
    *   *Concept:* Covariance, Pearson/Spearman correlation coefficients, generating and reading heatmaps.
    *   *Assignment:* Compute a correlation matrix and isolate highly collinear features.
    *   *Test:* `day25_test.py`
*   **Day 26-27: Week 4 Challenge: Full Visual EDA Report**
    *   *Challenge:* Write a Jupyter notebook performing an end-to-end EDA report on the California Housing dataset.

##### **Week 5: Math Foundations for Machine Learning (Days 29–35)**
*   **Day 28: Vectors & Dot Products**
    *   *Concept:* Vector space, vector addition, scalar multiplication, dot product geometric interpretation.
    *   *Assignment:* Code Cosine Similarity between user rating profiles from scratch.
    *   *Test:* `day28_test.py`
*   **Day 29: Matrix Operations & Transformations**
    *   *Concept:* Matrix multiplication, determinants, transposition, inverse matrices, linear equations.
    *   *Assignment:* Solve systems of linear equations using NumPy matrix functions.
    *   *Test:* `day29_test.py`
*   **Day 30: Eigenvalues & Eigenvectors**
    *   *Concept:* Geometrical meaning of eigenvalues/eigenvectors, trace, application in PCA.
    *   *Assignment:* Compute eigenvalues and trace manually and via NumPy.
    *   *Test:* `day30_test.py`
*   **Day 31: Calculus: Limits & Single-Variable Derivatives**
    *   *Concept:* Limits, continuity, derivatives, rules of differentiation (power, product, chain rule).
    *   *Assignment:* Write numerical approximation functions for derivatives.
    *   *Test:* `day31_test.py`
*   **Day 32: Multivariable Calculus: Gradients**
    *   *Concept:* Partial derivatives, Jacobian, gradient vector, directional derivatives.
    *   *Assignment:* Code a gradient computation function for quadratic surfaces.
    *   *Test:* `day32_test.py`
*   **Day 33: Optimization: Gradient Descent Math**
    *   *Concept:* Optimization formulations, local/global minima, step size/learning rate.
    *   *Assignment:* Implement a simple 1D Gradient Descent solver from scratch.
    *   *Test:* `day33_test.py`
*   **Day 34-35: Week 5 Challenge: Mathematical Optimization Engine**
    *   *Challenge:* Implement a multivariable Gradient Descent solver to optimize a custom objective function.

---

#### **Month 2: Statistics & Supervised Learning (Days 36–70)**

##### **Week 6: Probability & Statistics (Days 36–42)**
*   **Day 36: Basic & Conditional Probability**
    *   *Concept:* Probability rules, independent events, Bayes' Theorem.
    *   *Assignment:* Compute conditional probability and implement Bayes rule for diagnostic prediction.
    *   *Test:* `day36_test.py`
*   **Day 37: Probability Distributions**
    *   *Concept:* Uniform, Binomial, Normal, and Poisson distributions (PDF/CDF).
    *   *Assignment:* Simulate Binomial coin tosses and Normal heights distribution.
    *   *Test:* `day37_test.py`
*   **Day 38: Descriptive Statistics & Central Limit Theorem**
    *   *Concept:* Mean, median, mode, variance, standard deviation, skewness, CLT simulation.
    *   *Assignment:* Simulate rolling dice to demonstrate mean convergence.
    *   *Test:* `day38_test.py`
*   **Day 39: Confidence Intervals**
    *   *Concept:* Point estimation, margin of error, confidence interval calculation (Z and T distributions).
    *   *Assignment:* Compute confidence intervals for sample user transactions.
    *   *Test:* `day39_test.py`
*   **Day 40: Introduction to Hypothesis Testing**
    *   *Concept:* $H_0$ vs $H_a$, significance level ($\alpha$), critical values, p-value interpretation.
    *   *Assignment:* Set up hypothesis testing metrics for retail conversions.
    *   *Test:* `day40_test.py`
*   **Day 41-42: Week 6 Challenge: Naive Bayes Text Classification**
    *   *Challenge:* Write a text spam/ham Naive Bayes classifier utilizing probability calculations.

##### **Week 7: Hypothesis Testing & A/B Testing (Days 43–49)**
*   **Day 43: One-Sample & Two-Sample T-tests**
    *   *Concept:* Student's T-test, independent vs paired tests, calculating t-statistics.
    *   *Assignment:* Compare average user sessions on old vs new website designs.
    *   *Test:* `day43_test.py`
*   **Day 44: ANOVA (Analysis of Variance)**
    *   *Concept:* F-statistic, comparing multiple groups, post-hoc tests (Tukey's).
    *   *Assignment:* Analyze marketing costs across three distinct channels.
    *   *Test:* `day44_test.py`
*   **Day 45: Chi-Square Tests**
    *   *Concept:* Categorical dependency testing, Chi-Square goodness-of-fit, independence test.
    *   *Assignment:* Check independence of customer type and product selection.
    *   *Test:* `day45_test.py`
*   **Day 46: A/B Testing: Sample Size & Power Analysis**
    *   *Concept:* Statistical power, effect size (Cohen's d), sample size calculation.
    *   *Assignment:* Estimate the required audience sizes for A/B conversion campaigns.
    *   *Test:* `day46_test.py`
*   **Day 47: A/B Testing Case Study Analysis**
    *   *Concept:* Practical pitfalls: p-hacking, early stopping, sample ratio mismatch (SRM).
    *   *Assignment:* Analyze and debug a broken marketing page design experiment.
    *   *Test:* `day47_test.py`
*   **Day 48-49: Week 7 Challenge: Conversion Experiment Analysis Engine**
    *   *Challenge:* Develop an end-to-end A/B test report analyzer script calculating sample checks, t-tests, and conversions.

##### **Week 8: Supervised Learning - Regression (Days 50–56)**
*   **Day 50: Linear Regression Derivation (OLS)**
    *   *Concept:* Ordinary Least Squares derivation, assumptions of linear model (linearity, independence, normality).
    *   *Assignment:* Manually compute the slope and intercept coefficients on raw data points.
    *   *Test:* `day50_test.py`
*   **Day 51: Scikit-Learn Linear Regression**
    *   *Concept:* Fitting model in sklearn, interpreting coefficients, predicting data points.
    *   *Assignment:* Build and run basic linear regression modeling housing prices.
    *   *Test:* `day51_test.py`
*   **Day 52: Polynomial Regression**
    *   *Concept:* Non-linear relationships, bias-variance trade-off, overfitting.
    *   *Assignment:* Fit polynomial features and evaluate train vs test error scores.
    *   *Test:* `day52_test.py`
*   **Day 53: Regularized Models: Ridge & Lasso**
    *   *Concept:* L1/L2 regularization penalties, feature selection (Lasso), ElasticNet.
    *   *Assignment:* Run regularized models on colinear datasets, evaluating coefficients.
    *   *Test:* `day53_test.py`
*   **Day 54: Regression Evaluation Metrics**
    *   *Concept:* MSE, RMSE, MAE, R-squared, Adjusted R-squared.
    *   *Assignment:* Implement custom regression evaluation functions.
    *   *Test:* `day54_test.py`
*   **Day 55-56: Week 8 Challenge: Housing Prices Prediction Pipeline**
    *   *Challenge:* Train, regularize, and select the optimal regression model using cross-validation.

##### **Week 9: Supervised Learning - Classification (Days 57–63)**
*   **Day 57: Logistic Regression**
    *   *Concept:* Logits, sigmoid activation, binary cross-entropy, decision boundaries.
    *   *Assignment:* Build a logistic classifier predicting medical disease presence.
    *   *Test:* `day57_test.py`
*   **Day 58: Support Vector Machines (SVM)**
    *   *Concept:* Linear margin optimization, support vectors, Kernels (RBF, Polynomial).
    *   *Assignment:* Implement classification boundaries using various SVM kernels.
    *   *Test:* `day58_test.py`
*   **Day 59: Decision Trees**
    *   *Concept:* Recursive partitioning, Gini impurity vs Entropy, tree pruning limits.
    *   *Assignment:* Train and visualize decision boundary tree paths.
    *   *Test:* `day59_test.py`
*   **Day 60: Random Forest Ensembles**
    *   *Concept:* Bagging (Bootstrap Aggregation), feature subspace sampling, feature importance.
    *   *Assignment:* Train customer default classification using Random Forest.
    *   *Test:* `day60_test.py`
*   **Day 61: Boosting Algorithms**
    *   *Concept:* Boosting theory, AdaBoost, Gradient Boosting, XGBoost.
    *   *Assignment:* Train an XGBoost model and compare parameters against Random Forest.
    *   *Test:* `day61_test.py`
*   **Day 62-63: Week 9 Challenge: Customer Churn Classification**
    *   *Challenge:* Build classification models utilizing multiple algorithms, optimizing model parameters for performance.

##### **Week 10: Model Validation & Unsupervised Learning (Days 64–70)**
*   **Day 64: Classification Metrics**
    *   *Concept:* Confusion matrix, precision, recall, F1-score, ROC-AUC, Precision-Recall Curve.
    *   *Assignment:* Implement custom precision-recall threshold selection functions.
    *   *Test:* `day64_test.py`
*   **Day 65: Hyperparameter Optimization**
    *   *Concept:* GridSearch, RandomizedSearch, cross-validation scoring.
    *   *Assignment:* Optimize classifier structures via search spaces.
    *   *Test:* `day65_test.py`
*   **Day 66: Pipelines & Preprocessing**
    *   *Concept:* Pipeline construction, ColumnTransformers, categorical imputation, handling imbalance (SMOTE).
    *   *Assignment:* Build end-to-end preprocessing pipelines on tabular data.
    *   *Test:* `day66_test.py`
*   **Day 67: K-Means Clustering**
    *   *Concept:* Cluster centroids, Elbow method, Silhouette score, WCSS.
    *   *Assignment:* Segment customer transaction patterns using K-Means.
    *   *Test:* `day67_test.py`
*   **Day 68: PCA Dimensionality Reduction**
    *   *Concept:* Variance projection, explained variance ratio, plotting dimensions.
    *   *Assignment:* Condense loan features and plot customer segments in 2D.
    *   *Test:* `day68_test.py`
*   **Day 69-70: Week 10 Challenge: Unsupervised Customer Segmentation Pipeline**
    *   *Challenge:* Complete pre-processing, PCA clustering, and diagnostic segmentation report generation.

---

#### **Month 3: Advanced Topics, MLOps, & Deployment (Days 71–90)**

##### **Week 11: Deep Learning & Special Topics (Days 71–77)**
*   **Day 71: Intro to Neural Networks & PyTorch**
    *   *Concept:* PyTorch tensors, operations, simple Multi-Layer Perceptron (MLP) layers.
    *   *Assignment:* Create layers and feed-forward operations.
    *   *Test:* `day71_test.py`
*   **Day 72: Training Neural Networks**
    *   *Concept:* Loss functions, Backpropagation, SGD/Adam optimizers, training loops.
    *   *Assignment:* Build and train an MLP on MNIST digit classification.
    *   *Test:* `day72_test.py`
*   **Day 73: Time Series Analysis & Forecasting**
    *   *Concept:* Trend, seasonality, stationarity (ADF Test), ARIMA models.
    *   *Assignment:* Forecast electric power usage numbers.
    *   *Test:* `day73_test.py`
*   **Day 74: Natural Language Processing Basics**
    *   *Concept:* Text pre-processing, TF-IDF vectorizers, word tokenization.
    *   *Assignment:* Sentiment analysis using TF-IDF and Logistic Regression.
    *   *Test:* `day74_test.py`
*   **Day 75: Recommender Systems**
    *   *Concept:* Collaborative filtering, similarity matrices, content-based recommendation.
    *   *Assignment:* Build a movie recommendation utility engine.
    *   *Test:* `day75_test.py`
*   **Day 76-77: Week 11 Challenge: Deep Learning Image Classifier**
    *   *Challenge:* Construct and train a PyTorch neural network classifying custom target datasets.

##### **Week 12: Serving Models & API Production (Days 78–84)**
*   **Day 78: Model Serialization & Versioning**
    *   *Concept:* Saving models (joblib, pickle), validation metrics tracking, output reproducibility.
    *   *Assignment:* Export pipeline steps and metadata logs.
    *   *Test:* `day78_test.py`
*   **Day 79: FastAPI: REST API Introduction**
    *   *Concept:* Endpoint structure, path parameters, GET requests, FastAPI setup.
    *   *Assignment:* Build basic utility routes returning system parameters.
    *   *Test:* `day79_test.py`
*   **Day 80: POST Endpoints & Pydantic Schemas**
    *   *Concept:* Request bodies, Pydantic type validation, POST predictions parsing.
    *   *Assignment:* Create data input schemas for prediction requests.
    *   *Test:* `day80_test.py`
*   **Day 81: FastAPI ML Prediction Integration**
    *   *Concept:* Loading models at startup, prediction routing, return structure.
    *   *Assignment:* Serve pipeline predictions through API.
    *   *Test:* `day81_test.py`
*   **Day 82: Dockerizing APIs**
    *   *Concept:* Containers vs VMs, Dockerfile syntax, building and running local containers.
    *   *Assignment:* Containerize the FastAPI predictor model.
    *   *Test:* `day82_test.py`
*   **Day 83-84: Week 12 Challenge: Containerized Prediction Microservice**
    *   *Challenge:* Build, test, and containerize a predictive service serving predictions with input validation.

##### **Final Week: Capstone Project & Portfolio (Days 85–90)**
*   **Day 85: Capstone Formulation & EDA**
    *   *Objective:* Finalize dataset, define predictive goals, and document initial exploratory analysis.
*   **Day 86: Feature Engineering & Preprocessing Pipeline**
    *   *Objective:* Construct robust data pre-processing and automated cleanup pipelines.
*   **Day 87: Model Selection & Hyperparameter Tuning**
    *   *Objective:* Train and optimize multiple model structures, logging accuracy comparisons.
*   **Day 88: Serving Interface FastAPI Application**
    *   *Objective:* Build and write comprehensive test suites for prediction endpoints.
*   **Day 89: Containerization & Portfolio Preparation**
    *   *Objective:* Containerize the Capstone, compose detailed README documentation, and format repository.
*   **Day 90: Capstone Verification & Final Technical Assessment**
    *   *Objective:* Run comprehensive review assessments and conduct mock interviews.

---

## Verification Plan

### Automated Tests
*   Daily concept check files (`dayX_test.py`) will automatically verify parameters using standard Python test frameworks.
*   The capstone API service will contain unit testing blocks executable via:
    ```bash
    pytest Capstone_Project/tests/
    ```

### Manual Verification
*   We will visually inspect regression residuals, ROC-AUC plots, and PCA cluster profiles.
