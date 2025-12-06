# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor: Initializes a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: User-friendly format."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: Recreates the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage (you can remove this part if you only want the class definition):
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(str(book1))   # Output: 1984 by George Orwell, published in 1949
    print(repr(book1))  # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the book explicitly to trigger __del__
    del book1
