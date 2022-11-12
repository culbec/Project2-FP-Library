from repository.repository_client import ClientRepository
from utils.library_controller import LibraryController


def test_create_client():
    client_repo = ClientRepository()
    client1 = client_repo.create_client(1, 'Vasile Pop', 1021723551632, 2021)
    client2 = client_repo.create_client(23, 'Ionescu Jean', 5010203511333, 2017)
    client3 = client_repo.create_client(51, 'Maria Ion', 6120203111222, 2009)

    assert client1.get_name() == 'Vasile Pop'
    assert client1.get_cnp() == 1021723551632

    assert client2.get_identity() == 23
    assert client2.get_subscription_year() == 2017

    assert client3.get_identity() == 51
    assert client3.get_name() == "Maria Ion"


def test_add_client_to_list():
    library_controller = LibraryController()
    assert not library_controller.get_client_list()

    client1 = library_controller.use_client_repository().create_client(1, 'Vasile Pop', 50301111222222, 2019)
    library_controller.use_client_repository().add_client_to_list(client1, library_controller)
    assert len(library_controller.get_client_list()) == 1

    client2 = library_controller.use_client_repository().create_client(2, 'Ion X', 1000000333333, 2002)
    library_controller.use_client_repository().add_client_to_list(client2, library_controller)
    assert len(library_controller.get_client_list()) == 2


def test_search_client_by_name():
    library_controller = LibraryController()
    client1 = library_controller.use_client_repository().create_client(1, 'Vasile Pop', 5030122111222, 2019)
    library_controller.use_client_repository().add_client_to_list(client1, library_controller)
    client2 = library_controller.use_client_repository().create_client(2, 'Vasile Pop', 5010203444555, 2012)
    library_controller.use_client_repository().add_client_to_list(client2, library_controller)

    client_list = library_controller.use_client_repository().search_client_by_name('Vasile Pop', library_controller)
    assert len(client_list) == 2

    try:
        library_controller.use_client_repository().search_client_by_name('Vasile X', library_controller)
        assert False
    except ValueError:
        assert True
