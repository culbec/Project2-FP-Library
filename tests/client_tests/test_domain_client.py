import unittest

from domain.entities import Client


class TestCasesClientDomain(unittest.TestCase):
    def test_create_client(self):
        client1 = Client('Vasile Pop', 1021723551632, 2021)
        client2 = Client('Ionescu Jean', 5010203511333, 2017)
        client3 = Client('Maria Ion', 6120203111222, 2009)

        self.assertEqual(client1.get_identity(), 1021723551632)
        self.assertEqual(client1.get_name(), 'Vasile Pop')
        self.assertEqual(client1.get_cnp(), 1021723551632)
        self.assertEqual(client1.get_subscription_year(), 2021)

        self.assertEqual(client2.get_identity(), 5010203511333)
        self.assertEqual(client2.get_name(), 'Ionescu Jean')
        self.assertEqual(client2.get_cnp(), 5010203511333)
        self.assertEqual(client2.get_subscription_year(), 2017)

        self.assertEqual(client3.get_identity(), 6120203111222)
        self.assertEqual(client3.get_name(), 'Maria Ion')
        self.assertEqual(client3.get_cnp(), 6120203111222)
        self.assertEqual(client3.get_subscription_year(), 2009)
