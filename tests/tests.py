import time

from tests.book_tests.test_domain_book import test_create_book
from tests.client_tests.test_domain_client import test_create_client
from tests.test_library_controller import test_add_client_to_list_utils, test_add_book_to_list_utils, \
    test_search_book_by_title_utils, test_search_book_by_year_utils, test_search_client_by_name_utils, \
    test_modify_book_utils, test_modify_client_utils, test_delete_book_utils, test_delete_client_utils, \
    test_search_book_in_time_period, test_search_book_by_status_utils, \
    test_search_client_by_subscription_age_utils_utils, test_search_client_rented_books, test_rent_book_utils, \
    test_return_book_utils
from tests.book_tests.test_repository_book import test_add_book_to_list, test_modify_book, test_delete_book, \
    test_search_book_by_id
from tests.client_tests.test_repository_client import test_add_client_to_list, test_modify_client, \
    test_search_client_by_id, test_delete_client
from tests.book_tests.test_validate_book import test_validate_book, test_validate_year, test_validate_title, \
    test_validate_author_name, test_validate_volume, test_validate_period, test_validate_status
from tests.client_tests.test_validate_client import test_validate_client, test_validate_name, test_validate_cnp, \
    test_validate_sub_year, test_validate_subscription_age


class Tester:
    def __init__(self):
        pass

    @staticmethod
    def run_all_tests():
        # Book tests
        test_create_book()
        test_validate_book()
        test_add_book_to_list()
        test_search_book_by_id()
        test_modify_book()
        test_delete_book()
        test_validate_title()
        test_validate_volume()
        test_validate_year()
        test_validate_author_name()
        test_validate_period()
        test_validate_status()

        # Client tests
        test_create_client()
        test_validate_client()
        test_validate_name()
        test_validate_cnp()
        test_validate_sub_year()
        test_validate_subscription_age()
        test_add_client_to_list()
        test_modify_client()
        test_search_client_by_id()
        test_delete_client()

        # LibraryController tests
        test_add_client_to_list_utils()
        test_add_book_to_list_utils()
        test_search_book_by_title_utils()
        test_search_book_by_year_utils()
        test_search_book_in_time_period()
        test_search_book_by_status_utils()
        test_search_client_by_name_utils()
        test_search_client_by_subscription_age_utils_utils()
        test_search_client_rented_books()
        test_modify_book_utils()
        test_modify_client_utils()
        test_delete_book_utils()
        test_delete_client_utils()
        test_rent_book_utils()
        test_return_book_utils()
