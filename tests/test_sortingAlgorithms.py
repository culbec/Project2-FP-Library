import unittest

from algorithms import sortingAlgorithms as sort_alg
from domain.entities import Client, Book
from utils.library_controller import LibraryController


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        self.library_controller = LibraryController()

        self.client1 = Client('Vasile Pop', 5030102111222, 2016)
        self.client2 = Client('Vasile X', 6010203111333, 2012)
        self.client3 = Client('Ion Marinescu', 4010203111555, 2002)

        self.library_controller.get_client_list().append(self.client1)
        self.library_controller.get_client_list().append(self.client2)
        self.library_controller.get_client_list().append(self.client3)

        self.library_controller.get_database().get_client_list()[self.client1] = 1000
        self.library_controller.get_database().get_client_list()[self.client2] = 800
        self.library_controller.get_database().get_client_list()[self.client3] = 5000

        self.book1 = Book(0, 'Amintiri din copilarie', 'Ion Creanga', 1892, 'Amintiri din copilarie')
        self.book2 = Book(1, 'Ulysses', 'James Grant', 1922, 'Ulysses')
        self.book3 = Book(2, 'The Great Gatsby', 'Marinica', 2003, 'Marinel')

        self.library_controller.get_book_list().append(self.book1)
        self.library_controller.get_book_list().append(self.book2)
        self.library_controller.get_book_list().append(self.book3)

        self.library_controller.get_database().get_book_list()[self.book1] = 250
        self.library_controller.get_database().get_book_list()[self.book2] = 1001
        self.library_controller.get_database().get_book_list()[self.book3] = 45

        # declaring the sorted iterables for comparison
        self.sorted_book_database_ascending_rentals = {self.book3: 45, self.book1: 250, self.book2: 1001}
        self.sorted_book_database_descending_rentals = {self.book2: 1001, self.book1: 250, self.book3: 45}

        self.sorted_book_database_ascending_titles = {self.book1: 250, self.book2: 1001, self.book3: 45}
        self.sorted_book_database_descending_titles = {self.book3: 45, self.book2: 1001, self.book1: 250}

        self.sorted_client_database_ascending_name = {self.client3: 5000, self.client1: 1000, self.client2: 800}
        self.sorted_client_database_descending_name = {self.client2: 800, self.client1: 1000, self.client3: 5000}

        self.sorted_client_database_ascending_rentals = {self.client2: 800, self.client1: 1000, self.client3: 5000}
        self.sorted_client_database_descending_rentals = {self.client3: 5000, self.client1: 1000, self.client2: 800}

        self.book_list_tuples = list(self.library_controller.get_database().get_book_list().items())
        self.client_list_tuples = list(self.library_controller.get_database().get_client_list().items())

    def test_compare(self):
        self.assertTrue(sort_alg.compare(self.book1, self.book3, key=lambda elem: elem.get_year()))
        self.assertFalse(sort_alg.compare(self.book_list_tuples[0], self.book_list_tuples[2], key=lambda elem: elem[1]))

    def test_bingo_sort_ascending_book_rentals(self):
        # Bingo sort for books rentals - Ascending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, key=lambda elem: elem[1])
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_rentals)

    def test_bingo_sort_descending_book_rentals(self):
        # Bingo sort for books rentals - Descending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, key=lambda elem: elem[1], reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_rentals)

    def test_bingo_sort_ascending_book_names(self):
        # Bingo sort for book names - Ascending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, key=lambda elem: elem[0].get_title())
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_titles)

    def test_bingo_sort_descending_book_names(self):
        # Bingo sort for book names - Descending
        book_list_tuples_sorted = sort_alg.bingo_sort(self.book_list_tuples, key=lambda elem: elem[0].get_title(),
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_titles)

    def test_bingo_sort_ascending_client_rentals(self):
        # Bingo sort for client rentals - Ascending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, key=lambda elem: elem[1])
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_rentals)

    def test_bingo_sort_descending_client_rentals(self):
        # Bingo sort for client rentals - Descending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, key=lambda elem: elem[1],
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_rentals)

    def test_bingo_sort_ascending_client_names(self):
        # Bingo sort for client names - Ascending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, key=lambda elem: elem[0].get_name())
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_name)

    def test_bingo_sort_descending_client_names(self):
        # Bingo sort for client names - Descending
        client_list_tuples_sorted = sort_alg.bingo_sort(self.client_list_tuples, key=lambda elem: elem[0].get_name(),
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_name)

    def test_merge_sort_ascending_book_rentals(self):
        # Merge sort for book rentals - Ascending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, key=lambda elem: elem[1])
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_rentals)

    def test_merge_sort_descending_book_rentals(self):
        # Merge sort for book rentals - Descending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, key=lambda elem: elem[1],
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_rentals)

    def test_merge_sort_ascending_book_names(self):
        # Merge sort for book names - Ascending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, key=lambda elem: elem[0].get_title())
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_ascending_titles)

    def test_merge_sort_descending_book_names(self):
        # Merge sort for book names - Descending
        book_list_tuples_sorted = sort_alg.merge_sort(self.book_list_tuples, key=lambda elem: elem[0].get_title(),
                                                      reverse=True)
        self.assertEqual(dict(book_list_tuples_sorted), self.sorted_book_database_descending_titles)

    def test_merge_sort_ascending_client_rentals(self):
        # Merge sort for client rentals - Ascending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, key=lambda elem: elem[1])
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_rentals)

    def test_merge_sort_descending_client_rentals(self):
        # Merge sort for client rentals - Descending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, key=lambda elem: elem[1],
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_rentals)

    def test_merge_sort_ascending_client_names(self):
        # Merge sort for client names - Ascending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, key=lambda elem: elem[0].get_name())
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_ascending_name)

    def test_merge_sort_ascending_client_names(self):
        # Merge sort for client names - Descending
        client_list_tuples_sorted = sort_alg.merge_sort(self.client_list_tuples, key=lambda elem: elem[0].get_name(),
                                                        reverse=True)
        self.assertEqual(dict(client_list_tuples_sorted), self.sorted_client_database_descending_name)
