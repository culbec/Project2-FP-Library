import unittest
from datetime import datetime

from utils.library_controller import LibraryController


class TestCasesLibraryController(unittest.TestCase):
    def setUp(self) -> None:
        self._controller = LibraryController()
        self._controller.get_book_repo()._clear_file()
        self._controller.get_client_repo()._clear_file()
        self._controller.get_rental_repo()._clear_file()
        self._controller.get_database()._clear_file()

    def tearDown(self) -> None:
        self._controller.get_book_repo()._clear_file()
        self._controller.get_client_repo()._clear_file()
        self._controller.get_rental_repo()._clear_file()
        self._controller.get_database()._clear_file()

    def test_add_client_to_list_utils(self):
        self.assertFalse(self._controller.get_client_list())

        self._controller.add_client_to_list_utils('Vasile Pop', 5010203111222, 2009)
        self.assertTrue(self._controller.get_client_list())
        self.assertEqual(len(self._controller.get_client_list()), 1)

        self.assertRaises(ValueError, self._controller.add_client_to_list_utils, 'Vasi 33', 5113344666777, 1900)
        self._controller.add_client_to_list_utils('Maria Y', 6112233555666, 2010)
        self.assertEqual(len(self._controller.get_client_list()), 2)

    # Black box testing for this method in the controller class
    # raises ValueError if the passed parameters are not valid for creating a book with them
    def test_add_book_to_list_utils(self):
        self.assertFalse(self._controller.get_book_list())
        self._controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                                1892, 'Amintiri din copilarie')
        self.assertTrue(self._controller.get_book_list())
        self.assertEqual(len(self._controller.get_book_list()), 1)

        self.assertRaises(ValueError, self._controller.add_book_to_list_utils, 1, 123, '501', '', 1)
        self._controller.add_book_to_list_utils(100, 'The Great Gatsby', 'F. Scott Fitzgerald',
                                                1928, 'The Great Gatsby')
        self.assertEqual(len(self._controller.get_book_list()), 2)

    def test_search_book_by_title_utils(self):
        self._controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                                1892, 'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(2, 'Amintiri din copilarie', 'Ion Creanga',
                                                1892, 'Amintiri din copilarie')
        book_list = self._controller.search_book_by_title_utils('Amintiri din copilarie')
        self.assertTrue(book_list)
        self.assertEqual(len(book_list), 2)

        self.assertRaises(ValueError, self._controller.search_book_by_title_utils, '')
        self.assertRaises(ValueError, self._controller.search_book_by_title_utils, 'Amintiri...')
        self.assertRaises(ValueError, self._controller.search_book_by_title_utils, 1)

    def test_search_book_by_year_utils(self):
        self._controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga',
                                                1892, 'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(2, 'Amintiri din copilarie', 'Ion Creanga',
                                                1892, 'Amintiri din copilarie')
        book_list = self._controller.search_book_by_year_utils(1892)
        self.assertTrue(book_list)
        self.assertEqual(len(book_list), 2)

        self.assertRaises(ValueError, self._controller.search_book_by_year_utils, 1450)
        self.assertRaises(ValueError, self._controller.search_book_by_year_utils, 2021)
        self.assertRaises(ValueError, self._controller.search_book_by_year_utils, '')

    def test_search_book_in_time_period(self):
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga',
                                                1892, 'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga',
                                                1881, 'Basme din popor')
        self._controller.add_book_to_list_utils(2, 'Ulysses', 'James Grant',
                                                1920, 'Ulysses')
        self.assertEqual(len(self._controller.search_book_in_time_period(1800, 2000)), 3)

        self.assertRaises(ValueError, self._controller.search_book_in_time_period, 1560, 2000)
        self.assertRaises(ValueError, self._controller.search_book_in_time_period, 1700, int(datetime.now().year) + 5)
        self.assertRaises(ValueError, self._controller.search_book_in_time_period, 't123', 1900)
        self.assertRaises(ValueError, self._controller.search_book_in_time_period, 1700, 'y1533')

    def test_search_client_by_name_utils(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5111122333444, 2019)
        self._controller.add_client_to_list_utils('Vasile Pop', 6111222333444, 2010)

        self.assertEqual(len(self._controller.search_client_by_name_utils('Vasile Pop')), 2)

        self.assertRaises(ValueError, self._controller.search_client_by_name_utils, 'Vasil Pop')
        self.assertRaises(ValueError, self._controller.search_client_by_name_utils, 'Vasil1 P0p')
        self.assertRaises(ValueError, self._controller.search_client_by_name_utils, 1)

    def test_search_client_by_subscription_age_utils_utils(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
        self._controller.add_client_to_list_utils('Ion X', 5030201666111, 2016)

        self.assertEqual(len(self._controller.search_client_by_subscription_age_utils(6)), 2)

        self.assertRaises(ValueError, self._controller.search_client_by_subscription_age_utils, 5)
        self.assertRaises(ValueError, self._controller.search_client_by_subscription_age_utils, '1')
        self.assertRaises(ValueError, self._controller.search_client_by_subscription_age_utils, 91)

    def test_search_client_rented_books(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.rent_book_utils(5030102111666, 1)
        self.assertEqual(len(self._controller.search_client_in_rentals()), 1)

        self._controller.return_book_utils("5030102111666_1")

        self.assertRaises(TypeError, self._controller.search_client_in_rentals)

    def test_search_rental(self):
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
        self._controller.add_client_to_list_utils('Ion X', 5030201666111, 2016)
        self._controller.rent_book_utils(5030102111666, 1)
        self.assertTrue(self._controller.search_rental("5030102111666_1"))
        self.assertRaises(ValueError, self._controller.search_rental, "6030102111666_1")

    def test_modify_book_utils(self):
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.modify_book_utils(1, 'Baltagul', 'Mihail Sadoveanu', 1928, 'Baltagul')
        self.assertEqual(self._controller.get_book_list()[0].get_title(), 'Baltagul')

        self.assertRaises(ValueError, self._controller.modify_book_utils, 1, 'abc1', 23, '1231', 54)

    def test_modify_client_utils(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
        self._controller.add_client_to_list_utils('Maria Y', 6010203111666, 2018)

        self._controller.modify_client_utils(5030102111666, 'Ion X', 2019)
        self.assertEqual(self._controller.get_client_list()[0].get_subscription_year(), 2019)

        self.assertRaises(ValueError, self._controller.modify_client_utils, 6010203111666, 'Maria Y', '201e')

    def test_delete_book_utils(self):
        self.assertFalse(self._controller.get_book_list())
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                                'Povestea lui Harap-Alb')
        self.assertTrue(self._controller.get_book_list())
        self.assertEqual(len(self._controller.get_book_list()), 2)
        self._controller.delete_book_utils(1)
        self.assertEqual(len(self._controller.get_book_list()), 1)
        self._controller.delete_book_utils(2)
        self.assertFalse(self._controller.get_book_list())
        self.assertRaises(ValueError, self._controller.delete_book_utils, 5)

    def test_delete_client_utils(self):
        self.assertFalse(self._controller.get_client_list())
        self._controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
        self._controller.add_client_to_list_utils('Ion X', 5010203222666, 2019)

        self.assertTrue(self._controller.get_client_list())
        self.assertEqual(len(self._controller.get_client_list()), 2)
        self._controller.delete_client_utils(5030102111666)
        self.assertEqual(len(self._controller.get_client_list()), 1)
        self._controller.delete_client_utils(5010203222666)
        self.assertFalse(self._controller.get_client_list())
        self.assertRaises(ValueError, self._controller.delete_client_utils, 5010302111666)

    def test_rent_book_utils(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5030201111666, 2016)
        self._controller.add_client_to_list_utils('Ion X', 5010203666111, 2019)
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                                'Basme din popor')
        self._controller.rent_book_utils(5030201111666, 1)
        self.assertTrue(self._controller.get_rentals())
        self.assertEqual(self._controller.get_database().get_book_list()[self._controller.get_book_list()[0]], 1)
        self.assertEqual(self._controller.get_rentals()[0].get_client().get_identity(), 5030201111666)

        self.assertRaises(ValueError, self._controller.rent_book_utils, 5010203666111, 1)

    def test_return_book_utils(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5030102111666, 2016)
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881,
                                                'Basme din popor')
        self._controller.rent_book_utils(5030102111666, 1)
        self.assertTrue(self._controller.get_rentals())
        self.assertEqual(len(self._controller.get_rentals()), 1)
        self._controller.rent_book_utils(5030102111666, 2)
        self.assertEqual(len(self._controller.get_rentals()), 2)
        self._controller.return_book_utils("5030102111666_1")
        self.assertEqual(len(self._controller.get_rentals()), 1)
        self._controller.return_book_utils("5030102111666_2")
        self.assertFalse(self._controller.get_rentals())

    def test_generate_random_book(self):
        self.assertFalse(self._controller.get_book_list())
        self._controller.generate_random_book()
        self._controller.generate_random_book()
        self.assertTrue(self._controller.get_book_list())
        self.assertEqual(len(self._controller.get_book_list()), 2)

    def test_most_rented_books(self):
        self._controller.add_book_to_list_utils(0, 'Amintiri din copilarie', 'Ion Creanga', 1892,
                                                'Amintiri din copilarie')
        self._controller.add_book_to_list_utils(1, 'Povestea lui Harap-Alb', 'Ion Creanga', 1881, 'Basme din popor')
        self._controller.add_book_to_list_utils(2, 'Ulysses', 'James Grant', 1922, 'Ulysses')

        self.assertRaises(ValueError, self._controller.most_rented_books)

        self._controller.get_database().add_book_to_database(self._controller.get_book_list()[0])
        self._controller.get_database().add_book_to_database(self._controller.get_book_list()[1])
        self._controller.get_database().add_book_to_database(self._controller.get_book_list()[2])

        self._controller.get_database().get_book_list()[self._controller.get_book_list()[0]] = 200
        self._controller.get_database().get_book_list()[self._controller.get_book_list()[1]] = 400
        self._controller.get_database().get_book_list()[self._controller.get_book_list()[2]] = 500

        most_rented_books = self._controller.most_rented_books()

        self.assertEqual(most_rented_books, {self._controller.get_book_list()[2]: 500,
                                             self._controller.get_book_list()[1]: 400,
                                             self._controller.get_book_list()[0]: 200})

    def test_sort_clients_by_name_and_no_rentals(self):
        self._controller.add_client_to_list_utils('Vasile Popa', 5030102111666, 2016)
        self._controller.add_client_to_list_utils('Vasile Pop', 6010203555312, 2012)
        self._controller.add_client_to_list_utils('Maria Y', 4010231555341, 2011)

        self.assertRaises(ValueError, self._controller.sort_clients_by_name_and_no_rentals)

        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[0])
        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[1])
        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[2])

        self._controller.get_database().get_client_list()[self._controller.get_client_list()[0]] = 7000
        self._controller.get_database().get_client_list()[self._controller.get_client_list()[1]] = 7000
        self._controller.get_database().get_client_list()[self._controller.get_client_list()[2]] = 19

        sorted_dict = self._controller.sort_clients_by_name_and_no_rentals()

        self.assertEqual(sorted_dict, {self._controller.get_client_list()[1]: 7000,
                                       self._controller.get_client_list()[0]: 7000,
                                       self._controller.get_client_list()[2]: 19})

    def test_first_20_percent_most_active_clients(self):
        self._controller.add_client_to_list_utils('Vasile Pop', 5010203541531, 2016)
        self._controller.add_client_to_list_utils('Vasile Popa', 4010302541222, 2012)
        self._controller.add_client_to_list_utils('Ion Minulescu', 3043133879111, 2000)

        self.assertRaises(ValueError, self._controller.first_20_percent_most_active_clients)

        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[0])
        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[2])
        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[1])

        self._controller.get_database().get_client_list()[self._controller.get_client_list()[0]] = 7000
        self._controller.get_database().get_client_list()[self._controller.get_client_list()[1]] = 801
        self._controller.get_database().get_client_list()[self._controller.get_client_list()[2]] = 651

        sorted_dict = self._controller.first_20_percent_most_active_clients()
        self.assertEqual(sorted_dict, {self._controller.get_client_list()[0]: 7000,
                                       self._controller.get_client_list()[1]: 801,
                                       self._controller.get_client_list()[2]: 651})

        self._controller.add_client_to_list_utils('Maria Ioana', 6001002223331, 2012)
        self._controller.add_client_to_list_utils('Flavius X', 1020302111444, 2010)

        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[3])
        self._controller.get_database().add_client_to_database(self._controller.get_client_list()[4])

        another_sorted_dict = self._controller.first_20_percent_most_active_clients()
        assert another_sorted_dict == {self._controller.get_client_list()[0]: 7000}

    def test_sort_books_by_name(self):
        self._controller.add_book_to_list_utils(0, "Amintiri din copilarie", "Ion Creanga", 1892,
                                                "Amintiri din copilarie")
        self._controller.add_book_to_list_utils(1, "Povestea lui Harap-Alb", "Ion Creanga", 1881,
                                                "Basme din popor")
        self._controller.add_client_to_list_utils("Vasile Pop", 5030102111666, 2016)

        self.assertRaises(ValueError, self._controller.sort_books_by_name)

        self._controller.rent_book_utils(5030102111666, 1)
        self._controller.rent_book_utils(5030102111666, 2)

        self.assertEqual(self._controller.sort_books_by_name(), {self._controller.get_book_list()[0]: 1,
                                                                 self._controller.get_book_list()[1]: 1})
