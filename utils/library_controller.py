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
        # will be completed with books
        self._book_list = []
        # will be completed with clients
        self._client_list = []
        # will be completed with {client : [{list of books}]}
        self._client_books = {}
        self._book_controller = BookController()
        self._client_controller = ClientController()

    def get_book_list(self):
        return self._book_list

    def get_client_list(self):
        return self._client_list

    def get_client_books(self):
        return self._client_books

    def set_book_list(self, book_list):
        self._book_list = book_list

    def set_client_list(self, client_list):
        self._client_list = client_list

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

    @classmethod
    def add_client_to_list_utils(cls, client_id, client_name, client_cnp, client_subscription_year, library_controller):
        """
        Adds a client to the library_controller's client_list
        :param client_id: int
        :param client_name: str
        :param client_cnp: int
        :param client_subscription_year: int
        :param library_controller: LibraryController
        :return: nothing - just adds the client to the library_controller's client_list
        :raises ValueError: - if the client is not a valid one or if it already exists in the list.
        """
        client_id = client_id + 1
        client = library_controller.use_client_repository().create_client(client_id,
                                                                          client_name,
                                                                          client_cnp,
                                                                          client_subscription_year)
        library_controller.use_client_validator().validate_client(client, library_controller)
        library_controller.use_client_repository().add_client_to_list(client, library_controller)

    @classmethod
    def add_book_to_list_utils(cls, book_id, book_title, book_author, book_year, book_volume, library_controller):
        """
        Adds a book to the library_controller's book_list
        :param book_id: int
        :param book_title: str
        :param book_author: str
        :param book_year: int
        :param book_volume: str
        :param library_controller: LibraryController
        :return: -
        :raises ValueError - if the book is not a valid one or if it already exists in the list.
        """
        book_id = book_id + 1
        book = library_controller.use_book_repository().create_book(book_id,
                                                                    book_title,
                                                                    book_author,
                                                                    book_year,
                                                                    book_volume)
        library_controller.use_book_validator().validate_book(book)
        library_controller.use_book_repository().add_book_to_list(book, library_controller)

    @staticmethod
    def search_book_by_title_utils(title, library_controller):
        """
        Returns the list of books in library_controller's book_list that have the 'title' title
        :param title: str
        :param library_controller: LibraryController
        :return: a list of books with books in library_controller that have the 'title' title
        :raises ValueError: - if the passed title is not a string or the ' ' string
                              the associated string is: "The title needs to be a valid string."
                            - if a book with the passed title doesn't exist in library_controller's book_list
                              the associated string is: "Books with the passed title do not exist!
        """
        library_controller.use_book_validator().validate_title(title)
        return library_controller.use_book_repository().search_book_by_title(title, library_controller)

    @staticmethod
    def search_book_by_year_utils(year, library_controller):
        """
        Returns the list of books in library_controller's book_list that have the 'year' year
        :param year: int
        :param library_controller: LibraryController
        :return: a list of books with books in library_controller that have the 'year' year
        :raises ValueError: - if the passed year is not a strictly positive integer between 1680 and current year
                              the associated string is: "The year needs to be a positive integer between
                                                         1680 and {current_year}."
                            - if a book with the year doesn't exist in library_controller's book_list
                              the associated string is: "Books with the passed release year do not exist!"
        """
        library_controller.use_book_validator().validate_year(year)
        return library_controller.use_book_repository().search_book_by_year(year, library_controller)

    @staticmethod
    def search_client_by_name_utils(name, library_controller):
        """
        Returns the list of clients in library_controller's client_list that have the 'name' name
        :param name: str
        :param library_controller: LibraryController
        :return: a list of clients with clients in library_controller's client_list that have the 'name' name
        :raises ValueError: - if the passed name is not a valid name
                              the associated string is: "The client's name needs to be a valid string."
                            - if a client with the passed name doesn't exist in library_controller's client_list
                              the associated string is: "Clients with the passed name do not exist!"
        """
        library_controller.use_client_validator().validate_name(name)
        return library_controller.use_client_repository().search_client_by_name(name, library_controller)
