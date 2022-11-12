from datetime import datetime

from utils.library_controller import LibraryController


def test_validate_client():
    library_controller = LibraryController()
    valid_client = library_controller.use_client_repository().create_client(1, 'Vasile Pop', 5030122111222, 2012)
    library_controller.use_client_validator().validate_client(valid_client, library_controller)
    library_controller.use_client_repository().add_client_to_list(valid_client, library_controller)

    wrong_name_client = library_controller.use_client_repository().create_client(1, 'Vasile-alexandru pOp', 5030122111222, 2009)
    try:
        library_controller.use_client_validator().validate_client(wrong_name_client, library_controller)
        assert False
    except ValueError as ve:
        assert str(ve) == "The client's name needs to be a valid string."

    wrong_cnp_client = library_controller.use_client_repository().create_client(1, 'Vasile Pop', '5021c1', 2009)
    try:
        library_controller.use_client_validator().validate_client(wrong_cnp_client, library_controller)
        assert False
    except ValueError as ve:
        assert str(ve) == "The client's CNP needs to be a valid one."

    wrong_subscription_year_client = library_controller.use_client_repository().create_client(1, 'Vasile Pop', 5030222111222, 1922)
    try:
        library_controller.use_client_validator().validate_client(wrong_subscription_year_client, library_controller)
        assert False
    except ValueError as ve:
        assert str(ve) == f"The client's subscription year cannot be greater than {datetime.now().year} " \
                          f"or more than 90 years of subscription."

    same_id_client = library_controller.use_client_repository().create_client(1, 'Ion X', 5030101111222, 1987)
    try:
        library_controller.use_client_validator().validate_client(same_id_client, library_controller)
        assert False
    except ValueError as ve:
        assert str(ve) == "Another client with the same identity or CNP already exists."


def test_validate_name():
    library_controller = LibraryController()

    valid_name = 'John-Martin F. Reginald'
    library_controller.use_client_validator().validate_name(valid_name)

    wrong_name = 'John-Martin F.123  143'
    try:
        library_controller.use_client_validator().validate_name(wrong_name)
        assert False
    except ValueError:
        assert True
