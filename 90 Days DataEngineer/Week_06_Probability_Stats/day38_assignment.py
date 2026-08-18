import numpy as np

def simulate_clt(population_mean: float, population_std: float, sample_size: int, num_samples: int) -> np.ndarray:
    """
    Draw 'num_samples' samples of size 'sample_size' from a normal population,
    and return an array of sample means.
    """
    means = []
    for _ in range(num_samples):
        sample = np.random.normal(population_mean, population_std, sample_size)
        means.append(np.mean(sample))
    return np.array(means)