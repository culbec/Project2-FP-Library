import unittest

from domain.entities import Book, Client, Rental
from repository.repository_rental import RentalRepository


class TestCasesRepositoryRental(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = RentalRepository()
        self.book = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        self.client = Client("Vasile Pop", 5030102111666, 2016)

    def test_add_rental_to_list(self):
        rental = Rental(self.client, self.book)

        self.assertFalse(self._repo.get_rentals_list())
        self._repo.add_rental_to_list(rental)
        self.assertTrue(self._repo.get_rentals_list())
        self.assertEqual(len(self._repo.get_rentals_list()), 1)

    def test_delete_rental(self):
        rental = Rental(self.client, self.book)

        self.assertFalse(self._repo.get_rentals_list())
        self._repo.add_rental_to_list(rental)
        self.assertTrue(self._repo.get_rentals_list())
        self.assertEqual(len(self._repo.get_rentals_list()), 1)

        self._repo.delete_rental(rental)
        self.assertFalse(self._repo.get_rentals_list())
