# Day 38: The Central Limit Theorem (CLT)

The Central Limit Theorem is arguably the most important theorem in all of statistics. It explains why the normal distribution is so ubiquitous and allows us to make inferences about a population even when we don't know its underlying distribution.

---

## 1. What is the CLT?
The Central Limit Theorem states that if you take sufficiently large random samples from *any* population with a defined mean and variance, the **distribution of the sample means** will approximate a **normal distribution**, regardless of the shape of the original population's distribution.

In simpler terms: Take a bunch of samples, calculate their averages. Plot those averages. The plot will look like a bell curve, even if the original data looked nothing like a bell curve.

---

## 2. Core Concepts & Operations

### Simulating the CLT in Python
Let's prove the CLT works using code. We'll start with a heavily skewed, non-normal distribution (an Exponential distribution), take many samples, calculate their means, and plot the distribution of those means.

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Create a non-normal population (Exponential distribution)
population = np.random.exponential(scale=2.0, size=10000)
pop_mean = np.mean(population)

# 2. Function to draw samples and calculate their means
def simulate_clt(population, sample_size, num_samples):
    sample_means = []
    for _ in range(num_samples):
        # Draw a random sample with replacement
        sample = np.random.choice(population, size=sample_size)
        sample_means.append(np.mean(sample))
    return np.array(sample_means)

# 3. Run the simulation
# Take 1000 samples, each of size 50
means = simulate_clt(population, sample_size=50, num_samples=1000)

# 4. Visualize
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Plot the original skewed population
sns.histplot(population, ax=axes[0])
axes[0].set_title('Original Population (Exponential, Non-Normal)')

# Plot the distribution of the sample means
sns.histplot(means, kde=True, ax=axes[1])
axes[1].set_title('Distribution of Sample Means (Normal!)')
axes[1].axvline(pop_mean, color='red', linestyle='--', label='Population Mean')
axes[1].legend()

plt.show()
```

### Why is this useful?
Because the sample means are normally distributed, we can use the mathematical properties of the normal distribution (like calculating standard errors and confidence intervals) to estimate the true population mean, even if we only have one sample!

---

## 3. Reference Documentation
* [Central Limit Theorem (Wikipedia)](https://en.wikipedia.org/wiki/Central_limit_theorem)
