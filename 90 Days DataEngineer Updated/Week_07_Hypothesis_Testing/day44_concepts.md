# Day 44: ANOVA (Comparing 3+ Groups)

If you are running an A/B/C test (testing three different website designs), you might think to just run three separate T-tests (A vs B, B vs C, A vs C). **Don't do this.**

---

## 1. Why ANOVA?
Every time you run a statistical test with an alpha of 0.05, there's a 5% chance of a false positive. If you run three tests, your overall chance of a false positive inflates significantly. 

**ANOVA (Analysis of Variance)** allows you to compare the means of 3 or more groups simultaneously with a single test.
* **Null Hypothesis ($H_0$):** All groups have the exact same population mean.
* **Alternative Hypothesis ($H_1$):** At least one group's mean is different from the others.

*Note:* ANOVA tells you *if* there is a difference, but it doesn't tell you *which* specific groups are different. You need post-hoc tests (like Tukey's HSD) for that.

---

## 2. Core Concepts & Operations

### One-Way ANOVA
"One-Way" means we are looking at the effect of one independent variable (e.g., website design) that has multiple levels (Design A, Design B, Design C) on a continuous dependent variable (e.g., conversion rate).

```python
import numpy as np
import scipy.stats as stats

# Sample data: Revenue per user for three different marketing campaigns
group_1 = np.array([50, 55, 52, 48, 51])
group_2 = np.array([60, 62, 58, 65, 61])
group_3 = np.array([51, 49, 53, 50, 52])

# Run One-Way ANOVA
f_statistic, p_value = stats.f_oneway(group_1, group_2, group_3)

print(f"F-Statistic: {f_statistic:.4f}")
print(f"P-Value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject null hypothesis: At least one group mean is different.")
else:
    print("Fail to reject null: No significant difference among groups.")
```

---

## 3. Reference Documentation
* [SciPy f_oneway](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html)
* [ANOVA (Wikipedia)](https://en.wikipedia.org/wiki/Analysis_of_variance)
