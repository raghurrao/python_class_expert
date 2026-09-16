# Day 33: Optimization (Gradient Descent)

We know how to calculate a gradient, and we know that it points in the direction of steepest ascent. Now we can finally use it to train a machine learning model using an algorithm called Gradient Descent.

---

## 1. What is Gradient Descent?
Imagine you are blindfolded on a mountain and want to find the lowest valley (the minimum error of your model). You feel the slope of the ground under your feet (the gradient). You take a step downhill (in the *negative* direction of the gradient). You repeat this until the ground is flat (the gradient is zero).

This is exactly how neural networks and many other ML models "learn".

---

## 2. Core Concepts & Operations

### The Learning Rate ($\alpha$)
The learning rate dictates how big of a step you take downhill. 
* If it's too small, you will take millions of tiny steps and training will take forever.
* If it's too large, you might step completely over the valley and bounce up the other side (divergence).

### The Update Rule
For a parameter $x$, the update rule at each step is:
$x_{new} = x_{old} - (\text{learning\_rate} \times \text{gradient})$

```python
def f(x):
    """The loss function we want to minimize: f(x) = (x - 3)^2"""
    # The minimum is obviously at x = 3, where f(x) = 0
    return (x - 3)**2

def gradient_f(x):
    """The analytical derivative: f'(x) = 2(x - 3)"""
    return 2 * (x - 3)

def gradient_descent(start_x, learning_rate, num_iterations):
    x = start_x
    print(f"Starting at x = {x:.4f}")
    
    for i in range(num_iterations):
        # 1. Calculate the gradient at current x
        grad = gradient_f(x)
        
        # 2. Update x by moving in the opposite direction of the gradient
        x = x - (learning_rate * grad)
        
        if (i+1) % 5 == 0:
            print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}")
            
    return x

# Run gradient descent
# Let's start far away at x = -5
final_x = gradient_descent(start_x=-5.0, learning_rate=0.1, num_iterations=30)
print(f"\nFinal optimized x: {final_x:.4f}") # Should be very close to 3.0
```

### Types of Gradient Descent
* **Batch Gradient Descent:** Uses the entire dataset to compute the gradient before taking a step. Slow but stable.
* **Stochastic Gradient Descent (SGD):** Uses a single random data point to compute the gradient. Very fast, but very noisy (bounces around).
* **Mini-batch Gradient Descent:** A compromise. Uses a small batch (e.g., 32 or 64 samples) to compute the gradient. This is what modern deep learning actually uses.

---

## 3. Reference Documentation
* [Gradient descent (Wikipedia)](https://en.wikipedia.org/wiki/Gradient_descent)
* [Optimizers in PyTorch (for context on modern usage)](https://pytorch.org/docs/stable/optim.html)