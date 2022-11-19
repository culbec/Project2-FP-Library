from datetime import datetime

from domain.book import Book
from domain.client import Client
from repository.repository_book import BookRepository
from validate.validate_book import BookValidator
from repository.repository_client import ClientRepository
from validate.validate_client import ClientValidator


class BookController:
    def __init__(self):
        self._book_repository = BookRepository()
        self._book_validator = BookValidator()

    def get_book_repository(self):
        return self._book_repository

    def get_book_validator(self):
        return self._book_validator


class ClientController:
    def __init__(self):
        self._client_repository = ClientRepository()
        self._client_validator = ClientValidator()

    def get_client_repository(self):
        return self._client_repository

    def get_client_validator(self):
        return self._client_validator


class LibraryController:
    def __init__(self):
        """
        Initializes the controller of our application.
        """
        self._client_books = {}
        self._book_controller = BookController()
        self._client_controller = ClientController()

    # def get_book_list(self):
        # return self._book_controller.get_book_repository().get_book_list()
    def get_book_list(self):
        return self._book_controller.get_book_repository().get_book_list()

    def get_client_list(self):
        return self._client_controller.get_client_repository().get_client_list()

    def get_client_books(self):
        return self._client_books

    def get_client_rented_books(self, client_id):
        return self._client_books[client_id]

    # def set_book_list(self, book_list):
        # self._book_list = book_list
    def set_book_list(self, book_list):
        self._book_controller.get_book_repository()._book_list = book_list

    def set_client_list(self, client_list):
        self._client_controller.get_client_repository()._client_list = client_list

    def set_client_books(self, client_books):
        self._client_books = client_books

    def use_book_repository(self):
        return self._book_controller.get_book_repository()

    def use_book_validator(self):
        return self._book_controller.get_book_validator()

    def use_client_repository(self):
        return self._client_controller.get_client_repository()

    def use_client_validator(self):
        return self._client_controller.get_client_validator()

    def add_client_to_list_utils(self, client_name, client_cnp, client_subscription_year):
        """
        Adds a client to the library_controller's client_list
        :param client_name: str
        :param client_cnp: int
        :param client_subscription_year: int
        :return: nothing - just adds the client to the library_controller's client_list
        :raises ValueError: - if the client is not a valid one or if it already exists in the list.
        """
        client = Client(client_cnp, client_name, client_cnp, client_subscription_year)
        self.use_client_validator().validate_client(client, self)
        self.use_client_repository().add_client_to_list(client)

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
        self.use_book_validator().validate_book(book)
        self.use_book_repository().add_book_to_list(book)

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
        self.use_book_validator().validate_title(book_title)
        self.use_book_validator().validate_author_name(book_author)
        self.use_book_validator().validate_year(book_year)
        self.use_book_validator().validate_volume(book_volume)
        self.use_book_repository().modify_book(self.use_book_repository().search_book_by_id(book_id),
                                               book_title, book_author, book_year, book_volume)

    def delete_book_utils(self, book_id):
        """
        Deletes a book with its id equal to book_id
        :param book_id: int
        :return: nothing, just deletes that certain book
        """
        self.use_book_repository().delete_book(self.use_book_repository().search_book_by_id(book_id))

    def delete_client_utils(self, client_id):
        """
        Deletes a client with its id equal to client_id
        :param client_id: int
        :return: nothing, just deletes that certain client
        """
        self.use_client_repository().delete_client(self.use_client_repository().search_client_by_id(client_id))

    def modify_client_utils(self, client_id, client_name, client_sub_year):
        """
        Modifies a client with the client_id as id
        :param client_id: int
        :param client_name: str
        :param client_sub_year: int
        :return: nothing - just modifies the client in client_repo's client_list
        :raises ValueError: if any of the passed arguments are invalid
        """
        self.use_client_validator().validate_name(client_name)
        self.use_client_validator().validate_sub_year(client_sub_year)
        self.use_client_repository().modify_client(self.use_client_repository().search_client_by_id(client_id),
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
        self.use_book_validator().validate_title(title)
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
        self.use_book_validator().validate_year(year)
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
        self.use_book_validator().validate_period(start_year, finish_year)
        book_list = [book for book in self.get_book_list() if start_year <= book.get_year() <= finish_year]
        if not book_list:
            raise ValueError(f"There are no books published between {start_year} and {finish_year}.")
        return book_list

    def search_book_by_status_utils(self, status):
        """
        Returns a list of books in book_list that have the status equal to 'status'.
        :param status: str
        :return: a list of books in book_list that have the status equal to 'status'
        :raises ValueError: - if the passed status is not 'Available' or 'Rented'
                              the associated string is: "The searched status needs to be 'Available' or 'Rented'."
                            - if no books have their status equal to 'status':
                              the associated string is: f"There are no books with the status {status}."
        """
        self.use_book_validator().validate_status(status)
        book_list = [book for book in self.get_book_list() if book.get_status() == status]
        if not book_list:
            raise ValueError(f"There are no books with the status {status}.")
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
        self.use_client_validator().validate_name(name)
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
        self.use_client_validator().validate_subscription_age(sub_age)
        client_list = [client for client in self.get_client_list() if
                       datetime.now().year - client.get_subscription_year() == sub_age]
        if not client_list:
            raise ValueError("Clients with the passed subscription age do not exist!")
        return client_list

    def search_client_rented_books(self):
        """
        Returns a list of clients which rented books
        :return: a list of clients which rented books
        :raises TypeError: - if no clients have rented books
                             the associated string is:"No clients have rented books."
        """
        client_list = [client for client in self.get_client_list() if client in self.get_client_books().keys()]
        if not client_list:
            raise TypeError("No clients have rented books.")
        return client_list

    def rent_book_utils(self, client_id, book_id):
        """
        Rents the book with its id equal to 'book_id' to the client with its id 'client_id'
        :param client_id: int
        :param book_id: int
        :return: -
        :raises ValueError: - if the book with the id 'book_id' is already rented
                            - the associated string is:"Book {book_title} is already rented!"
        """
        book = self.use_book_repository().search_book_by_id(book_id)
        if book.get_status() == 'Rented':
            raise ValueError(f"Book {book.get_title()} is already rented!")
        book.set_status('Rented')
        client = self.use_client_repository().search_client_by_id(client_id)
        if client not in self.get_client_books().keys():
            self.get_client_books().update({client: [book]})
        else:
            self.get_client_books()[client].extend([book])

    def return_book_utils(self, client_id, book_id):
        """
        Returns the book with its id equal to 'book_id' from the client with its id 'client_id'
        :param client_id: int
        :param book_id: int
        :return: -
        """
        book = self.use_book_repository().search_book_by_id(book_id)
        client = self.use_client_repository().search_client_by_id(client_id)
        self.get_client_books()[client].remove(book)
        book.set_status('Available')
        if not self.get_client_books()[client]:
            del self.get_client_books()[client]
