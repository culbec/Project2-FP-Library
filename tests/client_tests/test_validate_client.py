from datetime import datetime

from domain.client import Client
from repository.repository_client import ClientRepository
from utils.library_controller import LibraryController
from validate.validate_client import ClientValidator


def test_validate_client():
    client_validator = ClientValidator()
    client_repo = ClientRepository()
    valid_client = Client(1, 'Vasile Pop', 5030122111222, 2012)
    client_validator.validate_client(valid_client, client_repo)
    client_repo.add_client_to_list(valid_client)

    wrong_name_client = Client(1, 'Vasile-alexandru pOp', 5030122111222, 2009)
    try:
        client_validator.validate_client(wrong_name_client, client_repo)
        assert False
    except ValueError as ve:
        assert str(ve) == "The client's name needs to be a valid string."

    wrong_cnp_client = Client(1, 'Vasile Pop', '5021c1', 2009)
    try:
        client_validator.validate_client(wrong_cnp_client, client_repo)
        assert False
    except ValueError as ve:
        assert str(ve) == "The client's CNP needs to be a valid one."

    wrong_subscription_year_client = Client(1, 'Vasile Pop', 5030222111222, 1922)
    try:
        client_validator.validate_client(wrong_subscription_year_client, client_repo)
        assert False
    except ValueError as ve:
        assert str(ve) == f"The client's subscription year cannot be greater than {datetime.now().year} " \
                          f"or more than 90 years of subscription."

    same_id_client = Client(1, 'Ion X', 5030101111222, 1987)
    try:
        client_validator.validate_client(same_id_client, client_repo)
        assert False
    except ValueError as ve:
        assert str(ve) == "Another client with the same identity or CNP already exists."


def test_validate_name():
    client_validator = ClientValidator()

    valid_name = 'John-Martin F. Reginald'
    client_validator.validate_name(valid_name)

    wrong_name = 'John-Martin F.123  143'
    try:
        client_validator.validate_name(wrong_name)
        assert False
    except ValueError:
        assert True


def test_validate_cnp():
    client_validator = ClientValidator()

    valid_cnp = 5010302111666
    client_validator.validate_cnp(valid_cnp)

    wrong_cnp = '5010301222666'
    try:
        client_validator.validate_cnp(wrong_cnp)
        assert False
    except ValueError:
        assert True


def test_validate_sub_year():
    client_validator = ClientValidator()

    valid_sub_year = 2001
    client_validator.validate_sub_year(valid_sub_year)

    wrong_sub_year = 1800
    try:
        client_validator.validate_sub_year(wrong_sub_year)
        assert False
    except ValueError:
        assert True


def test_validate_subscription_age():
    client_validator = ClientValidator()

    client_validator.validate_subscription_age(80)
    try:
        client_validator.validate_subscription_age(91)
        assert False
    except ValueError:
        assert True