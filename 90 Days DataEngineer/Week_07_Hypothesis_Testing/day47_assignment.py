import numpy as np

def check_srm(observed_a: int, observed_b: int) -> float:
    """
    Perform a Chi-square goodness-of-fit test to check for Sample Ratio Mismatch (SRM).
    Assuming expected 50/50 allocation split.
    Return p-value.
    """
    import scipy.stats as stats
    total = observed_a + observed_b
    expected = [total / 2.0, total / 2.0]
    _, p = stats.chisquare([observed_a, observed_b], expected)
    return float(p)