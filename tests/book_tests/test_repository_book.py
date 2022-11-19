from domain.book import Book
from repository.repository_book import BookRepository


def test_add_book_to_list():
    book_repo = BookRepository()
    book1 = Book(15, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    book_repo.add_book_to_list(book1)
    assert len(book_repo.get_book_list()) == 1


def test_search_book_by_id():
    book_repo = BookRepository()
    book = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    book_repo.add_book_to_list(book)
    assert book_repo.search_book_by_id(1)

    try:
        book_repo.search_book_by_id(2)
        assert False
    except ValueError:
        assert True


def test_modify_book():
    book_repo = BookRepository()
    book1 = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    book2 = Book(2, 'Povestea lui Harap-Alb', 'Ion Creanga', 1882, 'Povestea lui Harap-Alb')
    book_repo.add_book_to_list(book1)
    book_repo.add_book_to_list(book2)

    book_repo.modify_book(book1, 'Ulysses', 'James Grant', '1922', 'Ulysses')
    assert book1.get_title() == 'Ulysses'
    assert book1.get_author() == 'James Grant'

    book_repo.modify_book(book2, 'Amintiri din copilarie', 'Mihai Eminescu', 1900, 'Povestea unui om lenes')
    assert book2.get_author() == 'Mihai Eminescu'
    assert book2.get_year() == 1900
    assert book2.get_volume() == 'Povestea unui om lenes'


def test_delete_book():
    book_repo = BookRepository()
    assert not book_repo.get_book_list()
    book1 = Book(1, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
    book2 = Book(2, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881, 'Povestea lui Harap-Alb')
    book_repo.add_book_to_list(book1)
    book_repo.add_book_to_list(book2)
    assert len(book_repo.get_book_list()) == 2

    book_repo.delete_book(book1)
    assert len(book_repo.get_book_list()) == 1
    book_repo.delete_book(book2)
    assert len(book_repo.get_book_list()) == 0
