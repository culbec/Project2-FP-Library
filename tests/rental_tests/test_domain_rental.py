import unittest

from domain.entities import Book, Client, Rental


class TestCasesRentalDomain(unittest.TestCase):
    def test_create_rental(self):
        book = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        client = Client('Vasile Pop', 5030102111666, 2016)

        rental = Rental(client, book)

        self.assertEqual(rental.get_client().get_identity(), 5030102111666)
        self.assertEqual(rental.get_book().get_identity(), 0)
