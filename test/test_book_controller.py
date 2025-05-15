import unittest
from infrastructure.book_controller import BookController

class TestBookController(unittest.TestCase):
    def setUp(self):
        # Mock the BookUseCase
        from unittest.mock import MagicMock
        self.mock_usecase = MagicMock()
        self.controller = BookController(self.mock_usecase)

    def test_get_books(self):
        self.mock_usecase.list_books.return_value = []
        result = self.controller.get_books()
        self.assertEqual(result, [])
        self.mock_usecase.list_books.assert_called_once()

    def test_get_book(self):
        self.mock_usecase.get_book.return_value = {"id": 1, "title": "Python Dasar"}
        result = self.controller.get_book(1)
        self.assertEqual(result, {"id": 1, "title": "Python Dasar"})
        self.mock_usecase.get_book.assert_called_once_with(1)

    def test_create_book(self):
        book_data = {"title": "Python Dasar", "author": "Andi", "year": 2023, "stock": 10}
        self.mock_usecase.create_book.return_value = book_data
        result = self.controller.create_book(book_data)
        self.assertEqual(result, book_data)
        self.mock_usecase.create_book.assert_called_once_with(book_data)

    def test_update_book(self):
        book_data = {"title": "Python Dasar", "author": "Andi", "year": 2023, "stock": 10}
        self.mock_usecase.update_book_by_id.return_value = book_data
        result = self.controller.update_book(1, book_data)
        self.assertEqual(result, book_data)
        self.mock_usecase.update_book_by_id.assert_called_once_with(1, book_data)

    def test_delete_book(self):
        self.mock_usecase.delete_book.return_value = None
        result = self.controller.delete_book(1)
        self.assertIsNone(result)
        self.mock_usecase.delete_book.assert_called_once_with(1)

if __name__ == '__main__':
    unittest.main()