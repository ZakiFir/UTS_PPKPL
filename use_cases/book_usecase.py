from entities.book import Book

class BookUseCase:
    def __init__(self, repo):
        self.repo = repo

    def add_book(self, book):
        self.repo.add(book)

    def list_books(self):
        return self.repo.get_all()

    def get_book(self, book_id):
        return self.repo.get_by_id(book_id)

    def update_book(self, book_id, book_data):
        if self.repo.get_by_id(book_id):
            book = Book(book_id, **book_data)
            self.repo.update(book)
            return book
        return None

    def delete_book(self, book_id):
        self.repo.delete(book_id)

    def create_book(self, book_data):
        book = Book(**book_data)
        self.repo.add(book)
        return book