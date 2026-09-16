# Day 46: Power Analysis & Sample Size

Before launching an A/B test, the most common question a data scientist gets is: "How many users do we need in the test, and how long should we run it?" Power Analysis answers this question.

---

## 1. The Four Pillars of Power Analysis
Statistical power is the probability that a test will correctly reject a false null hypothesis (i.e., the probability of detecting an effect if there really is one). Power analysis links four variables together; if you know three, you can calculate the fourth.

1. **Sample Size ($n$):** The number of observations per group.
2. **Effect Size (e.g., Cohen's $d$):** How big of a difference do you expect (or want) to see between the groups? A tiny difference requires a massive sample size to detect.
3. **Significance Level ($\alpha$):** The probability of a false positive (usually 0.05).
4. **Statistical Power ($1 - \beta$):** The probability of a true positive (usually set to 0.80).

---

## 2. Core Concepts & Operations

### Calculating Sample Size
We usually set $\alpha=0.05$ and Power=0.80. We define our Minimum Detectable Effect (MDE). Then we calculate $n$.

```python
from statsmodels.stats.power import TTestIndPower

# We want to detect a "small" effect size of 0.2 (Cohen's d)
# Alpha is 0.05 (5% false positive rate)
# Power is 0.80 (80% chance to detect the effect if it exists)
effect_size = 0.2
alpha = 0.05
power = 0.80

# Initialize the power analysis object for a two-sample independent t-test
analysis = TTestIndPower()

# Calculate the required sample size per group
# 'alternative' is two-sided because the new feature could be better OR worse
sample_size = analysis.solve_power(
    effect_size=effect_size, 
    alpha=alpha, 
    power=power, 
    alternative='two-sided'
)

print(f"Required sample size per group: {int(round(sample_size))}")
# If you have 2 groups (A and B), you need 2 * sample_size total users.
```

### Why is this important?
* If you run a test with too few users, your test is **underpowered**. You might miss a great feature just because you didn't have enough data to prove it worked.
* If you run a test with far too many users, you are wasting time and exposing users to potentially bad variations for longer than necessary.

---

## 3. Reference Documentation
* [Statsmodels TTestIndPower](https://www.statsmodels.org/stable/generated/statsmodels.stats.power.TTestIndPower.html)
* [Statistical Power (Wikipedia)](https://en.wikipedia.org/wiki/Power_of_a_test)
