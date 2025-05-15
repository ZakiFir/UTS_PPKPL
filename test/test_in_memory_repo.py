import unittest
from entities.book import Book
from infrastructure.in_memory_repo import InMemoryBookRepository

class TestInMemoryBookRepository(unittest.TestCase):  
    def setUp(self):
        self.repo = InMemoryBookRepository()

    def test_add_book(self):
        book = Book(1, "Python Dasar", "Andi", 2023, 10)
        self.repo.add(book)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(self.repo.get_by_id(1).title, "Python Dasar")
        self.assertEqual(self.repo.get_by_id(1).author, "Andi")

    def test_get_all_books(self):
        book1 = Book(1, "Python Dasar", "Andi", 2023, 10)
        book2 = Book(2, "Flask Web", "Citra", 2021, 8)
        self.repo.add(book1)
        self.repo.add(book2)
        books = self.repo.get_all()
        self.assertEqual(len(books), 2)
        self.assertEqual(books[0].title, "Python Dasar")
        self.assertEqual(books[1].title, "Flask Web")
        self.assertEqual(books[0].author, "Andi")

    def test_get_book_by_id(self):
        book = Book(1, "Python Dasar", "Andi", 2023, 10)
        self.repo.add(book)
        fetched_book = self.repo.get_by_id(1)
        self.assertEqual(fetched_book.title, "Python Dasar")
        self.assertEqual(fetched_book.author, "Andi")
        self.assertEqual(fetched_book.year, 2023)

    def test_update_book(self):
        book = Book(1, "Python Dasar", "Andi", 2023, 10)
        self.repo.add(book)
        updated_book = Book(1, "Python Lanjutan", "Andi", 2023, 5)
        self.repo.update(updated_book)
        fetched_book = self.repo.get_by_id(1)
        self.assertEqual(fetched_book.title, "Python Lanjutan")
        self.assertEqual(fetched_book.stock, 5)
        self.assertEqual(fetched_book.author, "Andi")

    def test_delete_book(self):
        book = Book(1, "Python Dasar", "Andi", 2023, 10)
        self.repo.add(book)
        self.repo.delete(1)
        self.assertIsNone(self.repo.get_by_id(1))
        self.assertEqual(len(self.repo.get_all()), 0)

if __name__ == '__main__':
    unittest.main()