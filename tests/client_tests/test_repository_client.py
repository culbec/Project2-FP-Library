from domain.client import Client
from utils.library_controller import LibraryController


def test_add_client_to_list():
    library_controller = LibraryController()
    assert not library_controller.get_client_list()

    client1 = Client.create_client(1, 'Vasile Pop', 50301111222222, 2019)
    library_controller.use_client_repository().add_client_to_list(client1, library_controller)
    assert len(library_controller.get_client_list()) == 1

    client2 = Client.create_client(2, 'Ion X', 1000000333333, 2002)
    library_controller.use_client_repository().add_client_to_list(client2, library_controller)
    assert len(library_controller.get_client_list()) == 2
