"""
from tests.book_tests.test_domain_book import TestCasesBookDomain
from tests.book_tests.test_repository_book import test_add_book_to_list, test_modify_book, test_delete_book, \
    test_search_book_by_id
from tests.book_tests.test_validate_book import TestCasesBookValidator
from tests.client_tests.test_domain_client import test_create_client
from tests.client_tests.test_repository_client import test_add_client_to_list, test_modify_client, \
    test_search_client_by_id, test_delete_client
from tests.client_tests.test_validate_client import test_validate_client, test_validate_name, test_validate_cnp, \
    test_validate_sub_year, test_validate_subscription_age
from tests.database_tests.test_database import test_add_client_to_database, test_add_book_to_database, \
    test_update_no_rentals_book, test_update_no_rentals_client, test_book_in_database, test_client_in_database
from tests.rental_tests.test_domain_rental import test_create_rental
from tests.rental_tests.test_repository_rental import test_add_rental_to_list, test_delete_rental
from tests.rental_tests.test_validate_rental import test_validate_rental
from tests.test_library_controller import test_add_client_to_list_utils, test_add_book_to_list_utils, \
    test_search_book_by_title_utils, test_search_book_by_year_utils, test_search_client_by_name_utils, \
    test_modify_book_utils, test_modify_client_utils, test_delete_book_utils, test_delete_client_utils, \
    test_search_book_in_time_period, test_search_book_by_status_utils, \
    test_search_client_by_subscription_age_utils_utils, test_search_client_rented_books, test_rent_book_utils, \
    test_return_book_utils, test_generate_random_book, test_search_rental, test_most_rented_books, \
    test_sort_clients_by_name_and_no_rentals, test_first_20_percent_most_active_clients, test_sort_books_by_name


class Tester:
    def __init__(self):
        pass

    @staticmethod
    def run_all_tests():
        # Book tests
        TestCasesBookDomain().test_create_book()
        TestCasesBookValidator().test_validate_book()
        test_add_book_to_list()
        test_search_book_by_id()
        test_modify_book()
        test_delete_book()
        TestCasesBookValidator().test_validate_title()
        TestCasesBookValidator().test_validate_volume()
        TestCasesBookValidator().test_validate_year()
        TestCasesBookValidator().test_validate_author_name()
        TestCasesBookValidator().test_validate_period()
        TestCasesBookValidator().test_validate_status()

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

        # Rental tests
        test_create_rental()
        test_add_rental_to_list()
        test_delete_rental()
        test_validate_rental()
        test_search_rental()

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
        test_generate_random_book()
        test_most_rented_books()
        test_sort_clients_by_name_and_no_rentals()
        test_first_20_percent_most_active_clients()
        test_sort_books_by_name()

        # Database tests
        test_add_book_to_database()
        test_add_client_to_database()
        test_update_no_rentals_book()
        test_update_no_rentals_client()
        test_book_in_database()
        test_client_in_database()
"""
