import unittest
from datetime import datetime

from domain.entities import Book
from validate.validate_book import BookValidator


class TestCasesBookValidator(unittest.TestCase):
    def setUp(self) -> None:
        self._validator = BookValidator()

    def test_validate_book(self):
        self.valid_book = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        self.wrong_author_book = Book(12, 'Amintiri din copilarie', 15, 1892, 'Amintiri din copilarie')
        self.wrong_title_book = Book(15, 1234, 'Ion Creanga', 1892, 'Amintiri din Copilarie')
        self.wrong_year_book = Book(15, 'Amintiri din copilarie', 'Ion Creanga', 'asd', 'Amintiri din copilarie')
        self.wrong_volume_book = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 16)
        self.multiple_mistakes_book = Book(-1, 'a1c', '', 1300, 'Amintiri')

        self.assertIsNone(self._validator.validate_book(self.valid_book))
        self.assertRaises(ValueError, self._validator.validate_book, self.wrong_author_book)
        self.assertRaises(ValueError, self._validator.validate_book, self.wrong_title_book)
        self.assertRaises(ValueError, self._validator.validate_book, self.wrong_year_book)
        self.assertRaises(ValueError, self._validator.validate_book, self.wrong_volume_book)
        self.assertRaises(ValueError, self._validator.validate_book, self.multiple_mistakes_book)

    def test_validate_title(self):
        self._validator = BookValidator()
        self.assertIsNone(self._validator.validate_title('Valid Title'))
        self.assertRaises(ValueError, self._validator.validate_title, '')

    def test_validate_volume(self):
        self._validator = BookValidator()
        self.assertIsNone(self._validator.validate_volume('Valid Volume'))
        self.assertRaises(ValueError, self._validator.validate_volume, '')

    def test_validate_year(self):
        self._validator = BookValidator()
        self.assertIsNone(self._validator.validate_year(1780))
        self.assertRaises(ValueError, self._validator.validate_year, 1412)
        self.assertRaises(ValueError, self._validator.validate_year, int(datetime.now().year) + 1)

    def test_validate_author_name(self):
        self._validator = BookValidator()
        self.assertIsNone(self._validator.validate_author_name('Vasile Pop'))
        self.assertRaises(ValueError, self._validator.validate_author_name, 'Vasile Pop-1Ion')
        self.assertRaises(ValueError, self._validator.validate_author_name, '')

    def test_validate_period(self):
        self._validator = BookValidator()
        self.assertIsNone(self._validator.validate_period(1800, 1900))
        self.assertRaises(ValueError, self._validator.validate_period, 1800, 1799)
        self.assertRaises(ValueError, self._validator.validate_period, 1499, 1500)
        self.assertRaises(ValueError, self._validator.validate_period, 1400, 1900)
        self.assertRaises(ValueError, self._validator.validate_period, 2002, int(datetime.now().year) + 1)
        self.assertRaises(ValueError, self._validator.validate_period, int(datetime.now().year) + 1, 2012)

    def test_validate_status(self):
        self._validator = BookValidator()
        self.assertIsNone(self._validator.validate_status('Available'))
        self.assertIsNone(self._validator.validate_status('Rented'))
        self.assertRaises(ValueError, self._validator.validate_status, 'Availabl')
        self.assertRaises(ValueError, self._validator.validate_status, '')
        self.assertRaises(ValueError, self._validator.validate_status, 'rEntEd')
