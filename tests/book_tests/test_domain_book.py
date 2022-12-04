import unittest

from domain.entities import Book


class TestCasesBookDomain(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_create_book(self):
        book1 = Book(15, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        book2 = Book(21, 'Ulysses', 'James Joyce', 1922, 'Ulysses')
        book3 = Book(23, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'The Great Gatsby')
        self.assertEqual(book1.get_identity(), 15)
        self.assertEqual(book1.get_title(), 'Amintiri din copilarie')

        self.assertEqual(book2.get_author(), 'James Joyce')
        self.assertEqual(book2.get_year(), 1922)
        self.assertEqual(book2.get_volume(), 'Ulysses')

        self.assertEqual(book3.get_year(), 1925)
        self.assertEqual(book3.get_author(), 'F. Scott Fitzgerald')
        self.assertEqual(book3.get_identity(), 23)
