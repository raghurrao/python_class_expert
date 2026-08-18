from statsmodels.stats.power import TTestIndPower

def calculate_required_sample_size(effect_size: float, alpha: float, power: float) -> int:
    """
    Calculate the required sample size per group for a two-sample t-test.
    """
    analysis = TTestIndPower()
    size = analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative='two-sided')
    return int(round(size))