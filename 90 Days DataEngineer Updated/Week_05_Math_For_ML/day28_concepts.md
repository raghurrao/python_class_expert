# Day 28: Vectors & Cosine Similarity

Linear algebra is the mathematical foundation of almost all machine learning algorithms. Today we focus on vectors, dot products, and how they can be used to measure similarity.

---

## 1. Why Vectors?
In machine learning, a data point (like an image, a text document, or a customer profile) is represented as a list of numbers—a vector. If we want an AI to understand similarities between documents or images, we need mathematical ways to compare these vectors.

---

## 2. Core Concepts & Operations

### Vectors
A vector is an array of numbers representing a point in space (or a direction and magnitude).

```python
import numpy as np

# A 2D vector
v = np.array([3, 4])
```

### Vector Magnitude (Norm)
The magnitude (or length) of a vector is calculated using the Pythagorean theorem (L2 norm).

```python
# Magnitude of v = sqrt(3^2 + 4^2) = sqrt(25) = 5
magnitude = np.linalg.norm(v)
```

### Dot Product
The dot product is an algebraic operation that takes two equal-length sequences of numbers and returns a single number. It relates to the lengths of the vectors and the cosine of the angle between them.

```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Dot product: (1*4) + (2*5) + (3*6) = 4 + 10 + 18 = 32
dot_prod = np.dot(v1, v2)
```

### Cosine Similarity
Cosine similarity measures the cosine of the angle between two non-zero vectors. 
* **1.0:** Vectors point in the exact same direction (very similar).
* **0.0:** Vectors are orthogonal (perpendicular).
* **-1.0:** Vectors point in exactly opposite directions.

It is heavily used in NLP to compare the similarity of two text documents, because it looks at the *angle* between the vectors rather than their *magnitude* (length).

```python
# Formula: (v1 . v2) / (||v1|| * ||v2||)
v1_norm = np.linalg.norm(v1)
v2_norm = np.linalg.norm(v2)

cos_sim = np.dot(v1, v2) / (v1_norm * v2_norm)
print(f"Cosine Similarity: {cos_sim}")
```

---

## 3. Reference Documentation
* [Numpy linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)
* [Cosine Similarity (Wikipedia)](https://en.wikipedia.org/wiki/Cosine_similarity)
