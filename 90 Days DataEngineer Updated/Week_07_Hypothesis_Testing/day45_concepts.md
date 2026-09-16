# Day 45: Chi-Square Test for Independence

T-tests and ANOVAs are for comparing *continuous* numerical data (like revenue, time, or height) across groups. But what if your data is *categorical* (like Yes/No, Red/Blue/Green)?

---

## 1. What is a Chi-Square Test?
The Chi-Square ($\chi^2$) test of independence determines if there is a significant association between two categorical variables. 

* **Null Hypothesis ($H_0$):** The two variables are completely independent (no relationship).
* **Alternative Hypothesis ($H_1$):** The two variables are dependent (there is a relationship).

For example, is "Subscribing to Premium" (Yes/No) independent of "Device Type" (Mobile/Desktop)?

---

## 2. Core Concepts & Operations

### Contingency Tables
To run a Chi-Square test, you first need to summarize your data into a contingency table (a frequency matrix), showing how many times each combination of categories occurred.

### Running the Test in Python

```python
import numpy as np
import scipy.stats as stats

# Example: Do mobile users click the "Buy" button more than desktop users?
# Rows = Device (Mobile, Desktop)
# Columns = Action (Clicked Buy, Did Not Click)
# Let's say:
# Mobile: 120 Clicked, 880 Didn't (Total 1000)
# Desktop: 80 Clicked, 920 Didn't (Total 1000)

contingency_table = np.array([
    [120, 880], # Mobile row
    [80,  920]  # Desktop row
])

# Run the Chi-Square test
chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print(f"Chi-Square Statistic: {chi2_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject null hypothesis: There is a significant relationship between Device and Clicking 'Buy'.")
else:
    print("Fail to reject null: Device type and clicking 'Buy' appear independent.")
```

---

## 3. Reference Documentation
* [SciPy chi2_contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)
* [Chi-squared test (Wikipedia)](https://en.wikipedia.org/wiki/Chi-squared_test)
