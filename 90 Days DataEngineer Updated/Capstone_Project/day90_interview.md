# Day 90: Career & Mock Technical Interview

Congratulations! You have completed the 90-day Data Science Mastery course!

## Standard Technical Interview Questions:

### 1. Machine Learning Basics
* **Question:** Explain the trade-off between Bias and Variance.
* **Answer:** Bias is error from erroneous assumptions in the learning algorithm (leads to underfitting). Variance is error from sensitivity to small fluctuations in the training set (leads to overfitting). As complexity increases, bias decreases and variance increases.

### 2. Tabular Data & SQL
* **Question:** What is the difference between an INNER JOIN and a LEFT JOIN in SQL?
* **Answer:** An INNER JOIN returns records that have matching values in both tables. A LEFT JOIN returns all records from the left table, and the matched records from the right table; missing values are returned as NULL.

### 3. Deployments & Serving
* **Question:** Why use Docker for serving Machine Learning models?
* **Answer:** Docker containers wrap all model weights, code files, OS libraries, and specific version dependencies together. This guarantees that your model runs identically on your local laptop, staging environments, and Kubernetes cloud clusters.