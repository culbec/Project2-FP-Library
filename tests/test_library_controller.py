from datetime import datetime

from utils.library_controller import LibraryController


def test_add_client_to_list_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5010203111222, 2009)
    assert len(library_controller.get_client_list()) == 1
    try:
        library_controller.add_client_to_list_utils('Vasi 33', 5113344666777, 1900)
        assert False
    except ValueError:
        assert True
    library_controller.add_client_to_list_utils('Maria Y', 6112233555666, 2010)
    assert len(library_controller.get_client_list()) == 2


def test_add_book_to_list_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie')
    assert len(library_controller.get_book_list()) == 1
    try:
        library_controller.add_book_to_list_utils(200, 'The Great Gatsby', 123,
                                                  1928, 'The Great Gatsby')
        assert False
    except ValueError:
        assert True
    library_controller.add_book_to_list_utils(100, 'The Great Gatsby', 'F. Scott Fitzgerald',
                                              1928, 'The Great Gatsby')


def test_search_book_by_title_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(2, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie')
    book_list = library_controller.search_book_by_title_utils('Amintiri din copilarie')
    assert len(book_list) == 2

    try:
        library_controller.search_book_by_title_utils('')
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_book_by_title_utils('Amintiri din ...')
        assert False
    except ValueError:
        assert True


def test_search_book_by_year_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(2, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie')
    book_list = library_controller.search_book_by_year_utils(1892)
    assert len(book_list) == 2

    try:
        library_controller.search_book_by_year_utils(1450)
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_book_by_year_utils(2021)
        assert False
    except ValueError:
        assert True


def test_search_book_in_time_period():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga',
                                              1892, 'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga',
                                              1881, 'Basme din popor')
    library_controller.add_book_to_list_utils(2, 'Ulysses', 'James Grant',
                                              1920, 'Ulysses')
    assert len(library_controller.search_book_in_time_period(1800, 2000)) == 3
    try:
        library_controller.search_book_in_time_period(1560, 2011)
        assert False
    except ValueError as ve:
        assert str(ve) == f"1560 is not a positive integer between 1680 and {datetime.now().year}"
    try:
        library_controller.search_book_in_time_period(1700, 1780)
        assert False
    except ValueError as ve:
        assert str(ve) == "There are no books published between 1700 and 1780."


def test_search_book_by_status_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                              'Povestea lui Harap-Alb')

    assert len(library_controller.get_book_list()) == 2
    assert len(library_controller.search_book_by_status_utils('Available')) == 2

    try:
        library_controller.search_book_by_status_utils('rented')
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_book_by_status_utils('Rented')
        assert False
    except ValueError:
        assert True


def test_search_client_by_name_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5111122333444, 2019)
    library_controller.add_client_to_list_utils('Vasile Pop', 6111222333444, 2010)

    client_list = library_controller.search_client_by_name_utils('Vasile Pop')
    assert len(client_list) == 2

    try:
        library_controller.search_client_by_name_utils('Vasil Pop')
        assert False
    except ValueError:
        assert True

    try:
        library_controller.search_client_by_name_utils('Vasil1 P0p')
        assert False
    except ValueError:
        assert True
        

def test_search_client_by_subscription_age_utils_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
    library_controller.add_client_to_list_utils('Ion X', 5030201666111, 2016)
    assert len(library_controller.search_client_by_subscription_age_utils(6)) == 2
    
    try:
        library_controller.search_client_by_subscription_age_utils(5)
        assert False
    except ValueError:
        assert True
    
    try:
        library_controller.search_client_by_subscription_age_utils(91)
        assert False
    except ValueError:
        assert True


def test_search_client_rented_books():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.get_client_books()\
        .update({library_controller.get_client_list()[0]: [library_controller.get_book_list()[0]]})
    assert len(library_controller.search_client_rented_books()) == 1
    del library_controller.get_client_books()[library_controller.get_client_list()[0]]
    try:
        library_controller.search_client_rented_books()
        assert False
    except TypeError:
        assert True


def test_modify_book_utils():
    library_controller = LibraryController()
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.modify_book_utils(1, 'Baltagul', 'Mihail Sadoveanu', 1928, 'Baltagul')
    assert library_controller.get_book_list()[0].get_title() == 'Baltagul'

    try:
        library_controller.modify_book_utils(1, 'abc1', 23, '1231', 54)
        assert False
    except ValueError:
        assert True


def test_modify_client_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
    library_controller.add_client_to_list_utils('Maria Y', 6010203111666, 2018)

    library_controller.modify_client_utils(5030102111666, 'Ion X', 2019)
    assert library_controller.get_client_list()[0].get_subscription_year() == 2019

    try:
        library_controller.modify_client_utils(6010203111666, 'Maria Y', '201e')
        assert False
    except ValueError:
        assert True


def test_delete_book_utils():
    library_controller = LibraryController()
    assert not library_controller.get_book_list()
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                              'Povestea lui Harap-Alb')
    assert len(library_controller.get_book_list()) == 2
    library_controller.delete_book_utils(1)
    assert len(library_controller.get_book_list()) == 1
    library_controller.delete_book_utils(2)
    assert not library_controller.get_book_list()


def test_delete_client_utils():
    library_controller = LibraryController()
    assert not library_controller.get_client_list()
    library_controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
    library_controller.add_client_to_list_utils('Ion X', 5010203222666, 2019)

    assert len(library_controller.get_client_list()) == 2
    library_controller.delete_client_utils(5030102111666)
    assert len(library_controller.get_client_list()) == 1
    library_controller.delete_client_utils(5010203222666)
    assert len(library_controller.get_client_list()) == 0


def test_rent_book_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5030201111666, 2016)
    library_controller.add_client_to_list_utils('Ion X', 5010203666111, 2019)
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                              'Basme din popor')
    library_controller.rent_book_utils(5030201111666, 1)
    assert library_controller.get_client_books() == {library_controller.get_client_list()[0]:
                                                     [library_controller.get_book_list()[0]]}
    assert library_controller.get_client_books()[library_controller.get_client_list()[0]][0].get_identity() == 1

    try:
        library_controller.rent_book_utils(5010203666111, 1)
        assert False
    except ValueError:
        assert True


def test_return_book_utils():
    library_controller = LibraryController()
    library_controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
    library_controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                              'Amintiri din copilarie')
    library_controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                              'Basme din popor')
    library_controller.rent_book_utils(5030102111666, 1)
    assert len(library_controller.get_client_books()[library_controller.get_client_list()[0]]) == 1
    library_controller.rent_book_utils(5030102111666, 2)
    assert len(library_controller.get_client_books()[library_controller.get_client_list()[0]]) == 2
    library_controller.return_book_utils(5030102111666, 1)
    assert library_controller.get_book_list()[0].get_status() == 'Available'
    assert len(library_controller.get_client_books()[library_controller.get_client_list()[0]]) == 1
    library_controller.return_book_utils(5030102111666, 2)
    assert not library_controller.get_client_books()
