from utils.library_controller import LibraryController


def test_add_client_to_list_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils(1, 'Vasile Pop', 5010203111222, 2009, library_controller)
    assert len(library_controller.get_client_list()) == 1
    try:
        library_controller.add_client_to_list_utils(1, 'Vasi 33', 5113344666777, 1900, library_controller)
        assert False
    except ValueError:
        assert True
    try:
        library_controller.add_client_to_list_utils(1, 'Ion X', 4112233444555, 2008, library_controller)
        assert False
    except ValueError:
        assert True
    library_controller.add_client_to_list_utils(2, 'Maria Y', 6112233555666, 2010, library_controller)
    assert len(library_controller.get_client_list()) == 2


def test_add_book_to_list_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie', library_controller)
    assert len(library_controller.get_book_dict()) == 1
    try:
        library_controller.add_book_to_list_utils(200, 'The Great Gatsby', 123,
                                                  1928, 'The Great Gatsby', library_controller)
        assert False
    except ValueError:
        assert True
    library_controller.add_book_to_list_utils(100, 'The Great Gatsby', 'F. Scott Fitzgerald',
                                              1928, 'The Great Gatsby', library_controller)


def test_search_book_by_title_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie', library_controller)
    library_controller.add_book_to_list_utils(2, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie', library_controller)
    book_list = library_controller.search_book_by_title_utils('Amintiri din copilarie', library_controller)
    assert len(book_list) == 2

    try:
        library_controller.search_book_by_title_utils('', library_controller)
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_book_by_title_utils('Amintiri din ...', library_controller)
        assert False
    except ValueError:
        assert True


def test_search_book_by_year_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie', library_controller)
    library_controller.add_book_to_list_utils(2, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie', library_controller)
    book_list = library_controller.search_book_by_year_utils(1892, library_controller)
    assert len(book_list) == 2

    try:
        library_controller.search_book_by_year_utils(1450, library_controller)
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_book_by_year_utils(2021, library_controller)
        assert False
    except ValueError:
        assert True


def test_search_client_by_name_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils(1, 'Vasile Pop', 5111122333444, 2019, library_controller)
    library_controller.add_client_to_list_utils(2, 'Vasile Pop', 6111222333444, 2010, library_controller)

    client_list = library_controller.search_client_by_name_utils('Vasile Pop', library_controller)
    assert len(client_list) == 2

    try:
        library_controller.search_client_by_name_utils('Vasil Pop', library_controller)
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_client_by_name_utils('Vasil1 P0p', library_controller)
        assert False
    except ValueError:
        assert True
