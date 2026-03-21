class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        return f"'{self.title}' by {self.author} — Available: {self.is_available}"

    def checkout(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True


class Library:                          # ✅ no inheritance from Book
    def __init__(self, name):
        self.name = name
        self.books = []                 # ✅ fresh empty list

    def add_book(self, book):
        self.books.append(book)         # ✅ append, not replace

    def show_books(self):
        print(f"\n{self.name} — Book List:")
        for book in self.books:
            print(f"  {book}")          # calls __str__ on each Book

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print(f"'{title}' not found.")
        return None


lib = Library("City Library")

b1 = Book("Atomic Habits", "James Clear")
b2 = Book("Deep Work", "Cal Newport")
b3 = Book("Python Crash Course", "Eric Matthes")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

lib.show_books()

b1.checkout()
lib.show_books()

found = lib.find_book("Deep Work")
print(found)