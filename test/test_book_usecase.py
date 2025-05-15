import unittest
from entities.book import Book
from use_cases.book_usecase import BookUseCase
from infrastructure.in_memory_repo import InMemoryBookRepository

class TestBookUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryBookRepository()
        self.usecase = BookUseCase(self.repo)

    # ---------------------------
    # Test Add Book
    # ---------------------------
    def test_add_book_success(self):
        book = Book(1, "Python Dasar", "Andi", 2023, 10)
        self.usecase.add_book(book)
        self.assertEqual(len(self.usecase.list_books()), 1)

    def test_add_book_duplicate_id(self):
        book1 = Book(1, "Python Dasar", "Andi", 2023, 10)
        book2 = Book(1, "Python Lanjutan", "Budi", 2024, 5)
        self.usecase.add_book(book1)
        self.usecase.add_book(book2)
        self.assertEqual(self.usecase.get_book(1).title, "Python Lanjutan")

    def test_add_multiple_books(self):
        for i in range(3):
            self.usecase.add_book(Book(i, f"Book {i}", "Author", 2022, 5))
        self.assertEqual(len(self.usecase.list_books()), 3)

    # ---------------------------
    # Test Get Book
    # ---------------------------
    def test_get_book_existing(self):
        book = Book(2, "Flask Web", "Citra", 2021, 8)
        self.usecase.add_book(book)
        fetched = self.usecase.get_book(2)
        self.assertEqual(fetched.title, "Flask Web")

    def test_get_book_not_exist(self):
        self.assertIsNone(self.usecase.get_book(999))

    def test_get_book_after_delete(self):
        book = Book(3, "Machine Learning", "Dina", 2020, 4)
        self.usecase.add_book(book)
        self.usecase.delete_book(3)
        self.assertIsNone(self.usecase.get_book(3))

    # ---------------------------
    # Test Delete Book
    # ---------------------------
    def test_delete_book_success(self):
        book = Book(4, "AI 101", "Eko", 2023, 7)
        self.usecase.add_book(book)
        self.usecase.delete_book(4)
        self.assertEqual(len(self.usecase.list_books()), 0)

    def test_delete_book_not_exist(self):
        self.usecase.delete_book(404)  # Tidak error meskipun tidak ada
        self.assertEqual(len(self.usecase.list_books()), 0)

    def test_delete_and_readd_same_id(self):
        book = Book(5, "Re-add", "Fajar", 2022, 6)
        self.usecase.add_book(book)
        self.usecase.delete_book(5)
        self.usecase.add_book(Book(5, "Re-add 2", "Gina", 2023, 3))
        self.assertEqual(self.usecase.get_book(5).title, "Re-add 2")

    # ---------------------------
    # Test Update Book
    # ---------------------------
    def test_update_book_success(self):
        book = Book(6, "Old Title", "Hani", 2020, 2)
        self.usecase.add_book(book)
        updated_book = Book(6, "New Title", "Hani", 2020, 2)
        self.usecase.update_book(updated_book)
        self.assertEqual(self.usecase.get_book(6).title, "New Title")

    def test_update_book_not_exist(self):
        book = Book(7, "Not Found", "Ira", 2019, 1)
        self.usecase.update_book(book)  # Tidak menambahkan karena belum ada
        self.assertIsNone(self.usecase.get_book(7))


    def test_update_with_different_data(self):
        book = Book(8, "First", "Joko", 2021, 10)
        self.usecase.add_book(book)
        self.usecase.update_book(Book(8, "Updated", "Joko", 2021, 5))
        self.assertEqual(self.usecase.get_book(8).stock, 5)

    # ---------------------------
    # Test List Books
    # ---------------------------
    def test_list_books_empty(self):
        self.assertEqual(len(self.usecase.list_books()), 0)

    def test_list_books_after_add(self):
        self.usecase.add_book(Book(9, "One", "Lina", 2022, 1))
        books = self.usecase.list_books()
        self.assertEqual(len(books), 1)

    def test_list_books_multiple(self):
        self.usecase.add_book(Book(10, "A", "X", 2020, 1))
        self.usecase.add_book(Book(11, "B", "Y", 2021, 2))
        self.usecase.add_book(Book(12, "C", "Z", 2022, 3))
        self.assertEqual(len(self.usecase.list_books()), 3)

if __name__ == '__main__':
    unittest.main()
