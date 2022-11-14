from datetime import datetime

from domain.book import Book
from utils.library_controller import LibraryController


def test_validate_book():
    library_controller = LibraryController()
    valid_book = Book.create_book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    library_controller.use_book_validator().validate_book(valid_book)

    wrong_author_book = Book.create_book(12, 'Amintiri din copilarie', 15, 1892, 'Amintiri din copilarie')
    try:
        library_controller.use_book_validator().validate_book(wrong_author_book)
        assert False
    except ValueError as ve:
        assert str(ve) == "The author's name needs to be a valid string."

    wrong_title_book = Book.create_book(15, 1234, 'Ion Creanga', 1892, 'Amintiri din Copilarie')
    try:
        library_controller.use_book_validator().validate_book(wrong_title_book)
        assert False
    except ValueError as ve:
        assert str(ve) == "The book's title needs to be a valid string."

    wrong_year_book = Book.create_book(15, 'Amintiri din copilarie', 'Ion Creanga', 'asd', 'Amintiri din copilarie')
    try:
        library_controller.use_book_validator().validate_book(wrong_year_book)
        assert False
    except ValueError as ve:
        assert str(ve) == f"The book's release year needs to be betwwen 1680 and {datetime.now().year}."

    wrong_volume_book = Book.create_book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 16)
    try:
        library_controller.use_book_validator().validate_book(wrong_volume_book)
        assert False
    except ValueError as ve:
        assert str(ve) == "The book's volume needs to be a valid string."


def test_validate_title():
    library_controller = LibraryController()
    valid_title = 'Valid Title'
    library_controller.use_book_validator().validate_title(valid_title)

    wrong_title = ''
    try:
        library_controller.use_book_validator().validate_title(wrong_title)
        assert False
    except ValueError as ve:
        assert str(ve) == "The title needs to be a valid string."


def test_validate_year():
    library_controller = LibraryController()
    valid_year = 1780
    library_controller.use_book_validator().validate_year(valid_year)

    wrong_year = 1412
    try:
        library_controller.use_book_validator().validate_year(wrong_year)
        assert False
    except ValueError as ve:
        assert str(ve) == f"The release year needs to be an integer between 1680 and {datetime.now().year}."
