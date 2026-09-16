# Day 71: PyTorch Tensors

Welcome to the world of Deep Learning! While libraries like `scikit-learn` are great for traditional machine learning (Random Forests, Logistic Regression), deep learning (Neural Networks) requires massive parallel computation. To achieve this, we use specialized libraries like **PyTorch**.

---

## 1. What is a Tensor?
A Tensor is simply a multi-dimensional array, exactly like a NumPy array. 
* 0D Tensor: Scalar (a single number)
* 1D Tensor: Vector
* 2D Tensor: Matrix
* 3D+ Tensor: N-Dimensional Tensor

### If they are just NumPy arrays, why do we need them?
1. **GPU Acceleration:** NumPy arrays can only run on your CPU. PyTorch Tensors can be seamlessly moved to a GPU (Graphics Processing Unit), which can perform matrix multiplications thousands of times faster.
2. **Automatic Differentiation (Autograd):** PyTorch tensors keep track of the operations performed on them. When it's time to do Gradient Descent, PyTorch calculates the derivatives automatically!

---

## 2. Core Concepts & Operations

### Creating and Using Tensors

```python
import torch
import numpy as np

# 1. Create from a Python list
t_from_list = torch.tensor([[1, 2], [3, 4]])

# 2. Create from a NumPy array (They share the same underlying memory!)
np_array = np.array([5, 6, 7])
t_from_numpy = torch.from_numpy(np_array)

# 3. Create a tensor of zeros, ones, or random numbers
t_zeros = torch.zeros(2, 3) # 2 rows, 3 columns
t_rand = torch.rand(2, 2)   # Random numbers between 0 and 1

# 4. Math operations look exactly like NumPy
t_a = torch.tensor([1, 2, 3])
t_b = torch.tensor([4, 5, 6])
t_sum = t_a + t_b
print(f"Sum: {t_sum}")

# 5. Moving a tensor to the GPU (if you have one)
if torch.cuda.is_available():
    t_gpu = t_a.to('cuda')
    print("Moved to GPU!")
```

---

## 3. Reference Documentation
* [PyTorch Tensors Tutorial](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html)