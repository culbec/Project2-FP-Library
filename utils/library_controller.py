import itertools
import random
import string
from datetime import datetime

from domain.entities import Book, Client, Rental
from repository.database import DatabaseFile
from repository.repository_book import BookRepositoryFile
from repository.repository_client import ClientRepositoryFile
from repository.repository_rental import RentalRepositoryFile
from validate.validate_book import BookValidator
from validate.validate_client import ClientValidator
from validate.validate_rental import RentalValidator


class LibraryController:
    def __init__(self):
        """
        Initializes the controller of our application.
        """
        self._book_repository = BookRepositoryFile("data/books.txt")
        self._book_validator = BookValidator()
        self._client_repository = ClientRepositoryFile("data/clients.txt")
        self._client_validator = ClientValidator()
        self._rental_repository = RentalRepositoryFile("data/rentals.txt")
        self._rental_validator = RentalValidator()
        self._database = DatabaseFile("data/database.txt")

    def get_book_list(self):
        return self.get_book_repo().get_book_list()

    def get_client_list(self):
        return self.get_client_repo().get_client_list()

    def get_rentals(self):
        return self.get_rental_repo().get_rentals_list()

    def get_database(self):
        return self._database

    def get_book_repo(self):
        return self._book_repository

    def get_book_valid(self):
        return self._book_validator

    def get_client_repo(self):
        return self._client_repository

    def get_client_valid(self):
        return self._client_validator

    def get_rental_repo(self):
        return self._rental_repository

    def get_rental_valid(self):
        return self._rental_validator

    def add_client_to_list_utils(self, client_name, client_cnp, client_subscription_year):
        """
        Adds a client to the library_controller's client_list
        :param client_name: str
        :param client_cnp: int
        :param client_subscription_year: int
        :return: nothing - just adds the client to the library_controller's client_list
        :raises ValueError: - if the client is not a valid one or if it already exists in the list.
        """
        client = Client(client_name, client_cnp, client_subscription_year)
        self.get_client_valid().validate_client(client, self)
        self.get_client_repo().add_client_to_list(client)

    def add_book_to_list_utils(self, book_id, book_title, book_author, book_year, book_volume):
        """
        Adds a book to the library_controller's book_list
        :param book_id: int
        :param book_title: str
        :param book_author: str
        :param book_year: int
        :param book_volume: str
        :return: -
        :raises ValueError - if the book is not a valid one or if it already exists in the list.
        """
        book_id = book_id + 1
        book = Book(book_id, book_title, book_author, book_year, book_volume)
        self.get_book_valid().validate_book(book)
        self.get_book_repo().add_book_to_list(book)

    @staticmethod
    def generate_random_string():
        """
        Generates a random string with lowercase and uppercase letters
        :return: a random string with lowercase and uppercase letters
        """
        first_string = ''.join(random.sample(string.ascii_letters, random.randrange(21)))
        last_string = ''.join(random.sample(string.ascii_letters, random.randrange(21)))
        result_string = f"{first_string} {last_string}"
        return result_string

    def generate_random_book(self):
        """
        Generates a random book with:
        * a random id in range [1, 100]
        * a random title
        * a random author
        * a random publish year in range [1680, {current_year}]
        * a random volume
        - the passed status of the book will still be 'Available', as a new book cannot be rented instantly
        :return: a random book with the passed random attributes, except status
        """
        book_id = random.randrange(1, 101)
        book_title = self.generate_random_string()
        book_author = self.generate_random_string()
        book_year = random.randrange(1680, int(datetime.now().year) + 1)
        book_volume = self.generate_random_string()
        book = Book(book_id, book_title, book_author, book_year, book_volume)
        self.get_book_repo().add_book_to_list(book)

    def modify_book_utils(self, book_id, book_title, book_author, book_year, book_volume):
        """
        Modifies a book with its identity equal to the passed identity.
        :param book_id: int
        :param book_title: str
        :param book_author: str
        :param book_year: str
        :param book_volume: str
        :return: -
        :raises ValueError: - if the title, author name, year, or volume are not valid
        """
        self.get_book_valid().validate_title(book_title)
        self.get_book_valid().validate_author_name(book_author)
        self.get_book_valid().validate_year(book_year)
        self.get_book_valid().validate_volume(book_volume)
        self.get_book_repo().modify_book(self.get_book_repo().search_book_by_id(book_id),
                                         book_title, book_author, book_year, book_volume)

    def delete_book_utils(self, book_id):
        """
        Deletes a book with its id equal to book_id
        :param book_id: int
        :return: nothing, just deletes that certain book
        """
        self.get_book_repo().delete_book(self.get_book_repo().search_book_by_id(book_id))

    def delete_client_utils(self, client_id):
        """
        Deletes a client with its id equal to client_id
        :param client_id: int
        :return: nothing, just deletes that certain client
        """
        self.get_client_repo().delete_client(self.get_client_repo().search_client_by_id(client_id))

    def modify_client_utils(self, client_id, client_name, client_sub_year):
        """
        Modifies a client with the client_id as id
        :param client_id: int
        :param client_name: str
        :param client_sub_year: int
        :return: nothing - just modifies the client in client_repo's client_list
        :raises ValueError: if any of the passed arguments are invalid
        """
        self.get_client_valid().validate_name(client_name)
        self.get_client_valid().validate_sub_year(client_sub_year)
        self.get_client_repo().modify_client(self.get_client_repo().search_client_by_id(client_id),
                                             client_name, client_sub_year)

    def search_book_by_title_utils(self, title):
        """
        Returns the list of books in library_controller's book_list that have the 'title' title
        :param title: str
        :return: a list of books with books in library_controller that have the 'title' title
        :raises ValueError: - if the passed title is not a string or the ' ' string
                              the associated string is: "The title needs to be a valid string."
                            - if a book with the passed title doesn't exist in library_controller's book_list
                              the associated string is: "Books with the passed title do not exist!"
        """
        self.get_book_valid().validate_title(title)
        book_list = []
        for book in self.get_book_list():
            if book.get_title() == title:
                book_list.append(book)
        if not book_list:
            raise ValueError("Books with the passed title do not exist!")
        return book_list

    def search_book_by_year_utils(self, year):
        """
        Returns the list of books in library_controller's book_list that have the 'year' year
        :param year: int
        :return: a list of books with books in library_controller that have the 'year' year
        :raises ValueError: - if the passed year is not a strictly positive integer between 1680 and current year
                              the associated string is: "The year needs to be a positive integer between
                                                         1680 and {current_year}."
                            - if a book with the year doesn't exist in library_controller's book_list
                              the associated string is: "Books with the passed release year do not exist!"
        """
        self.get_book_valid().validate_year(year)
        book_list = []
        for book in self.get_book_list():
            if book.get_year() == year:
                book_list.append(book)
        if not book_list:
            raise ValueError("Books with the passed release year do not exist!")
        return book_list

    def search_book_in_time_period(self, start_year, finish_year):
        """
        Returns a list of books in book_list that are published between start_year and finish_year
        :param start_year: int
        :param finish_year: int
        :return: a list of books in book_list that are published between start_year and finish_year
        :raises ValueError: - if either of the passed years are not strictly positive integers between 1680 and current
                              year
                              the associated string is: "{start_year}/{finish_year} is not a positive integer between
                                                         1680 and {current_year}."
                            - if no books where published in the specified time period
                              the associated string is: "There are no books published between {start_year}
                                                         and {finish_year}."
        """
        self.get_book_valid().validate_period(start_year, finish_year)
        book_list = [book for book in self.get_book_list() if start_year <= book.get_year() <= finish_year]
        if not book_list:
            raise ValueError(f"There are no books published between {start_year} and {finish_year}.")
        return book_list

    def search_client_by_name_utils(self, name):
        """
        Returns the list of clients in library_controller's client_list that have the 'name' name
        :param name: str
        :return: a list of clients with clients in library_controller's client_list that have the 'name' name
        :raises ValueError: - if the passed name is not a valid name
                              the associated string is: "The client's name needs to be a valid string."
                            - if a client with the passed name doesn't exist in library_controller's client_list
                              the associated string is: "Clients with the passed name do not exist!"
        """
        self.get_client_valid().validate_name(name)
        client_list = []
        for client in self.get_client_list():
            if client.get_name() == name:
                client_list.append(client)
        if not client_list:
            raise ValueError("Clients with the passed name do not exist!")
        return client_list

    def search_client_by_subscription_age_utils(self, sub_age):
        """
        Returns the list of clients in client_list that have their subscription age equal to 'sub_age'
        :param sub_age: int
        :return: a list of clients with clients in client_list that have their subscription age equal to 'sub_age'
        :raises ValueError: - if the sub_age is not an integer between 0 and 90
                              the associated string is: "The subscription age needs to be an integer between 0 and 90."
                            - if no clients with the passed subscription age exist in client_list
                              the associated string is: "Clients with the passed subscription age do not exist!"
        """
        self.get_client_valid().validate_subscription_age(sub_age)
        client_list = [client for client in self.get_client_list() if
                       datetime.now().year - client.get_subscription_year() == sub_age]
        if not client_list:
            raise ValueError("Clients with the passed subscription age do not exist!")
        return client_list

    def search_client_in_rentals(self):
        """
        Returns a list of clients which rented books
        :return: a list of clients which rented books
        :raises TypeError: - if no clients have rented books
                             the associated string is:"No clients have rented books."
        """
        client_list = []
        for rental in self.get_rentals():
            if rental.get_client() not in client_list:
                client_list.append(rental.get_client())
        if not client_list:
            raise TypeError("No clients have rented books.")
        return client_list

    def search_rental(self, rental_id):
        """
        Returns the rental that has its id equal to rental_id
        :param rental_id: str
        :return: the rental with its id equal to rental_id
        :raises ValueError: - if the no rental with the passed id exists
                              the associated string is: "The rental with the id {rental_id} couldn't be found!"
        """
        for rental in self.get_rentals():
            if rental.get_identity() == rental_id:
                return rental
        raise ValueError(f"The rental with the id {rental_id} couldn't be found!")

    def rent_book_utils(self, client_id, book_id):
        """
        Rents the book with its id equal to 'book_id' to the client with its id 'client_id'
        :param client_id: int
        :param book_id: int
        :return: -
        :raises ValueError: - if the book with the id 'book_id' is already rented
                            - the associated string is:"Book {book_title} is already rented!"
        """
        book = self.get_book_repo().search_book_by_id(book_id)
        for rental in self.get_rentals():
            if book == rental.get_book():
                raise ValueError(f"Book {book.get_title()} is already rented!")
        try:
            self._database.add_book_to_database(book)
        except ValueError:
            self._database.update_no_rentals_book(book)
        client = self.get_client_repo().search_client_by_id(client_id)
        try:
            self._database.add_client_to_database(client)
        except ValueError:
            self._database.update_no_rentals_client(client)
        rental = Rental(client, book)
        self.get_rental_valid().validate_rental(rental, self.get_rental_repo().get_rentals_list())
        self.get_rental_repo().add_rental_to_list(rental)

    def return_book_utils(self, rental_id):
        """
        Returns the rental with its id equal to rental_id
        :param rental_id = str
        :return: -
        """
        rental = self.search_rental(rental_id)
        self.get_rental_repo().delete_rental(rental)

    def most_rented_books(self):
        """
        Returns a new sorted dictionary with the values of the database's book list by their number of rentals
        in reverse order
        :return: a sorted book list of the database by the number of rentals of each book
        :raises ValueError: - if the book list of the database is clear
                              the associated string is: "The book list of the database is clear!"
        """
        if not self.get_database().get_book_list():
            raise ValueError("The book list of the database is clear!")
        sorted_tuple = sorted(self.get_database().get_book_list().items(), key=lambda item: item[1], reverse=True)
        return dict(sorted_tuple)

    def sort_clients_by_name_and_no_rentals(self):
        """
        Returns a new sorted dictionary with the values of the database's client list by their name and
        number of rentals
        :return: a sorted client list of the database by their name and number of rentals
        :raises ValueError: - if the client list of the database is clear
                              the associated string is: "The client list of the database is clear!"
        """
        if not self.get_database().get_client_list():
            raise ValueError("The client list of the database is clear!")
        sorted_by_name = sorted(self.get_database().get_client_list().items(), key=lambda item: item[0].get_name())
        sorted_dict = dict(sorted_by_name)
        sorted_tuple = sorted(sorted_dict.items(), key=lambda item: item[1], reverse=True)
        return dict(sorted_tuple)

    def first_20_percent_most_active_clients(self):
        """
        Shows the first 20% most active clients sorted by name and number of books rented
        If the number of the clients expressed in the 20% is < 1.00, then it will show all the clients sorted
        in the proposed order
        If the number of the clients is not an integer number, then it will be floored
        and then transformed in an integer
        :return: the first 20% of a sorted client list of the database by their name and number of rentals
        :raises ValueError: - if the client list of the database is clear
                              the associated string is: "The client list of the database is clear!"
        """
        if not self.get_database().get_client_list():
            raise ValueError("The client list of the database is clear!")
        sorted_dict = self.sort_clients_by_name_and_no_rentals()
        number_of_clients = (20.0 * len(sorted_dict)) / 100
        if number_of_clients < 1.0:
            return sorted_dict
        else:
            number_of_clients = int(number_of_clients)
            new_sorted_dict = dict(itertools.islice(sorted_dict.items(), 0, number_of_clients))
            return new_sorted_dict

    def sort_books_by_name(self):
        """
        Returns a sorted book list by their names
        :return: a sorted book list by their names
        :raises ValueError: - if the book list is clear
                              the associated string is: "The book list of the database is clear!"
        """
        if not self.get_database().get_book_list():
            raise ValueError("The book list of the database is clear!")
        sorted_tuple = sorted(self.get_database().get_book_list().items(), key=lambda item: item[0].get_title())
        return dict(sorted_tuple)
