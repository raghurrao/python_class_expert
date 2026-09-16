# Day 75: Recommender Systems (Item Similarity)

How does Netflix know what movie you want to watch next? How does Amazon suggest items? They use Recommender Systems.

---

## 1. Types of Recommender Systems
1. **Content-Based Filtering:** Recommends items similar to those a user has liked in the past, based on item attributes (e.g., If you watch an Action movie starring Tom Cruise, it recommends other Action movies starring Tom Cruise).
2. **Collaborative Filtering:** Recommends items based on the behavior of *other similar users* (e.g., "Users who bought this also bought...").

### Item-Item Similarity
A core component of many recommender systems is computing how similar two items are. If we have a matrix showing how every user rated every item, we can calculate the similarity between columns (items) using metrics like Cosine Similarity (which we learned in Week 5!).

---

## 2. Core Concepts & Operations

### Recommending based on a Similarity Matrix
If you have already computed an $N \times N$ matrix where `matrix[i, j]` is the similarity between Item $i$ and Item $j$, finding recommendations is as simple as sorting the array!

```python
import numpy as np

# Imagine we have 4 items. We computed their cosine similarity.
# 1.0 means perfectly similar (e.g., an item compared to itself).
# 0.0 means completely dissimilar.
item_similarities = np.array([
    [1.00, 0.85, 0.10, 0.20], # Item 0 similarities
    [0.85, 1.00, 0.15, 0.30], # Item 1 similarities
    [0.10, 0.15, 1.00, 0.90], # Item 2 similarities
    [0.20, 0.30, 0.90, 1.00]  # Item 3 similarities
])

def recommend_similar_items(item_similarities, item_index, top_n=2):
    """Returns the indices of the top N most similar items."""
    # Copy the similarity scores for the target item
    scores = item_similarities[item_index].copy()
    
    # We don't want to recommend the item to itself!
    # Set its similarity to itself to -1 so it falls to the bottom of the list
    scores[item_index] = -1.0
    
    # np.argsort returns indices that would sort the array from lowest to highest.
    # [::-1] reverses it to be highest to lowest.
    # [:top_n] grabs the top N.
    top_indices = np.argsort(scores)[::-1][:top_n]
    
    return top_indices

# Let's say a user is looking at Item 0. What 2 items should we recommend?
target_item = 0
recommended = recommend_similar_items(item_similarities, item_index=target_item, top_n=2)

print(f"Because you looked at Item {target_item}:")
print(f"We recommend Item(s): {recommended}")
# It should recommend Item 1 (score 0.85) and Item 3 (score 0.20)
```

---

## 3. Reference Documentation
* [Recommender system (Wikipedia)](https://en.wikipedia.org/wiki/Recommender_system)
* [Scikit-Learn Cosine Similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)
