import scipy.stats as stats
import numpy as np

def run_chi_square(contingency_table: np.ndarray):
    """
    Run Chi-Square test of independence.
    Return: (chi2_statistic, p_value)
    """
    chi2, p, _, _ = stats.chi2_contingency(contingency_table)
    return float(chi2), float(p)