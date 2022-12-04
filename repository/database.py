# Keeps track of all the books and clients and their number of rentals that ever existed in this app
import io

from domain.entities import Book, Client


class Database:
    def __init__(self):
        self._books = {}
        self._clients = {}

    def get_book_list(self):
        return self._books

    def get_client_list(self):
        return self._clients

    def book_in_database(self, book):
        """
        Verifies if the book is in the database
        :param book: Book
        :return: the book if the book is in the database
        :raises ValueError: - if the book is not in the database
                              the associated string is: "The book is not in the database!"
        """
        for _book in self.get_book_list().keys():
            if (book.get_title() == _book.get_title() and
                    book.get_author() == _book.get_author() and
                    book.get_year() == _book.get_year() and
                    book.get_volume() == _book.get_volume()):
                return _book
        return False

    def client_in_database(self, client):
        """
        Verifies if the client is in the database
        :param client: Client
        :return: the client if the client is in the database
        :raises ValueError: - if the client is not in the database
                              the associated string is: "The client is not in the database!"
        """
        for _client in self.get_client_list().keys():
            if (client.get_name() == _client.get_name() and
                    client.get_cnp() == _client.get_cnp() and
                    client.get_subscription_year() == _client.get_subscription_year()):
                return _client
        return False

    def add_book_to_database(self, book):
        """
        Adds a passed book to the database
        :param book: Book
        :return: -
        :raises ValueError: - if the same book already exists in the database
                              the associated string is: "The book already exists in the database!"
        """
        if not self.book_in_database(book):
            self.get_book_list().update({book: 1})
        else:
            raise ValueError("The book already exists in the database!")

    def add_client_to_database(self, client):
        """
        Adds a passed client to the database
        :param client: Client
        :return: -
        :raises ValueError: - if the same client already exists in the database
                              the associated string is: "The client already exists in the database!"
        """
        if not self.client_in_database(client):
            self.get_client_list().update({client: 1})
        else:
            raise ValueError("The client already exists in the database!")

    def update_no_rentals_book(self, book):
        """
        Updates the number of rentals for a passed book
        :param book: Book
        :return: -
        :raises ValueError: - if the book doesn't exist in the database
                              the associated string is: "The book is not in the database!"
        """
        if self.book_in_database(book):
            self.get_book_list()[self.book_in_database(book)] = int(
                self.get_book_list()[self.book_in_database(book)]) + 1
        else:
            raise ValueError("The book is not in the database!")

    def update_no_rentals_client(self, client):
        """
        Updates the number of rentals that a passed client has made
        :param client: Client
        :return: -
        :raises ValueError: - if the client doesn't exist in the database
                              the associated string is: "The client is not in the database!"
        """
        if self.client_in_database(client):
            self.get_client_list()[self.client_in_database(client)] = \
                self.get_client_list()[self.client_in_database(client)] + 1
        else:
            raise ValueError("The client is not in the database!")


class DatabaseFile(Database):
    def __init__(self, filename):
        Database.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _load_from_file(self):
        try:
            file = io.open(self._filename, mode='r', encoding='utf-8')
        except IOError:
            return

        lines = file.readlines()
        for line in lines:
            try:
                book_id, book_title, book_author, book_year, book_volume, \
                    book_rentals = [token.strip() for token in line.split(';')]
                book = Book(int(book_id), book_title, book_author, int(book_year), book_volume)
                self.get_book_list().update({book: int(book_rentals)})
            except ValueError:
                client_id, client_name, client_cnp, client_sub_year, \
                    client_rentals = [token.strip() for token in line.split(';')]
                client = Client(client_name, int(client_cnp), int(client_sub_year))
                self.get_client_list().update({client: int(client_rentals)})
        file.close()

    def _save_to_file(self):
        book_list = self.get_book_list()
        client_list = self.get_client_list()
        with io.open(self._filename, mode='w', encoding='utf-8') as file:
            for book, noRentals in book_list.items():
                book_str = f"{book.get_identity()} ; {book.get_title()} ; {book.get_author()} ; {book.get_year()} ; " \
                           f"{book.get_volume()} ; {int(noRentals)}\n"
                file.write(book_str)
            for client, noRentals in client_list.items():
                client_str = f"{client.get_identity()} ; {client.get_name()} ; {client.get_cnp()} ; " \
                             f"{client.get_subscription_year()} ; {int(noRentals)}\n"
                file.write(client_str)

    def _clear_file(self):
        with io.open(self._filename, mode='w', encoding='utf-8'):
            pass

    def add_book_to_database(self, book):
        Database.add_book_to_database(self, book)
        self._save_to_file()

    def add_client_to_database(self, client):
        Database.add_client_to_database(self, client)
        self._save_to_file()

    def update_no_rentals_book(self, book):
        Database.update_no_rentals_book(self, book)
        self._save_to_file()

    def update_no_rentals_client(self, client):
        Database.update_no_rentals_client(self, client)
        self._save_to_file()
