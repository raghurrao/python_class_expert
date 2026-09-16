import numpy as np

def simulate_binomial(n: int, p: float, size: int) -> float:
    """
    Simulate a Binomial process (e.g. coin tosses) and return the mean number of successes.
    """
    samples = np.random.binomial(n, p, size)
    return float(np.mean(samples))