import time

from tests.book_tests.test_domain_book import test_create_book
from tests.client_tests.test_domain_client import test_create_client
from tests.test_library_controller import test_add_client_to_list_utils, test_add_book_to_list_utils, \
    test_search_book_by_title_utils, test_search_book_by_year_utils, test_search_client_by_name_utils
from tests.book_tests.test_repository_book import test_add_book_to_list
from tests.client_tests.test_repository_client import test_add_client_to_list
from tests.book_tests.test_validate_book import test_validate_book, test_validate_year, test_validate_title
from tests.client_tests.test_validate_client import test_validate_client, test_validate_name


class Tester:
    def __init__(self):
        pass

    @staticmethod
    def run_all_tests():
        # Book tests
        test_create_book()
        test_validate_book()
        test_add_book_to_list()
        test_validate_title()
        test_validate_year()

        # Client tests
        test_create_client()
        test_validate_client()
        test_validate_name()
        test_add_client_to_list()

        # LibraryController tests
        test_add_client_to_list_utils()
        test_add_book_to_list_utils()
        test_search_book_by_title_utils()
        test_search_book_by_year_utils()
        test_search_client_by_name_utils()
