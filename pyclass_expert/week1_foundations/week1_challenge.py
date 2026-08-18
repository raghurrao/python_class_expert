# Week 1 Challenge: Automated Library System
# ----------------------------------------------------------------------
# Instructions: Integrate all concepts from Days 1-5 to build a mini Library System.
# Follow the class definitions and requirements exactly.
# Run 'python week1_challenge_test.py' to verify your solution.

class Book:
    """
    Represents a library book.
    Requirements:
    1. Constructor should take 'title' (str), 'author' (str), and 'isbn' (str).
    2. Store a private attribute '__is_borrowed' initialized to False.
    3. Implement a read-only property 'is_borrowed' to expose '__is_borrowed'.
    4. Implement 'borrow_book(self)':
       - If '__is_borrowed' is already True, raise a ValueError("Book is already borrowed").
       - Otherwise, set '__is_borrowed' to True.
    5. Implement 'return_book(self)':
       - If '__is_borrowed' is False, raise a ValueError("Book was not borrowed").
       - Otherwise, set '__is_borrowed' to False.
    """
    # TODO: Implement Book class


class Member:
    """
    Represents a library member.
    Requirements:
    1. Class attribute 'total_members' initialized to 0.
    2. Constructor should take 'name' (str) and 'member_id' (str).
    3. In the constructor, initialize 'borrowed_books' as an empty list (to hold Book objects),
       and increment 'total_members' class attribute.
    4. Implement 'borrow_book(self, book)':
       - Attempt to borrow the book by calling book.borrow_book().
       - If successful, append the book object to 'self.borrowed_books'.
    5. Implement 'return_book(self, book)':
       - Attempt to return the book by calling book.return_book().
       - If successful, remove the book object from 'self.borrowed_books'.
    """
    # TODO: Implement Member class


class Library:
    """
    Represents a Library facility.
    Requirements:
    1. Class attribute 'library_motto' set to "Knowledge is Power".
    2. Constructor should take 'name' (str) and initialize:
       - 'self.name' = name
       - 'self.books' = empty list (to store Book objects)
    3. Implement 'add_book(self, book)':
       - Add the book object to 'self.books'.
    4. Implement a read-only property 'available_books_count':
       - Count and return the number of books in 'self.books' where 'is_borrowed' is False.
    5. Implement a class method 'update_motto(cls, new_motto)':
       - Update the class attribute 'library_motto' to 'new_motto' globally.
    6. Implement a static method 'is_valid_isbn(isbn)':
       - Returns True if isbn is a string, is numeric, and has a length of exactly 13 digits.
       - Returns False otherwise.
    """
    # TODO: Implement Library class
