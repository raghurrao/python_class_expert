# Day 4: Sequences (Lists & Tuples)

In Python, sequences are ordered collections of items. The two most common sequence types are **Lists** and **Tuples**.

---

## 1. Lists vs. Tuples

| Feature | List | Tuple |
| :--- | :--- | :--- |
| **Mutability** | **Mutable** (can be changed after creation) | **Immutable** (cannot be changed after creation) |
| **Syntax** | Square brackets: `my_list = [1, 2, 3]` | Parentheses: `my_tuple = (1, 2, 3)` |
| **Performance** | Slightly slower, requires more memory | Faster, memory-efficient |
| **Use Case** | Collections of items that can grow/shrink | Fixed records (e.g. coordinates: `(latitude, longitude)`) |

---

## 2. Indexing & Slicing

Python uses 0-based indexing. You can access elements from the start or end (using negative indices).

```python
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])   # Output: apple
print(fruits[-1])  # Output: date (last element)
print(fruits[-2])  # Output: cherry (second to last)
```

### Slicing Syntax: `sequence[start:stop:step]`
*   `start`: Index to begin slice (inclusive). Default is 0.
*   `stop`: Index to end slice (exclusive). Default is end of sequence.
*   `step`: Increments between elements. Default is 1.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])    # Output: [2, 3, 4, 5] (indices 2 to 5)
print(numbers[:4])     # Output: [0, 1, 2, 3] (from beginning to index 3)
print(numbers[5:])     # Output: [5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[::2])    # Output: [0, 2, 4, 6, 8] (every second element)
print(numbers[::-1])   # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse list!)
```

---

## 3. Useful List Methods

Here are the most common methods to modify lists:
*   `list.append(item)`: Adds an item to the end of the list.
*   `list.insert(index, item)`: Inserts an item at a specific index.
*   `list.remove(item)`: Removes the first occurrence of an item. Raises `ValueError` if not found.
*   `list.pop(index)`: Removes and returns the item at `index` (defaults to the last item).
*   `list.sort()`: Sorts the list in-place (mutates original list).
*   `len(list)`: Built-in function that returns the number of elements in the list.

```python
tasks = ["wash dishes", "buy groceries"]
tasks.append("clean room")
tasks.sort()
print(tasks)  # Output: ['buy groceries', 'clean room', 'wash dishes']
```

---

## 4. Sequence Unpacking

You can assign elements of a list or tuple to individual variables in a single line.

```python
point = (10, 20)
x, y = point  # x = 10, y = 20
```

---

Now, proceed to the Day 4 Assignment: [day4_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week1_basics/day4_assignment.py).
