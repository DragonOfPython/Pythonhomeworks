class BookNotFoundException(Exception):
    """Exception raised when a book is not found in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Exception raised when a book is already borrowed."""
    pass

class MemberLimitExceededException(Exception):
    """Exception raised when a member tries to borrow more than allowed books."""
    pass

from dataclasses import dataclass, field
from typing import Dict, Set

@dataclass(frozen=True)  # Make Book instances immutable
class Book:
    title: str
    author: str
    is_borrowed: bool = field(default=False)

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Borrowed' if self.is_borrowed else 'Available'}"

@dataclass
class Member:
    name: str
    borrowed_books: Set[Book] = field(default_factory=set)  # Use a set for faster membership checks
    MAX_BORROW_LIMIT: int = 3

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) >= self.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(f"{self.name} has exceeded the borrowing limit of {self.MAX_BORROW_LIMIT} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.add(book)
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} cannot return '{book.title}' as it was not borrowed.")

class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}

    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.books[title] = book
        print(f"Added book: {book}")

    def add_member(self, name: str):
        member = Member(name)
        self.members[name] = member
        print(f"Added member: {member.name}")

    def borrow_book(self, member_name: str, book_title: str):
        member = self.members.get(member_name)
        book = self.books.get(book_title)

        if book is None:
            raise BookNotFoundException(f"The book '{book_title}' does not exist in the library.")
        
        if member is None:
            print(f"No member found with the name '{member_name}'.")
            return

        member.borrow_book(book)

    def return_book(self, member_name: str, book_title: str):
        member = self.members.get(member_name)
        book = self.books.get(book_title)

        if member is None:
            print(f"No member found with the name '{member_name}'.")
            return

        if book is None:
            print(f"The book '{book_title}' does not exist in the library.")
            return

        member.return_book(book)

# Example Usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book("1984", "George Orwell")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")

    # Adding members
    library.add_member("Alice")
    library.add_member("Bob")

    # Borrowing books
    try:
        library.borrow_book("Alice", "1984")
        library.borrow_book("Alice", "1984")  # Should raise BookAlreadyBorrowedException
    except Exception as e:
        print(e)

    try:
        library.borrow_book("Bob", "The Great Gatsby")
        library.borrow_book("Bob", "To Kill a Mockingbird")
        library.borrow_book("Bob", "Moby Dick")  # Should raise BookNotFoundException
    except Exception as e:
        print(e)

    try:
        library.borrow_book("Bob", "To Kill a Mockingbird")
        library.borrow_book("Bob", "1984")  # Should raise MemberLimitExceededException
    except Exception as e:
        print(e)

    # Returning books
    library.return_book("Alice", "1984")
    library.return_book("Alice", "The Great Gatsby")  # Should indicate it was not borrowed