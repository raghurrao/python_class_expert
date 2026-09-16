# Day 37: Probability Distributions

A probability distribution describes the mathematical rules that govern how probabilities are distributed across all possible outcomes of a random experiment.

---

## 1. Discrete vs. Continuous Distributions
* **Discrete Distributions:** Variables can only take on specific, separate values (e.g., number of heads in 10 coin flips, number of customers in a store).
* **Continuous Distributions:** Variables can take on any value within a range (e.g., exact height of a person, time to finish a race).

---

## 2. Core Concepts & Operations

### The Binomial Distribution (Discrete)
The binomial distribution models the number of successes in a fixed number of independent trials, each with the same probability of success.
* $n$: Number of trials.
* $p$: Probability of success on a single trial.

Examples: Flipping a coin 10 times, counting how many times an ad is clicked out of 100 views.

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Simulate 1000 experiments. 
# Each experiment is flipping a fair coin (p=0.5) 10 times (n=10).
n = 10
p = 0.5
size = 1000

# Draw samples from a binomial distribution
samples = np.random.binomial(n, p, size)

# The mean of our samples should be close to the expected value: n * p = 5
print(f"Mean number of successes: {np.mean(samples)}")

# Visualize the distribution
sns.histplot(samples, discrete=True, stat='probability')
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.show()
```

### The Normal (Gaussian) Distribution (Continuous)
The famous "bell curve." It is defined by its mean ($\mu$) and standard deviation ($\sigma$). Many natural phenomena (height, test scores) follow a normal distribution.

```python
# Draw samples from a normal distribution
# mean = 0, std = 1, size = 1000
normal_samples = np.random.normal(0, 1, 1000)
```

---

## 3. Reference Documentation
* [Numpy random.binomial](https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html)
* [Probability distribution (Wikipedia)](https://en.wikipedia.org/wiki/Probability_distribution)
