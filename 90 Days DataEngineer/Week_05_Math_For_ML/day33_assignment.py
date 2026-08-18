def gradient_descent_1d(start_x: float, lr: float, steps: int) -> float:
    """
    Optimize function f(x) = x^2 using Gradient Descent.
    f'(x) = 2 * x
    
    Update step: x_new = x_old - lr * f'(x_old)
    """
    x = start_x
    for _ in range(steps):
        grad = 2 * x
        x = x - lr * grad
    return x