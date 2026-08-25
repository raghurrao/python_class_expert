# Day 12: Math Utility

def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
