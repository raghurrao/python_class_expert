# Day 14 Assignment: Iterables & Callables
# ----------------------------------------------------------------------
# Instructions: Complete the Fibonacci and CallableAccumulator classes.
# Run 'python day14_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Fibonacci Iterator
# ======================================================================
class Fibonacci:
    """
    Requirements:
    1. Constructor accepts integer 'limit' (the total terms to yield).
    2. Implement '__iter__(self)' that returns the iterator itself.
    3. Implement '__next__(self)' to return the next Fibonacci number:
       - Starting with 0, then 1, 1, 2, 3, 5, 8, 13, etc.
       - Raise StopIteration when 'limit' terms have been generated.
    """
    def __init__(self, limit):
        # TODO: Initialize count, limit, and fibonacci state trackers
        pass

    def __iter__(self):
        # TODO: Return iterator object
        pass

    def __next__(self):
        # TODO: Calculate and return next Fibonacci term, or raise StopIteration
        pass


# ======================================================================
# Exercise 2: Stateful Callable Accumulator
# ======================================================================
class CallableAccumulator:
    """
    Requirements:
    1. Constructor accepts optional 'initial_value' (defaulting to 0).
    2. Store inside 'self.value'.
    3. Implement '__call__(self, amount)' to add 'amount' to 'self.value',
       save the sum, and return the new total.
    """
    # TODO: Implement constructor and __call__ method
    pass
