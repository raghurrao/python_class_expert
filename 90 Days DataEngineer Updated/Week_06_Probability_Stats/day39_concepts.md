# Day 39: Confidence Intervals

When we calculate a mean from a sample (e.g., the average height of 100 people), it's just a point estimate. It's almost certainly not the exact average height of the entire population. A confidence interval gives us a range of values within which we are confident the true population mean lies.

---

## 1. What is a Confidence Interval?
A 95% confidence interval means: "If we were to take 100 different samples and compute a confidence interval for each one, we expect about 95 of those intervals to contain the true population mean."

It is **NOT**: "There is a 95% probability that the true mean falls within this specific interval." (The true mean is a fixed value; it's either in the interval or it isn't).

---

## 2. Core Concepts & Operations

### Calculating a Confidence Interval
To calculate a confidence interval for a sample mean, we need:
1. **Sample Mean ($\bar{x}$)**
2. **Standard Error of the Mean (SEM):** Measures how far the sample mean of the data is likely to be from the true population mean. It's calculated as the sample standard deviation divided by the square root of the sample size ($s / \sqrt{n}$).
3. **Critical Value:** Based on our desired confidence level (e.g., 95%) and the distribution (usually the t-distribution if the sample size is small or population standard deviation is unknown).

```python
import numpy as np
import scipy.stats as stats

def compute_confidence_interval(data: np.ndarray, confidence: float = 0.95):
    """
    Compute the confidence interval for the mean of data using the t-distribution.
    """
    n = len(data)
    mean = np.mean(data)
    
    # Calculate Standard Error of the Mean
    sem = stats.sem(data)
    
    # Calculate the margin of error using the t-distribution's Percent Point Function (PPF)
    # df is degrees of freedom (n-1)
    margin = sem * stats.t.ppf((1 + confidence) / 2., n-1)
    
    lower_bound = mean - margin
    upper_bound = mean + margin
    
    return mean, lower_bound, upper_bound

# Example usage
sample_data = np.array([2.3, 3.1, 2.8, 3.4, 2.9, 3.2, 2.7])
mean, lower, upper = compute_confidence_interval(sample_data)

print(f"Sample Mean: {mean:.2f}")
print(f"95% Confidence Interval: [{lower:.2f}, {upper:.2f}]")
# We are 95% confident that the true population mean is between 'lower' and 'upper'
```

---

## 3. Reference Documentation
* [Scipy stats.sem](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.sem.html)
* [Confidence Interval (Wikipedia)](https://en.wikipedia.org/wiki/Confidence_interval)
