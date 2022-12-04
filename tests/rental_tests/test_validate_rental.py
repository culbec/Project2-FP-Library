import unittest

from domain.entities import Book, Client, Rental
from repository.repository_rental import RentalRepository
from validate.validate_rental import RentalValidator


class TestCasesRentalRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = RentalRepository()
        self._validator = RentalValidator()

    def test_validate_rental(self):
        book = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        client = Client('Vasile Pop', 5030102111666, 2016)
        rental = Rental(client, book)
        same_rental = Rental(client, book)

        self.assertIsNone(self._validator.validate_rental(rental, self._repo.get_rentals_list()))
        self._repo.add_rental_to_list(rental)
        self.assertRaises(ValueError, self._validator.validate_rental, same_rental, self._repo.get_rentals_list())
