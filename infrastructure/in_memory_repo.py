from interfaces.book_repository import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = {}

    def add(self, book):
        self.books[book.id] = book

    def get_all(self):
        return list(self.books.values())

    def get_by_id(self, book_id):
        return self.books.get(book_id)

    def update(self, book):
        if book.id in self.books:
            self.books[book.id] = book

    def delete(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
