import unittest

from domain.entities import Book, Client
from repository.database import DatabaseFile


class TestCasesDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self._database = DatabaseFile("data/database.txt")
        self._database._clear_file()

    def tearDown(self) -> None:
        self._database._clear_file()

    def test_book_in_database(self):
        book = Book(0, "Amintiri din copilarie", "Ion Creanga", 1892, "Amintiri din copilarie")
        self._database.add_book_to_database(book)
        self.assertTrue(self._database.book_in_database(book))

        other_book = Book(1, "Povestea lui Harap-Alb", "Ion Creanga", 1881, "Basme din popor")
        self.assertFalse(self._database.book_in_database(other_book))
        self._database.add_book_to_database(other_book)
        self.assertTrue(self._database.book_in_database(other_book))

    def test_client_in_database(self):
        client = Client("Vasile Pop", 5030102111666, 2016)
        self._database.add_client_to_database(client)
        self.assertTrue(self._database.client_in_database(client))

        other_client = Client("Maria Y", 6010203111555, 2012)
        self.assertFalse(self._database.client_in_database(other_client))
        self._database.add_client_to_database(other_client)
        self.assertTrue(self._database.client_in_database(other_client))

    def test_add_book_to_database(self):
        book = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        self._database.add_book_to_database(book)
        self.assertEqual(len(self._database.get_book_list()), 1)
        self.assertEqual(self._database.get_book_list()[book], 1)
        self.assertRaises(ValueError, self._database.add_book_to_database, book)

    def test_add_client_to_database(self):
        client = Client('Vasile Pop', 5030102111666, 2016)
        self._database.add_client_to_database(client)
        self.assertEqual(len(self._database.get_client_list()), 1)
        self.assertEqual(self._database.get_client_list()[client], 1)
        self.assertRaises(ValueError, self._database.add_client_to_database, client)

    def test_update_no_rentals_book(self):
        book = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        other_book = Book(1, 'Ulysses', 'James Grant', 1922, 'Ulysses')

        self._database.add_book_to_database(book)
        self.assertEqual(len(self._database.get_book_list()), 1)
        self.assertEqual(self._database.get_book_list()[book], 1)
        self._database.update_no_rentals_book(book)
        self.assertEqual(self._database.get_book_list()[book], 2)

        self.assertRaises(ValueError, self._database.update_no_rentals_book, other_book)

        self._database.add_book_to_database(other_book)
        self.assertEqual(len(self._database.get_book_list()), 2)
        self.assertEqual(self._database.get_book_list()[other_book], 1)
        self._database.update_no_rentals_book(other_book)
        self.assertEqual(self._database.get_book_list()[other_book], 2)

    def test_update_no_rentals_client(self):
        client = Client('Vasile Pop', 5030102111666, 2016)
        other_client = Client("Ion X", 5030201555666, 2009)

        self._database.add_client_to_database(client)
        self.assertEqual(len(self._database.get_client_list()), 1)
        self.assertEqual(self._database.get_client_list()[client], 1)
        self._database.update_no_rentals_client(client)
        self.assertEqual(self._database.get_client_list()[client], 2)

        self.assertRaises(ValueError, self._database.update_no_rentals_client, other_client)

        self._database.add_client_to_database(other_client)
        self.assertEqual(len(self._database.get_client_list()), 2)
        self.assertEqual(self._database.get_client_list()[other_client], 1)
        self._database.update_no_rentals_client(other_client)
        self.assertEqual(self._database.get_client_list()[other_client], 2)
