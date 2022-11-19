from domain.client import Client
from repository.repository_client import ClientRepository


def test_add_client_to_list():
    client_repo = ClientRepository()
    assert not client_repo.get_client_list()

    client1 = Client(50301111222222, 'Vasile Pop', 50301111222222, 2019)
    client_repo.add_client_to_list(client1)
    assert len(client_repo.get_client_list()) == 1

    client2 = Client(1000000333333, 'Ion X', 1000000333333, 2002)
    client_repo.add_client_to_list(client2)
    assert len(client_repo.get_client_list()) == 2


def test_modify_client():
    client_repo = ClientRepository()
    client1 = Client(50301111222222, 'Vasile Pop', 50301111222222, 2019)
    client2 = Client(1000000333333, 'Ion X', 1000000333333, 2002)

    client_repo.add_client_to_list(client1)
    client_repo.add_client_to_list(client2)

    client_repo.modify_client(client1, 'Maria Y', 2016)
    client_repo.modify_client(client2, 'Vasile X', 2018)

    assert client1.get_subscription_year() == 2016
    assert client2.get_name() == 'Vasile X'


def test_search_client_by_id():
    client_repo = ClientRepository()
    client1 = Client(5030201111222, 'Vasile Pop', 5030201111222, 2016)
    client2 = Client(4010302111666, 'Ion X', 4010302111666, 2015)

    client_repo.add_client_to_list(client1)
    client_repo.add_client_to_list(client2)

    assert client_repo.search_client_by_id(5030201111222)

    try:
        client_repo.search_client_by_id(5030201222111)
        assert False
    except ValueError:
        assert True


def test_delete_client():
    client_repo = ClientRepository()
    assert not client_repo.get_client_list()
    client1 = Client(5030102111666, 'Vasile Pop', 5030102111666, 2016)
    client2 = Client(5020103666111, 'Ion X', 5020103666111, 2019)

    client_repo.add_client_to_list(client1)
    client_repo.add_client_to_list(client2)

    assert len(client_repo.get_client_list()) == 2
    client_repo.delete_client(client1)
    assert len(client_repo.get_client_list()) == 1
    client_repo.delete_client(client2)
    assert len(client_repo.get_client_list()) == 0
