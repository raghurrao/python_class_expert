# Day 31: Single Variable Calculus & Derivatives

Calculus is the mathematics of continuous change. In machine learning, we use calculus (specifically derivatives) to figure out how to change our model's parameters to make its predictions better.

---

## 1. What is a Derivative?
The derivative of a function $f(x)$ at a specific point $x$ measures the **rate of change** (the slope) of the function at that exact point. 
* If the derivative is positive, the function is going up.
* If the derivative is negative, the function is going down.
* If the derivative is exactly zero, the function is at a flat spot (a local minimum, local maximum, or saddle point).

In machine learning, we define a "Loss Function" that measures how bad our model is. Our goal is to find the parameters where the loss is at a minimum (where the derivative is zero).

---

## 2. Core Concepts & Operations

### Analytical vs Numerical Derivatives
* **Analytical (Symbolic) Derivative:** Finding the exact mathematical formula for the derivative using calculus rules (e.g., if $f(x) = x^2$, then $f'(x) = 2x$).
* **Numerical Derivative:** Approximating the derivative using code by calculating the slope over a very small step $h$.

### Numerical Approximation
The definition of a derivative is the limit as $h$ approaches 0 of:
$f'(x) \approx \frac{f(x + h) - f(x)}{h}$

```python
def f(x):
    """Our function: f(x) = x^2 + 3x + 2"""
    return x**2 + 3*x + 2

def numerical_derivative(func, x, h=1e-5):
    """
    Approximates the derivative of a function at point x.
    Uses the central difference method for better accuracy:
    [f(x+h) - f(x-h)] / 2h
    """
    return (func(x + h) - func(x - h)) / (2 * h)

# Let's find the slope at x = 4
x_val = 4.0
approx_slope = numerical_derivative(f, x_val)

# The analytical derivative is 2x + 3. At x=4, it should be 2(4) + 3 = 11.
print(f"Approximate derivative at x={x_val}: {approx_slope}")
# Output will be very close to 11.0
```

### Why use Numerical Approximation?
While analytical derivatives are exact, some complex functions (like deep neural networks) have derivatives that are difficult to write down by hand. However, modern deep learning frameworks (like PyTorch and TensorFlow) use **Automatic Differentiation (Autograd)**, which calculates exact derivatives under the hood without you needing to do the math manually or rely on slow/imprecise numerical approximation. Numerical differentiation is mostly used to double-check that autograd is working correctly.

---

## 3. Reference Documentation
* [Derivative (Wikipedia)](https://en.wikipedia.org/wiki/Derivative)