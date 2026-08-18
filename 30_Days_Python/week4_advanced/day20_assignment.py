# Day 20 Assignment: Unit Testing Target Functions
# ----------------------------------------------------------------------
# Note: These functions are already fully implemented for you.
# Your assignment today is to write the unit tests for them in 'day20_test.py'.

def calculate_statistics(numbers):
    """
    Calculates summary metrics of a list of numbers.
    Returns a dictionary with sum, mean, max, and min.
    Raises ValueError if the input list is empty.
    """
    if not numbers:
        raise ValueError("List cannot be empty")
        
    return {
        'sum': sum(numbers),
        'mean': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers)
    }


def is_palindrome(s):
    """
    Returns True if string s is a palindrome, False otherwise.
    Ignores whitespace and case differences.
    """
    # Clean the string: remove spaces and lowercase
    cleaned = "".join(s.split()).lower()
    return cleaned == cleaned[::-1]
