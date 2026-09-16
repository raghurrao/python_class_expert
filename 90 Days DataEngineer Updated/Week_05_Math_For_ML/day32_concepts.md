# Day 32: Partial Derivatives & Gradients

Machine learning models rarely have just one parameter. They have hundreds, thousands, or billions (like GPT-4). To optimize multi-variable functions, we need partial derivatives and gradients.

---

## 1. What is a Partial Derivative?
When a function has multiple variables, e.g., $f(x, y)$, a partial derivative measures how much the function changes if we change *one* variable (like $x$) while holding all the other variables (like $y$) completely constant.

* Notation: $\frac{\partial f}{\partial x}$ (The partial derivative of $f$ with respect to $x$)

---

## 2. What is a Gradient?
The gradient, denoted by an upside-down triangle $\nabla f$ (nabla), is simply a vector containing all the partial derivatives of a function.

If $f(x, y) = x^2 + y^3$:
* $\frac{\partial f}{\partial x} = 2x$
* $\frac{\partial f}{\partial y} = 3y^2$
* The gradient vector $\nabla f = [2x, 3y^2]$

**The Most Important Property:** The gradient vector at any point always points in the direction of the **steepest ascent** (the fastest way to increase the function's value). Conversely, the negative gradient points in the direction of the **steepest descent** (the fastest way to decrease the function's value).

---

## 3. Core Concepts & Operations

### Numerical Approximation of Gradients
Just as we approximated a single derivative, we can approximate the gradient by taking the partial derivative with respect to each variable sequentially.

```python
import numpy as np

def f(x, y):
    """Our function: f(x, y) = x^2 + 3y^2"""
    return x**2 + 3 * y**2

def numerical_gradient(func, x, y, h=1e-5):
    """Approximates the gradient of a 2D function."""
    
    # Partial derivative with respect to x (hold y constant)
    df_dx = (func(x + h, y) - func(x - h, y)) / (2 * h)
    
    # Partial derivative with respect to y (hold x constant)
    df_dy = (func(x, y + h) - func(x, y - h)) / (2 * h)
    
    return np.array([df_dx, df_dy])

# Evaluate the gradient at point (2.0, 1.0)
point = (2.0, 1.0)
grad = numerical_gradient(f, point[0], point[1])

# Analytical gradient should be [2x, 6y]. At (2,1) this is [4, 6]
print(f"Approximate gradient at {point}: {grad}")
```

In neural networks, this gradient tells us exactly how to adjust every single weight and bias in the network to lower the loss (error) of our predictions.

---

## 4. Reference Documentation
* [Gradient (Wikipedia)](https://en.wikipedia.org/wiki/Gradient)
* [Partial derivative (Wikipedia)](https://en.wikipedia.org/wiki/Partial_derivative)