from domain.client import Client


def test_create_client():
    client1 = Client(1, 'Vasile Pop', 1021723551632, 2021)
    client2 = Client(23, 'Ionescu Jean', 5010203511333, 2017)
    client3 = Client(51, 'Maria Ion', 6120203111222, 2009)

    assert client1.get_name() == 'Vasile Pop'
    assert client1.get_cnp() == 1021723551632

    assert client2.get_identity() == 23
    assert client2.get_subscription_year() == 2017

    assert client3.get_identity() == 51
    assert client3.get_name() == "Maria Ion"