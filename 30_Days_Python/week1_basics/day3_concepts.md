# Day 3: Control Flow (Conditions & Loops)

Control flow is how a program decides which path of code to run. In Python, this is handled through conditionals (`if-elif-else`) and loops (`for` and `while`).

---

## 1. Conditionals (`if-elif-else`)

Python uses the keywords `if`, `elif` (short for else-if), and `else` to perform conditional logic. 

> [!IMPORTANT]
> Python uses **indentation** (typically 4 spaces) to define code blocks. There are no curly braces `{}` like in C, Java, or JavaScript.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # This block will run
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### Logical Operators
You can combine multiple conditions using logical operators:
*   `and`: Returns `True` if both conditions are true. (e.g. `age > 18 and age < 65`)
*   `or`: Returns `True` if at least one condition is true. (e.g. `is_weekend or is_holiday`)
*   `not`: Reverses the boolean value. (e.g. `not is_raining`)

---

## 2. Loops

Loops let you repeat a block of code multiple times.

### For Loops
`for` loops in Python are designed to iterate over items of a sequence (like a string, list, tuple, or a range).

The `range()` function generates a sequence of numbers.
*   `range(5)` generates `0, 1, 2, 3, 4` (starts at 0, goes up to but does not include 5)
*   `range(1, 6)` generates `1, 2, 3, 4, 5` (starts at 1, goes up to but does not include 6)
*   `range(1, 10, 2)` generates `1, 3, 5, 7, 9` (starts at 1, increments by 2)

```python
for i in range(3):
    print(f"Iteration {i}")
```

### While Loops
`while` loops repeat a block of code as long as a condition remains `True`.

```python
count = 1
while count <= 3:
    print(count)
    count += 1
```

---

## 3. Loop Control Statements

Sometimes you need to alter the flow of a loop:
*   `break`: Exits the loop immediately.
*   `continue`: Skips the rest of the current iteration and jumps to the next iteration.
*   `pass`: A null statement used as a placeholder (does nothing, prevents syntax errors in empty blocks).

```python
for num in range(1, 10):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num == 7:
        break     # Stop loop when num reaches 7
    print(num)    # Output: 1, 3, 5
```

---

Now, proceed to the Day 3 Assignment: [day3_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week1_basics/day3_assignment.py).
