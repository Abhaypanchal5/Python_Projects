class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


b1 = Book("Atomic Habits", "James Clear", 320)
b2 = Book("Atomic Habits", "James Clear", 290)
b3 = Book("Deep Work", "Cal Newport", 296)

print(b1)           # calls __str__
print(len(b1))      # calls __len__
print(b1 == b2)     # calls __eq__ → True (same title & author, different pages)
print(b1 == b3)     # calls __eq__ → False