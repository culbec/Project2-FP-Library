from utils.library_controller import LibraryController


def test_create_book():
    library_controller = LibraryController()
    book1 = library_controller.use_book_repository().create_book(15, 'Amintiri din copilarie', 'Ion Creanga',
                                                                 1892, 'Amintiri din copilarie')
    book2 = library_controller.use_book_repository().create_book(21, 'Ulysses', 'James Joyce',
                                                                 1922, 'Ulysses')
    book3 = library_controller.use_book_repository().create_book(23, 'The Great Gatsby', 'F. Scott Fitzgerald',
                                                                 1925, 'The Great Gatsby')
    assert book1.get_title() == 'Amintiri din copilarie'
    assert book1.get_status() == 'Available'

    assert book2.get_author() == 'James Joyce'
    assert book2.get_identity() == 21

    assert book3.get_volume() == 'The Great Gatsby'
    assert book3.get_year() == 1925


def test_add_book_to_list():
    library_controller = LibraryController()
    book1 = library_controller.use_book_repository().create_book(15, 'Amintiri din copilarie', 'Ion Creanga',
                                                                 1892, 'Amintiri din copilarie')
    library_controller.use_book_repository().add_book_to_list(book1, library_controller)
    assert len(library_controller.get_book_list()) == 1


def test_search_book_by_title():
    library_controller = LibraryController()
    book1 = library_controller.use_book_repository().create_book(21, 'Ulysses', 'James Joyce',
                                                                 1922, 'Ulysses')
    book2 = library_controller.use_book_repository().create_book(20, 'Ulysses', 'James Joyce',
                                                                 1922, 'Ulysses')
    library_controller.use_book_repository().add_book_to_list(book1, library_controller)
    library_controller.use_book_repository().add_book_to_list(book2, library_controller)
    book_list = library_controller.use_book_repository().search_book_by_title('Ulysses', library_controller)
    assert len(book_list) == 2
    try:
        library_controller.use_book_repository().search_book_by_title('Non-existing title', library_controller)
        assert False
    except ValueError as ve:
        assert str(ve) == "Books with the passed title do not exist!"


def test_search_book_by_year():
    library_controller = LibraryController()
    book = library_controller.use_book_repository().create_book(21, 'Ulysses', 'James Joyce',
                                                                1922, 'Ulysses')
    other_book = library_controller.use_book_repository().create_book(12, 'Ulysses', 'James Joyce',
                                                                      1922, 'Ulysses')
    library_controller.use_book_repository().add_book_to_list(book, library_controller)
    library_controller.use_book_repository().add_book_to_list(other_book, library_controller)

    book_list = library_controller.use_book_repository().search_book_by_year(1922, library_controller)
    assert len(book_list) == 2

    try:
        library_controller.use_book_repository().search_book_by_year(1909, library_controller)
        assert False
    except ValueError as ve:
        assert str(ve) == "Books with the passed release year do not exist!"
