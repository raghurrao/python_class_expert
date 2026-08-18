import scipy.stats as stats
import numpy as np

def run_anova(g1: np.ndarray, g2: np.ndarray, g3: np.ndarray):
    """
    Run a 1-way ANOVA across three groups.
    Return: (f_statistic, p_value)
    """
    f_val, p = stats.f_oneway(g1, g2, g3)
    return float(f_val), float(p)