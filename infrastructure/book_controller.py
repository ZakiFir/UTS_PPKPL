class BookController:
    def __init__(self, book_usecase):
        self.book_service = book_usecase

    def get_books(self):
        return self.book_service.list_books()

    def get_book(self, book_id):
        return self.book_service.get_book(book_id)

    def create_book(self, book_data):
        return self.book_service.create_book(book_data)

    def update_book(self, book_id, book_data):
        return self.book_service.update_book_by_id(book_id, book_data)

    def delete_book(self, book_id):
        return self.book_service.delete_book(book_id)