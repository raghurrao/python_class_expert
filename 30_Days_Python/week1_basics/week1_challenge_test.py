# Week 1 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week1_challenge_test.py
# It will verify if your challenge solutions are correct!

import sys
import os

# Ensure the parent directory is in sys.path to support imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import week1_basics.week1_challenge as challenge
except ImportError as e:
    print(f"[FAIL] Could not import week1_challenge.py. Error: {e}")
    sys.exit(1)

passed_tests = 0
total_tests = 0

def run_test(test_name, test_fn):
    global passed_tests, total_tests
    total_tests += 1
    try:
        test_fn()
        print(f"[PASS] {test_name}")
        passed_tests += 1
    except AssertionError as e:
        print(f"[FAIL] {test_name}")
        print(f"   AssertionError: {e}\n")
    except Exception as e:
        print(f"[FAIL] {test_name}")
        print(f"   Unexpected Error: {type(e).__name__}: {e}\n")

print("Starting Week 1 Challenge Tests...\n")

# 1. Test analyze_text
def test_analyze_text():
    assert hasattr(challenge, 'analyze_text'), "analyze_text not found in week1_challenge.py"
    
    text = "Hello world! Hello Python. Is this a challenge?"
    metrics = challenge.analyze_text(text)
    
    assert isinstance(metrics, dict), f"Expected dict, got {type(metrics).__name__}"
    assert metrics.get('char_count') == len(text), f"Expected char_count to be {len(text)}, got {metrics.get('char_count')}"
    assert metrics.get('word_count') == 8, f"Expected word_count to be 8, got {metrics.get('word_count')}"
    assert metrics.get('sentence_count') == 3, f"Expected sentence_count to be 3 (ends with !, ., ?), got {metrics.get('sentence_count')}"
    
    # Unique words: 'hello', 'world', 'python', 'is', 'this', 'a', 'challenge' -> 7 unique words
    assert metrics.get('unique_word_count') == 7, f"Expected unique_word_count to be 7, got {metrics.get('unique_word_count')}"

run_test("Verify Text Metrics Analyzer outputs", test_analyze_text)

# 2. Test calculate
def test_calculate():
    assert hasattr(challenge, 'calculate'), "calculate not found in week1_challenge.py"
    
    # Regular math ops
    assert challenge.calculate(10, 5, '+') == 15, "Addition failed"
    assert challenge.calculate(10, 5, '-') == 5, "Subtraction failed"
    assert challenge.calculate(10, 5, '*') == 50, "Multiplication failed"
    assert challenge.calculate(10, 5, '/') == 2.0, "Division failed"
    assert challenge.calculate(10, 3, '//') == 3, "Floor division failed"
    assert challenge.calculate(10, 3, '%') == 1, "Modulo failed"
    assert challenge.calculate(2, 3, '**') == 8, "Exponentiation failed"
    
    # Error: Division by zero
    assert challenge.calculate(10, 0, '/') == "Error: Division by zero"
    assert challenge.calculate(10, 0, '//') == "Error: Division by zero"
    assert challenge.calculate(10, 0, '%') == "Error: Division by zero"
    
    # Error: Invalid operator
    assert challenge.calculate(10, 5, 'add') == "Error: Invalid operator"
    assert challenge.calculate(10, 5, '&') == "Error: Invalid operator"

run_test("Verify Advanced Operations Calculator", test_calculate)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 1 Weekend Challenge.")
    print(f"You are now ready to progress to Week 2!")
else:
    print(f"FAILED: Some challenge tests failed. Check the errors above and fix your code in week1_challenge.py")
