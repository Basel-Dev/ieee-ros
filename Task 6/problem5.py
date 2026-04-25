class Book:
    def __init__(self, title, author, is_available):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrow_book(self):
        if self.is_available:
            print(f"You have borrowed the book: {self.title}")
            self.is_available = False
        else:
            print("The book is already out")

book = Book("Lord of The Rings", "J. R. R. Tolkien", True)

book.borrow_book()
book.borrow_book()
