# Week 1 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week1_challenge_test.py
# It will verify if your challenge code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week1_foundations.week1_challenge as challenge
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

# Reset trackers if classes are loaded
if hasattr(challenge, 'Member'):
    challenge.Member.total_members = 0
if hasattr(challenge, 'Library'):
    challenge.Library.library_motto = "Knowledge is Power"

# 1. Book Tests
def test_book():
    assert hasattr(challenge, 'Book'), "Book class not found"
    
    b = challenge.Book("Clean Code", "Robert C. Martin", "9780132350884")
    assert b.title == "Clean Code"
    assert b.author == "Robert C. Martin"
    assert b.isbn == "9780132350884"
    
    # Check encapsulated borrowing state
    assert not hasattr(b, '__is_borrowed'), "Should not expose raw __is_borrowed attribute"
    assert hasattr(b, 'is_borrowed'), "is_borrowed property missing"
    assert b.is_borrowed is False, "Book should not be borrowed initially"
    
    # Borrow book
    b.borrow_book()
    assert b.is_borrowed is True, "Book should be borrowed"
    
    # Try borrowing again
    try:
        b.borrow_book()
        raise AssertionError("Borrowing already borrowed book should raise ValueError")
    except ValueError:
        pass
        
    # Return book
    b.return_book()
    assert b.is_borrowed is False, "Book should be returned"
    
    # Try returning again
    try:
        b.return_book()
        raise AssertionError("Returning an unborrowed book should raise ValueError")
    except ValueError:
        pass

run_test("Challenge - Book class requirements", test_book)

# 2. Member Tests
def test_member():
    assert hasattr(challenge, 'Member'), "Member class not found"
    
    m1 = challenge.Member("Alice", "M001")
    assert m1.name == "Alice"
    assert m1.member_id == "M001"
    assert m1.borrowed_books == []
    assert challenge.Member.total_members == 1, f"Expected 1 member, got {challenge.Member.total_members}"
    
    m2 = challenge.Member("Bob", "M002")
    assert challenge.Member.total_members == 2
    
    b = challenge.Book("Clean Code", "Robert C. Martin", "9780132350884")
    
    # Member borrows book
    m1.borrow_book(b)
    assert b.is_borrowed is True
    assert b in m1.borrowed_books
    
    # Try letting Bob borrow it too (should fail because book is already borrowed)
    try:
        m2.borrow_book(b)
        raise AssertionError("Bob should not be able to borrow Alice's book")
    except ValueError:
        pass
        
    # Alice returns it
    m1.return_book(b)
    assert b.is_borrowed is False
    assert b not in m1.borrowed_books

run_test("Challenge - Member class requirements and member counter", test_member)

# 3. Library Tests
def test_library():
    assert hasattr(challenge, 'Library'), "Library class not found"
    assert challenge.Library.library_motto == "Knowledge is Power"
    
    lib = challenge.Library("City Library")
    assert lib.name == "City Library"
    assert lib.books == []
    
    b1 = challenge.Book("Book 1", "Author 1", "1234567890123")
    b2 = challenge.Book("Book 2", "Author 2", "1234567890124")
    
    lib.add_book(b1)
    lib.add_book(b2)
    assert lib.books == [b1, b2]
    assert lib.available_books_count == 2
    
    # Borrow one book
    b1.borrow_book()
    assert lib.available_books_count == 1, f"Expected 1 available book, got {lib.available_books_count}"
    
    # Test classmethod motto updates
    assert hasattr(challenge.Library, 'update_motto'), "update_motto classmethod missing"
    challenge.Library.update_motto("Read and Grow")
    assert challenge.Library.library_motto == "Read and Grow"
    
    # Test staticmethod isbn validator
    assert hasattr(challenge.Library, 'is_valid_isbn'), "is_valid_isbn staticmethod missing"
    assert challenge.Library.is_valid_isbn("9780132350884") is True
    assert challenge.Library.is_valid_isbn("12345") is False
    assert challenge.Library.is_valid_isbn(9780132350884) is False, "Should fail non-strings"
    assert challenge.Library.is_valid_isbn("abcde12345678") is False, "Should fail non-numeric strings"

run_test("Challenge - Library management metrics, classmethods, and staticmethods", test_library)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 1 Challenge.")
    print(f"You have fully mastered Week 1 foundations!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in week1_challenge.py")
