from domain.book import Book
from utils.library_controller import LibraryController


def test_add_book_to_list():
    library_controller = LibraryController()
    book1 = Book.create_book(15, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    library_controller.use_book_repository().add_book_to_list(book1, library_controller)
    assert len(library_controller.get_book_dict()) == 1
