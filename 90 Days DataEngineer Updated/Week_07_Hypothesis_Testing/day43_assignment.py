import scipy.stats as stats
import numpy as np

def run_t_test(group_a: np.ndarray, group_b: np.ndarray):
    """
    Run an independent 2-sample T-test (equal variance).
    Return: (t_statistic, p_value)
    """
    stat, p = stats.ttest_ind(group_a, group_b, equal_var=True)
    return float(stat), float(p)