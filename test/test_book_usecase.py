import unittest
from entities.book import Book
from use_cases.book_usecase import BookUseCase
from infrastructure.in_memory_repo import InMemoryBookRepository

class TestBookUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryBookRepository()
        self.usecase = BookUseCase(self.repo)
        self.book = Book(1, "Python Dasar", "Andi", 2023, 10)

    def test_add_book(self):
        self.usecase.add_book(self.book)
        self.assertEqual(len(self.usecase.list_books()), 1)

    def test_get_book(self):
        self.usecase.add_book(self.book)
        book = self.usecase.get_book(1)
        self.assertEqual(book.title, "Python Dasar")

    def test_delete_book(self):
        self.usecase.add_book(self.book)
        self.usecase.delete_book(1)
        self.assertIsNone(self.usecase.get_book(1))

    def test_update_book(self):
        self.usecase.add_book(self.book)
        updated_data = {"title": "Python Lanjut", "author": "Andi", "year": 2023, "stock": 10}
        self.usecase.update_book(1, updated_data)
        book = self.usecase.get_book(1)
        self.assertEqual(book.title, "Python Lanjut")

    def test_create_book(self):
        book_data = {"id": 2, "title": "Python Dasar", "author": "Andi", "year": 2023, "stock": 10}
        book = self.usecase.create_book(book_data)
        self.assertEqual(book.title, "Python Dasar")
        self.assertEqual(len(self.usecase.list_books()), 1)

if __name__ == '__main__':
    unittest.main()