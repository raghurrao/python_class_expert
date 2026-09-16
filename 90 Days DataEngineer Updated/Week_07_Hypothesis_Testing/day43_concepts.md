# Day 43: T-Tests (Comparing Two Groups)

When we run an A/B test (like checking if a new button color increases clicks), we need a way to know if the difference in clicks is real or just due to random chance. The T-test is the most common tool for this.

---

## 1. What is a T-Test?
A t-test tells you if the means (averages) of two groups are significantly different from each other. 
* **Null Hypothesis ($H_0$):** The means of the two groups are the same. (The new button didn't change anything).
* **Alternative Hypothesis ($H_1$):** The means are different. (The new button worked!)

It evaluates the difference between the means *relative* to the spread (variance) of the data. If the means are far apart and the data is tightly clustered, you get a high t-statistic (and a low p-value).

---

## 2. Core Concepts & Operations

### Independent Two-Sample T-Test
This is used when comparing two completely independent groups (e.g., Group A saw the old website, Group B saw the new website).

```python
import numpy as np
import scipy.stats as stats

# Imagine these are time spent on a website (in seconds)
group_a = np.array([120, 115, 122, 118, 125, 119, 121])
group_b = np.array([130, 135, 128, 132, 134, 129, 131])

# Run the T-test
# equal_var=True assumes both populations have similar variance (Student's t-test)
# equal_var=False uses Welch's t-test, which is safer if variances are different
t_statistic, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

print(f"T-Statistic: {t_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Result: Reject the null hypothesis. The difference is statistically significant.")
else:
    print("Result: Fail to reject the null hypothesis. No significant difference.")
```

### When to use it?
* You are comparing the **means** of exactly **two** groups.
* The data is continuous (like time, revenue, weight).
* The data is roughly normally distributed (though t-tests are robust to violations if the sample size is large).

---

## 3. Reference Documentation
* [SciPy ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)