import scipy.stats as stats
import numpy as np

def compute_confidence_interval(data: np.ndarray, confidence: float = 0.95):
    """
    Compute the confidence interval for the mean of data (t-distribution).
    Return tuple: (mean, lower_bound, upper_bound)
    """
    n = len(data)
    mean = np.mean(data)
    sem = stats.sem(data)
    margin = sem * stats.t.ppf((1 + confidence) / 2., n-1)
    return mean, mean - margin, mean + margin