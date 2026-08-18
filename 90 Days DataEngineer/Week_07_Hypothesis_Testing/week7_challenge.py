import numpy as np
import scipy.stats as stats

def run_conversion_experiment(clicks_a: int, n_a: int, clicks_b: int, n_b: int):
    """
    Test conversion rate significance using proportions z-test logic or t-test proxy.
    Here we build contingency table and run Chi-Square test.
    Returns: (conversions_a, conversions_b, p_value)
    """
    con_a = clicks_a / n_a
    con_b = clicks_b / n_b
    table = np.array([
        [clicks_a, n_a - clicks_a],
        [clicks_b, n_b - clicks_b]
    ])
    _, p, _, _ = stats.chi2_contingency(table)
    return con_a, con_b, float(p)