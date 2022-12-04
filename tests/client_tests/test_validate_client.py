import unittest
from datetime import datetime

from domain.entities import Client
from repository.repository_client import ClientRepository
from validate.validate_client import ClientValidator


class TestCasesClientValidator(unittest.TestCase):
    def setUp(self) -> None:
        self._validator = ClientValidator()
        self._repo = ClientRepository()

    def test_validate_client(self):
        valid_client = Client('Vasile Pop', 5030101111222, 2012)
        self.assertIsNone(self._validator.validate_client(valid_client, self._repo))
        self._repo.add_client_to_list(valid_client)

        wrong_name_client = Client('Vasile-alexandru pOp', 5030122111222, 2009)
        self.assertRaises(ValueError, self._validator.validate_client, wrong_name_client, self._repo)

        wrong_cnp_client = Client('Vasile Pop', '5021c1', 2009)
        self.assertRaises(ValueError, self._validator.validate_client, wrong_cnp_client, self._repo)

        wrong_subscription_year_client = Client('Vasile Pop', 5030222111222, 1922)
        self.assertRaises(ValueError, self._validator.validate_client, wrong_subscription_year_client, self._repo)

        same_id_client = Client('Ion X', 5030101111222, 1987)
        self.assertRaises(ValueError, self._validator.validate_client, same_id_client, self._repo)

    def test_validate_name(self):
        valid_name = 'John-Martin F. Reginald'
        self.assertIsNone(self._validator.validate_name(valid_name))

        wrong_name = 'John-Martin F.123  143'
        self.assertRaises(ValueError, self._validator.validate_name, wrong_name)

        self.assertRaises(ValueError, self._validator.validate_name, '')

    def test_validate_cnp(self):
        valid_cnp = 5010302111666
        self.assertIsNone(self._validator.validate_cnp(valid_cnp))

        wrong_cnp = '5010301222666'
        self.assertRaises(ValueError, self._validator.validate_cnp, wrong_cnp)
        self.assertRaises(ValueError, self._validator.validate_cnp, 'abcdefghijk123531')

    def test_validate_sub_year(self):
        valid_sub_year = 2001
        self.assertIsNone(self._validator.validate_sub_year(valid_sub_year))

        wrong_sub_year = 1800
        self.assertRaises(ValueError, self._validator.validate_sub_year, wrong_sub_year)

        self.assertRaises(ValueError, self._validator.validate_sub_year, int(datetime.now().year) + 1)
        self.assertRaises(ValueError, self._validator.validate_sub_year, '')

    def test_validate_subscription_age(self):
        self.assertIsNone(self._validator.validate_subscription_age(80))
        self.assertRaises(ValueError, self._validator.validate_subscription_age, 91)
        self.assertRaises(ValueError, self._validator.validate_subscription_age, '')
