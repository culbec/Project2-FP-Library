from utils.library_controller import LibraryController


class UI:
    def __init__(self):
        self._controller = LibraryController()
        self._number_books = 0
        self._number_clients = 0

    def _print_book_list(self):
        """
        Prints a list of all books saved.
        """
        book_dict = self._controller.get_book_dict()
        if len(book_dict) == 0:
            print("There are no books saved.")
        else:
            print("The book list is:\n")
            for book in book_dict.values():
                print(f"[{book.get_identity()}] {book.get_title()} by {book.get_author()} published in "
                      f"{book.get_year()} in the volume {book.get_volume()} with the status '{book.get_status()}'.")

    def _print_client_list(self):
        """
        Prints a list of all clients saved.
        """
        client_list = self._controller.get_client_list()
        if len(client_list) == 0:
            print("There are no clients saved.")
        else:
            print("The client list is:\n")
            for client in client_list:
                print(f"[{client.get_identity()}] {client.get_name()} with the CNP {client.get_cnp()} "
                      f"subscribed in {client.get_subscription_year()}.")

    def _add_book(self):
        """
        Adds a book with the given data.
        """
        title = input("Book title: ")
        author = input("Book author: ")
        year = input("Book release year: ")
        volume = input("Book volume: ")
        title.strip()
        author.strip()
        year.strip()
        volume.strip()
        try:
            year = int(year)
        except ValueError:
            print("The publish year needs to be an integer.")
            return
        try:
            self._controller.add_book_to_list_utils(self._number_books, title, author, year, volume, self._controller)
            print(f"The book {title} by {author} published in {year} in the volume {volume} was added successfully!")
            self._number_books = self._number_books + 1
        except ValueError as ve:
            print(str(ve))

    def _add_client(self):
        """
        Adds a client with the given data.
        """
        name = input("Client name: ")
        cnp = input("Client's CNP: ")
        subscription_year = input("Client's subscription year: ")
        name.strip()
        cnp.strip()
        subscription_year.strip()
        try:
            cnp = int(cnp)
        except ValueError:
            print("The client's CNP needs to be an integer.")
            return
        try:
            subscription_year = int(subscription_year)
        except ValueError:
            print("The client's subscription year needs to be a strictly positive integer.")
            return
        try:
            self._controller.add_client_to_list_utils(self._number_clients,
                                                      name, cnp, subscription_year, self._controller)
            print(f"The client {name} with the CNP {cnp} subscribed in {subscription_year} was added successfully!")
            self._number_clients = self._number_clients + 1
        except ValueError as ve:
            print(str(ve))

    def _search_book_by_title(self):
        """
        Prints a list of books with a given title
        """
        title = input("Title: ")
        try:
            book_list = self._controller.search_book_by_title_utils(title, self._controller)
            for book in book_list:
                print(f"[{book.get_identity()}] {book.get_title()} by {book.get_author()} published in "
                      f"{book.get_year()} in the volume {book.get_volume()} with the status '{book.get_status()}'")
        except ValueError as ve:
            print(str(ve))

    def _search_book_by_year(self):
        """
        Prints a list of books with a given publish year
        """
        year = input("Publish year: ")
        try:
            year = int(year)
        except ValueError:
            print("The year needs to be an integer.")
        try:
            book_list = self._controller.search_book_by_year_utils(year, self._controller)
            for book in book_list:
                print(f"[{book.get_identity()}] {book.get_title()} by {book.get_author()} published in "
                      f"{book.get_year()} in the volume {book.get_volume()} with the status '{book.get_status()}'")
        except ValueError as ve:
            print(str(ve))

    def _search_client_by_name(self):
        """
        Prints a list of clients with a give name
        """
        name = input("Name: ")
        try:
            client_list = self._controller.search_client_by_name_utils(name, self._controller)
            for client in client_list:
                print(f"[{client.get_identity()}] {client.get_name()} with the CNP {client.get_cnp()} "
                      f"subscribed in {client.get_subscription_year()}")
        except ValueError as ve:
            print(str(ve))

    def run_ui(self):
        while True:
            print("Available commands:")
            print("1. Print")
            print("2. Books")
            print("3. Clients")
            print("Type 'exit' to close the app.")

            option = input("Your option? ")
            if option == 'exit':
                print("Closing the application. Bye!")
                return

            elif option == '1':
                while True:
                    print("1. Print the book list")
                    print("2. Print the client list")
                    print("Type 'exit' to return")
                    option_print = input("Your option? ")
                    if option_print == 'exit':
                        print("Closing the sub-menu...\n")
                        break
                    elif option_print == '1':
                        self._print_book_list()
                        print("\n")
                    elif option_print == '2':
                        self._print_client_list()
                        print("\n")
                    else:
                        print("Invalid command!")
            elif option == '2':
                while True:
                    print("1. Add book to list")
                    print("2. Search")
                    print("Type 'exit' to return")
                    option_book = input("Your option? ")
                    if option_book == 'exit':
                        print("Closing the sub-menu...\n")
                        break
                    elif option_book == '1':
                        self._add_book()
                        print("\n")
                    elif option_book == '2':
                        while True:
                            print("1. Search book by title")
                            print("2. Search book by publish year")
                            print("Type 'exit' to return")
                            option_search_book = input("Your option? ")
                            if option_search_book == 'exit':
                                print("Closing the sub-menu...\n")
                                break
                            elif option_search_book == '1':
                                self._search_book_by_title()
                                print("\n")
                            elif option_search_book == '2':
                                self._search_book_by_year()
                                print("\n")
                            else:
                                print("Invalid command!")
                    else:
                        print("Invalid command!")
            elif option == '3':
                while True:
                    print("1. Add client to list")
                    print("2. Search")
                    print("Type 'exit' to return")
                    option_client = input("Your option? ")
                    if option_client == 'exit':
                        print("Closing the sub-menu...\n")
                        break
                    elif option_client == '1':
                        self._add_client()
                    elif option_client == '2':
                        print("1. Search client by name")
                        print("Type 'exit' to return")
                        while True:
                            option_search_client = input("Your option? ")
                            if option_search_client == 'exit':
                                print("Closing the sub-menu...\n")
                                break
                            elif option_search_client == '1':
                                self._search_client_by_name()
                            else:
                                print("Invalid command!")
                    else:
                        print("Invalid command!")
            else:
                print("Invalid command!")
