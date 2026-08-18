def numerical_derivative(func, x: float, h: float = 1e-5) -> float:
    """
    Compute the numerical derivative of a single variable function at x.
    Formula: f'(x) approx (f(x + h) - f(x - h)) / (2 * h)
    """
    return (func(x + h) - func(x - h)) / (2.0 * h)