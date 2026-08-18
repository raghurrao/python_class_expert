# Day 20 Assignment: Writing Unit Tests
# ----------------------------------------------------------------------
# Instructions: Complete the test cases below by replacing the # TODO placeholders
# with actual assertions. You can run 'python day20_test.py' to run your tests.
# The verification checker will run your tests and confirm they cover all cases!

import unittest
import os
import sys

# Ensure parent directory is in sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import week4_advanced.day20_assignment as assignment

# ======================================================================
# Exercise 1: Test Calculate Statistics
# ======================================================================
class TestCalculateStatistics(unittest.TestCase):

    def test_valid_numbers(self):
        # Task: Test calculate_statistics with a list of numbers (e.g. [1, 2, 3, 4])
        # Assert that the returned dictionary matches the expected sum, mean, max, and min.
        # TODO: Implement assertions
        pass

    def test_single_element(self):
        # Task: Test calculate_statistics with a single element list (e.g. [5])
        # TODO: Implement assertions
        pass

    def test_empty_list_raises_error(self):
        # Task: Test that passing an empty list raises a ValueError.
        # Hint: Use self.assertRaises(ValueError)
        # TODO: Implement assertions
        pass


# ======================================================================
# Exercise 2: Test Palindrome Checker
# ======================================================================
class TestIsPalindrome(unittest.TestCase):

    def test_simple_palindrome(self):
        # Task: Assert that "radar" is recognized as a palindrome
        # TODO: Implement assertions
        pass

    def test_palindrome_with_spaces_and_casing(self):
        # Task: Assert that "Race Car" is recognized as a palindrome
        # TODO: Implement assertions
        pass

    def test_non_palindrome(self):
        # Task: Assert that "hello" is NOT recognized as a palindrome
        # TODO: Implement assertions
        pass

    def test_empty_string(self):
        # Task: Assert that an empty string "" is recognized as a palindrome
        # TODO: Implement assertions
        pass


if __name__ == '__main__':
    unittest.main()
