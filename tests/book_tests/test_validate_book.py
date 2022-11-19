from datetime import datetime

from domain.book import Book
from validate.validate_book import BookValidator


def test_validate_book():
    book_validator = BookValidator()
    valid_book = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    book_validator.validate_book(valid_book)

    wrong_author_book = Book(12, 'Amintiri din copilarie', 15, 1892, 'Amintiri din copilarie')
    try:
        book_validator.validate_book(wrong_author_book)
        assert False
    except ValueError as ve:
        assert str(ve) == "The author's name needs to be a valid string."

    wrong_title_book = Book(15, 1234, 'Ion Creanga', 1892, 'Amintiri din Copilarie')
    try:
        book_validator.validate_book(wrong_title_book)
        assert False
    except ValueError as ve:
        assert str(ve) == "The book's title needs to be a valid string."

    wrong_year_book = Book(15, 'Amintiri din copilarie', 'Ion Creanga', 'asd', 'Amintiri din copilarie')
    try:
        book_validator.validate_book(wrong_year_book)
        assert False
    except ValueError as ve:
        assert str(ve) == f"The book's release year needs to be betwwen 1680 and {datetime.now().year}."

    wrong_volume_book = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 16)
    try:
        book_validator.validate_book(wrong_volume_book)
        assert False
    except ValueError as ve:
        assert str(ve) == "The book's volume needs to be a valid string."


def test_validate_title():
    book_validator = BookValidator()
    valid_title = 'Valid Title'
    book_validator.validate_title(valid_title)

    wrong_title = ''
    try:
        book_validator.validate_title(wrong_title)
        assert False
    except ValueError as ve:
        assert str(ve) == "The title needs to be a valid string."


def test_validate_volume():
    book_validator = BookValidator()
    valid_volume = 'Valid Volume'
    book_validator.validate_volume(valid_volume)

    wrong_volume = ''
    try:
        book_validator.validate_volume(wrong_volume)
        assert False
    except ValueError as ve:
        assert str(ve) == "The volume needs to be a valid string."


def test_validate_year():
    book_validator = BookValidator()
    valid_year = 1780
    book_validator.validate_year(valid_year)

    wrong_year = 1412
    try:
        book_validator.validate_year(wrong_year)
        assert False
    except ValueError as ve:
        assert str(ve) == f"The release year needs to be an integer between 1680 and {datetime.now().year}."


def test_validate_author_name():
    book_validator = BookValidator()
    valid_name = 'Vasile Pop-Ion'

    book_validator.validate_author_name(valid_name)

    wrong_name = 'Vasile Pop-1Ion'
    try:
        book_validator.validate_author_name(wrong_name)
        assert False
    except ValueError as ve:
        assert str(ve) == "The author's name needs to be a valid string."


def test_validate_period():
    book_validator = BookValidator()
    book_validator.validate_period(1800, 1900)
    try:
        book_validator.validate_period(1650, 1901)
        assert False
    except ValueError:
        assert True


def test_validate_status():
    book_validator = BookValidator()
    book_validator.validate_status('Available')
    try:
        book_validator.validate_status('rEnted')
        assert False
    except ValueError:
        assert True
