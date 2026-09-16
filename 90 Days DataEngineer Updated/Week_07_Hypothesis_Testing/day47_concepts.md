# Day 47: Sample Ratio Mismatch (SRM)

You designed a perfect A/B test. You calculated the sample size. You set the traffic split to 50% Control and 50% Treatment. You waited two weeks. 
But when you look at the data, Control has 51,000 users and Treatment has 49,000 users. Is this a normal random fluctuation, or is your experimentation platform broken? This is SRM.

---

## 1. What is Sample Ratio Mismatch?
SRM occurs when the observed traffic split in an A/B test deviates significantly from the expected traffic split. 
* **Expected:** 50/50
* **Observed:** 51/49

If the deviation is statistically significant, your test is **invalid**. SRM usually indicates a severe logging bug, a performance issue causing one variation to load slower (so users bounce before being logged), or a redirect loop. **Never trust the results of an A/B test that has an SRM.**

---

## 2. Core Concepts & Operations

### Checking for SRM using Goodness of Fit
To check for SRM, we use a specific variant of the Chi-Square test called the **Goodness of Fit** test. It compares an observed distribution of counts against an expected theoretical distribution.

* **Null Hypothesis ($H_0$):** The observed counts match the expected ratio (any difference is just random noise).
* **Alternative Hypothesis ($H_1$):** The observed counts do NOT match the expected ratio (we have an SRM!).

```python
import scipy.stats as stats

# Expected traffic split: 50% / 50%
# We observed 100,000 total users
observed_control = 51000
observed_treatment = 49000
total_users = observed_control + observed_treatment

# Calculate exactly how many we EXPECTED to see in each group
expected_control = total_users * 0.50
expected_treatment = total_users * 0.50

# Run the Chi-Square Goodness of Fit test
chi2_stat, p_value = stats.chisquare(
    f_obs=[observed_control, observed_treatment],
    f_exp=[expected_control, expected_treatment]
)

print(f"P-Value: {p_value:.6f}")

if p_value < 0.05:
    print("SRM DETECTED! (Reject Null) - Do not trust the A/B test results. Investigate the logging/bucketing pipeline.")
else:
    print("Traffic looks fine. (Fail to reject Null) - You can proceed with analyzing the A/B test.")
```

---

## 3. Reference Documentation
* [SciPy chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)
* [Diagnosing Sample Ratio Mismatch (Microsoft Paper)](https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/)
