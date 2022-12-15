import unittest

from algorithms import sortingAlgorithms as sort_alg
from domain.entities import Client, Book
from utils.library_controller import LibraryController


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        self.library_controller = LibraryController()

        client1 = Client('Vasile Pop', 5030102111222, 2016)
        client2 = Client('Vasile X', 6010203111333, 2012)
        client3 = Client('Ion Marinescu', 4010203111555, 2002)

        self.library_controller.get_client_list().append(client1)
        self.library_controller.get_client_list().append(client2)
        self.library_controller.get_client_list().append(client3)

        self.library_controller.get_database().get_client_list()[client1] = 1000
        self.library_controller.get_database().get_client_list()[client2] = 800
        self.library_controller.get_database().get_client_list()[client3] = 5000

        book1 = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        book2 = Book(1, 'Ulysses', 'James Grant', 1922, 'Ulysses')
        book3 = Book(2, 'The Great Gatsby', 'Marinica', 2003, 'Marinel')

        self.library_controller.get_book_list().append(book1)
        self.library_controller.get_book_list().append(book2)
        self.library_controller.get_book_list().append(book3)

        self.library_controller.get_database().get_book_list()[book1] = 250
        self.library_controller.get_database().get_book_list()[book2] = 1001
        self.library_controller.get_database().get_book_list()[book3] = 45

        # declaring the sorted iterables for comparison
        self.sorted_book_database_ascending_rentals = {book3: 45, book1: 250, book2: 1001}
        self.sorted_book_database_descending_rentals = {book2: 1001, book1: 250, book3: 45}

        self.sorted_book_database_ascending_titles = {book1: 250, book2: 1001, book3: 45}
        self.sorted_book_database_descending_titles = {book3: 45, book2: 1001, book1: 250}

        self.sorted_client_database_ascending_name = {client3: 5000, client1: 1000, client2: 800}
        self.sorted_client_database_descending_name = {client2: 800, client1: 1000, client3: 5000}

        self.sorted_client_database_ascending_rentals = {client2: 800, client1: 1000, client3: 5000}
        self.sorted_client_database_descending_rentals = {client3: 5000, client1: 1000, client2: 800}

        self.book_list_tuples = list(self.library_controller.get_database().get_book_list().items())
        self.client_list_tuples = list(self.library_controller.get_database().get_client_list().items())

    def test_bingo_sort_ascending_book_rentals(self):
        # Bingo sort for books rentals - Ascending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, sort_alg.compare_rentals_books)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_rentals)

    def test_bingo_sort_descending_book_rentals(self):
        # Bingo sort for books rentals - Descending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, sort_alg.compare_rentals_books,
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_rentals)

    def test_bingo_sort_ascending_book_names(self):
        # Bingo sort for book names - Ascending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, sort_alg.compare_names_books)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_titles)

    def test_bingo_sort_descending_book_names(self):
        # Bingo sort for book names - Descending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, sort_alg.compare_names_books,
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_titles)

    def test_bingo_sort_ascending_client_rentals(self):
        # Bingo sort for client rentals - Ascending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, sort_alg.compare_client_rentals)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_rentals)

    def test_bingo_sort_descending_client_rentals(self):
        # Bingo sort for client rentals - Descending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, sort_alg.compare_client_rentals,
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_rentals)

    def test_bingo_sort_ascending_client_names(self):
        # Bingo sort for client names - Ascending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, sort_alg.compare_names_clients)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_name)

    def test_bingo_sort_descending_client_names(self):
        # Bingo sort for client names - Descending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, sort_alg.compare_names_clients)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_name)

    def test_merge_sort_ascending_book_rentals(self):
        # Merge sort for book rentals - Ascending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, sort_alg.compare_rentals_books)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_rentals)

    def test_merge_sort_descending_book_rentals(self):
        # Merge sort for book rentals - Descending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, sort_alg.compare_rentals_books,
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_rentals)

    def test_merge_sort_ascending_book_names(self):
        # Merge sort for book names - Ascending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, sort_alg.compare_names_books)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_titles)

    def test_merge_sort_descending_book_names(self):
        # Merge sort for book names - Descending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, sort_alg.compare_names_books,
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_titles)

    def test_merge_sort_ascending_client_rentals(self):
        # Merge sort for client rentals - Ascending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, sort_alg.compare_client_rentals)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_rentals)

    def test_merge_sort_descending_client_rentals(self):
        # Merge sort for client rentals - Descending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, sort_alg.compare_client_rentals,
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_rentals)

    def test_merge_sort_ascending_client_names(self):
        # Merge sort for client names - Ascending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, sort_alg.compare_names_clients)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_name)

    def test_merge_sort_ascending_client_names(self):
        # Merge sort for client names - Descending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, sort_alg.compare_names_clients,
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_name)
