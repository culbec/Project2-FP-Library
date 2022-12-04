import unittest

from domain.entities import Client
from repository.repository_client import ClientRepository


class TestCasesClientRepository(unittest.TestCase):
    def setUp(self) -> None:
        self._repo = ClientRepository()
        self.client1 = Client('Vasile Pop', 50301111222222, 2019)
        self.client2 = Client('Ion X', 1000000333333, 2002)

    def test_add_client_to_list(self):
        self.assertFalse(self._repo.get_client_list())

        self._repo.add_client_to_list(self.client1)
        self.assertEqual(len(self._repo.get_client_list()), 1)

        self._repo.add_client_to_list(self.client2)
        self.assertEqual(len(self._repo.get_client_list()), 2)

    def test_modify_client(self):
        self._repo.add_client_to_list(self.client1)
        self._repo.add_client_to_list(self.client2)

        self.assertEqual(self.client1.get_identity(), 50301111222222)
        self.assertEqual(self.client1.get_name(), 'Vasile Pop')
        self.assertEqual(self.client1.get_cnp(), 50301111222222)
        self.assertEqual(self.client1.get_subscription_year(), 2019)

        self._repo.modify_client(self.client1, 'Maria Y', 2016)
        self.assertEqual(self.client1.get_name(), 'Maria Y')
        self.assertEqual(self.client1.get_subscription_year(), 2016)

        self.assertEqual(self.client2.get_identity(), 1000000333333)
        self.assertEqual(self.client2.get_name(), 'Ion X')
        self.assertEqual(self.client2.get_cnp(), 1000000333333)
        self.assertEqual(self.client2.get_subscription_year(), 2002)

        self._repo.modify_client(self.client2, 'Vasile X', 2018)
        self.assertEqual(self.client2.get_name(), 'Vasile X')
        self.assertEqual(self.client2.get_subscription_year(), 2018)

    def test_search_client_by_id(self):
        self._repo.add_client_to_list(self.client1)
        self._repo.add_client_to_list(self.client2)

        self.assertEqual(self._repo.search_client_by_id(50301111222222), self.client1)

        self.assertRaises(ValueError, self._repo.search_client_by_id, 5030201222111)
        self.assertRaises(ValueError, self._repo.search_client_by_id, 1112223334445)

    def test_delete_client(self):
        self.assertFalse(self._repo.get_client_list())

        self._repo.add_client_to_list(self.client1)
        self._repo.add_client_to_list(self.client2)

        self.assertEqual(len(self._repo.get_client_list()), 2)
        self._repo.delete_client(self.client1)
        self.assertEqual(len(self._repo.get_client_list()), 1)
        self._repo.delete_client(self.client2)
        self.assertFalse(self._repo.get_client_list())
