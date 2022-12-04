import unittest

from domain.entities import Book
from repository.repository_book import BookRepository


class TestCasesBookRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = BookRepository()

    def test_add_book_to_list(self):
        self.assertFalse(self._repo.get_book_list())

        book1 = Book(15, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        self._repo.add_book_to_list(book1)
        self.assertEqual(len(self._repo.get_book_list()), 1)

        book2 = Book(12, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881, 'Basme din popor')
        self._repo.add_book_to_list(book2)
        self.assertEqual(len(self._repo.get_book_list()), 2)

    def test_search_book_by_id(self):
        self.assertRaises(ValueError, self._repo.search_book_by_id, 1)

        book = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        self._repo.add_book_to_list(book)
        self.assertEqual(self._repo.search_book_by_id(book.get_identity()), book)

        self.assertRaises(ValueError, self._repo.search_book_by_id, 2)
        self.assertRaises(ValueError, self._repo.search_book_by_id, 3)

    def test_modify_book(self):
        book1 = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        book2 = Book(2, 'Povestea lui Harap-Alb', 'Ion Creanga', 1882, 'Povestea lui Harap-Alb')
        self._repo.add_book_to_list(book1)
        self._repo.add_book_to_list(book2)

        self.assertEqual(book1.get_title(), 'Amintiri din copilarie')
        self.assertEqual(book1.get_author(), 'Ion Creanga')
        self.assertEqual(book1.get_year(), 1892)
        self.assertEqual(book1.get_volume(), 'Amintiri din copilarie')

        self._repo.modify_book(book1, 'Ulysses', 'James Grant', 1922, 'Ulysses')
        self.assertEqual(book1.get_title(), 'Ulysses')
        self.assertEqual(book1.get_author(), 'James Grant')
        self.assertEqual(int(book1.get_year()), 1922)
        self.assertEqual(book1.get_volume(), 'Ulysses')

        self.assertEqual(book2.get_title(), 'Povestea lui Harap-Alb')
        self.assertEqual(book2.get_author(), 'Ion Creanga')
        self.assertEqual(book2.get_year(), 1882)
        self.assertEqual(book2.get_volume(), 'Povestea lui Harap-Alb')

        self._repo.modify_book(book2, 'Amintiri din copilarie', 'Mihai Eminescu', 1900, 'Povestea unui om lenes')
        self.assertEqual(book2.get_title(), 'Amintiri din copilarie')
        self.assertEqual(book2.get_author(), 'Mihai Eminescu')
        self.assertEqual(book2.get_year(), 1900)
        self.assertEqual(book2.get_volume(), 'Povestea unui om lenes')

    def test_delete_book(self):
        self.assertFalse(self._repo.get_book_list())
        book1 = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        book2 = Book(2, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881, 'Povestea lui Harap-Alb')

        self._repo.add_book_to_list(book1)
        self._repo.add_book_to_list(book2)
        self.assertEqual(len(self._repo.get_book_list()), 2)

        self._repo.delete_book(book1)
        self.assertEqual(len(self._repo.get_book_list()), 1)

        self._repo.delete_book(book2)
        self.assertFalse(self._repo.get_book_list())
