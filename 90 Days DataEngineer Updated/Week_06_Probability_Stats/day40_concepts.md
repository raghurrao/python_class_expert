# Day 40: P-Values and Hypothesis Testing

Hypothesis testing is a formal procedure used by statisticians to accept or reject statistical hypotheses. It forms the foundation of A/B testing in data science.

---

## 1. The Setup
1. **Null Hypothesis ($H_0$):** The default assumption. Typically states there is "no effect" or "no difference" (e.g., "The new website design does not increase sales").
2. **Alternative Hypothesis ($H_a$ or $H_1$):** The claim we are trying to prove (e.g., "The new website design increases sales").
3. **Significance Level ($\alpha$):** The probability of rejecting the null hypothesis when it is actually true (a false positive). Usually set to 0.05 (5%).

---

## 2. What is a P-Value?
The p-value is the probability of obtaining test results at least as extreme as the results actually observed, **under the assumption that the null hypothesis is correct**.

* **If p-value $\le \alpha$:** The observed data is highly unlikely under the null hypothesis. We **reject the null hypothesis** in favor of the alternative. Our results are "statistically significant."
* **If p-value $> \alpha$:** The observed data is somewhat likely even if the null hypothesis is true. We **fail to reject the null hypothesis**. We don't have enough evidence to prove the alternative.

*Important:* We never "accept" the null hypothesis, we only "fail to reject" it.

---

## 3. Core Concepts & Operations

### Simple Evaluation
In a real-world scenario, you would use statistical tests (like a t-test or z-test) to calculate the p-value. Once you have it, evaluating it is straightforward.

```python
def evaluate_p_value(p_value: float, alpha: float = 0.05) -> str:
    """
    Evaluates statistical significance based on the p-value and alpha.
    """
    if p_value <= alpha:
        return f"p={p_value:.4f} <= {alpha}. Reject the null hypothesis. The result is statistically significant."
    else:
        return f"p={p_value:.4f} > {alpha}. Fail to reject the null hypothesis. Not statistically significant."

# Scenario 1: A/B Test for Conversion Rate shows a p-value of 0.02
print(evaluate_p_value(0.02))

# Scenario 2: Testing a new drug shows a p-value of 0.15
print(evaluate_p_value(0.15))
```

---

## 4. Reference Documentation
* [P-value (Wikipedia)](https://en.wikipedia.org/wiki/P-value)
* [Statistical hypothesis testing (Wikipedia)](https://en.wikipedia.org/wiki/Statistical_hypothesis_testing)
