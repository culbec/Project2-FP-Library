from utils.library_controller import LibraryController


class UI:
    def __init__(self):
        self._controller = LibraryController()
        self._number_books = 0
        if self._controller.get_book_list():
            self._number_books = self._controller.get_book_list()[len(self._controller.get_book_list()) - 1] \
                .get_identity()
        self._number_clients = 0

    def _print_book_list(self):
        """
        Prints a list of all books saved.
        """
        book_list = self._controller.get_book_list()
        if len(book_list) == 0:
            print("There are no books saved.")
        else:
            print("The book list is:\n")
            for book in book_list:
                print(book)

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
                print(client)

    def _print_rentals(self):
        if not self._controller.get_rentals():
            print("\nThere are no books rented.")
            return
        for rental in self._controller.get_rentals():
            print(rental)

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
            self._controller.add_book_to_list_utils(self._number_books, title, author, year, volume)
            print(f"The book '{title}' by {author} published in {year} in the volume '{volume}'"
                  f" was added successfully!")
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
            self._controller.add_client_to_list_utils(name, cnp, subscription_year)
            print(f"The client {name} with the CNP {cnp} subscribed in {subscription_year} was added successfully!")
            self._number_clients = self._number_clients + 1
        except ValueError as ve:
            print(str(ve))

    def _modify_book(self):
        """
        Modifies a book by a given title
        """
        if not self._controller.get_book_list():
            print("The book list is clear. No books to modify!")
            return
        books_rented = [rental.get_book().get_identity() for rental in self._controller.get_rentals()]
        book_ids = [book.get_identity() for book in self._controller.get_book_list() if
                    book.get_identity() not in books_rented]
        if len(book_ids) == 0:
            print("The book list does not contain any 'Available' books. No books to modify!")
            return
        print("Available books to modify have these ids: ")
        for book_id in book_ids:
            print(book_id, end=' ')
        print("\n", end='')
        print("Type 'exit' to return.")
        input_id = input("Your id? ")
        if input_id == 'exit':
            print("Exiting...\n", end='')
            return
        while True:
            try:
                input_id = int(input_id)
            except ValueError:
                print("The id needs to be a valid integer.")
                return
            if input_id not in book_ids:
                print("Book id not found. Try another!")
                print("Type 'exit' to return.")
                input_id = input("Your id? ")
                if input_id == 'exit':
                    print("Exiting...\n", end='')
                    return
                continue
            break
        book = self._controller.get_book_repo().search_book_by_id(input_id)
        print("Available 'book' parameters to modify: ")
        print(f"Book title: {book.get_title()}")
        print(f"Book author: {book.get_author()}")
        print(f"Book publish year: {book.get_year()}")
        print(f"Book volume: {book.get_volume()}")
        new_title = input("New title: ")
        new_author = input("New author: ")
        new_year = input("New year: ")
        new_volume = input("New volume: ")
        try:
            new_year = int(new_year)
        except ValueError:
            print("The year needs to be a valid integer.")
            return
        try:
            self._controller.modify_book_utils(input_id, new_title, new_author, new_year, new_volume)
            print("The book was modified successfully!")
        except ValueError as ve:
            print(str(ve))

    def _modify_client(self):
        """
        Modifies a client.
        """
        if not self._controller.get_client_list():
            print("The client list is clear. No clients to modify!")
            return
        client_rentals = [rental.get_client().get_identity() for rental in self._controller.get_rentals()]
        client_ids = [client.get_identity() for client in self._controller.get_client_list() if
                      client.get_identity() not in client_rentals]
        if not client_ids:
            print("The are no clients with no books rented. No clients to modify!")
            return
        print("Available clients to modify have these ids: ")
        for client_id in client_ids:
            print(client_id, end=' ')
        print("\n", end='')
        print("Type 'exit' to return.")
        input_id = input("Your id? ")
        if input_id == 'exit':
            print("Exiting...\n", end='')
            return
        while True:
            try:
                input_id = int(input_id)
            except ValueError:
                print("The id needs to be a valid integer.")
                return
            if input_id not in client_ids:
                print("Client id not found. Try another!")
                print("Type 'exit' to return.")
                input_id = input("Your id? ")
                if input_id == 'exit':
                    print("Exiting...\n", end='')
                continue
            break
        client = self._controller.get_client_repo().search_client_by_id(input_id)
        print("Available 'client' parameters to modify: ")
        print(f"Client name: {client.get_name()}")
        print(f"Client subscription year: {client.get_subscription_year()}")
        new_name = input("New name: ")
        new_sub_year = input("New subscription year: ")
        try:
            new_sub_year = int(new_sub_year)
        except ValueError:
            print("The subscription year needs to be a valid integer.")
            return
        try:
            self._controller.modify_client_utils(input_id, new_name, new_sub_year)
            print("The client was modified successfully!")
        except ValueError as ve:
            print(str(ve))

    def _delete_book(self):
        if not self._controller.get_book_list():
            print("The book list is clear. No books to delete!")
            return
        books_rented = [rental.get_book().get_identity() for rental in self._controller.get_rentals()]
        book_ids = [book.get_identity() for book in self._controller.get_book_list() if
                    book.get_identity() not in books_rented]
        if len(book_ids) == 0:
            print("The book list does not contain any 'Available' books. No books to delete!")
            return
        print("Available books to delete have these ids: ")
        for book_id in book_ids:
            print(book_id, end=' ')
        print("\n", end='')
        print("Type 'exit' to return.")
        input_id = input("Your id? ")
        if input_id == 'exit':
            print("Exiting...\n", end='')
            return
        while True:
            try:
                input_id = int(input_id)
            except ValueError:
                print("The id needs to be a valid integer")
                return
            if input_id not in book_ids:
                print("Book id not found. Try another!")
                print("Type 'exit' to return.")
                input_id = input("Your id? ")
                if input_id == 'exit':
                    print("Exiting...\n", end='')
                    return
                continue
            break
        try:
            self._controller.delete_book_utils(input_id)
            print("Book deleted successfully!")
        except ValueError as ve:
            print(str(ve))

    def _delete_client(self):
        if not self._controller.get_client_list():
            print("The client list is clear. No clients to delete!")
            return
        client_rentals = [rental.get_client().get_identity() for rental in self._controller.get_rentals()]
        client_ids = [client.get_identity() for client in self._controller.get_client_list() if
                      client.get_identity() not in client_rentals]
        if not client_ids:
            print("There are no clients with no books rented. No clients to delete!")
            return
        print("Available clients to delete have these ids: ")
        for client_id in client_ids:
            print(client_id, end=' ')
        print("\n", end='')
        print("Type 'exit' to return.")
        input_id = input("Your id? ")
        if input_id == 'exit':
            print("Exiting...\n", end='')
        while True:
            try:
                input_id = int(input_id)
            except ValueError:
                print("The id needs to be a valid integer.")
                return
            if input_id not in client_ids:
                print("Client id not found. Try another!")
                print("Type 'exit' to return.")
                input_id = input("Your id? ")
                if input_id == 'exit':
                    print("Exiting...\n", end='')
                    return
                continue
            break
        self._controller.delete_client_utils(input_id)
        print("Client deleted successfully!")

    def _search_book_by_title(self):
        """
        Prints a list of books with a given title
        """
        if not self._controller.get_book_list():
            print("The book list is clear.")
            return
        title = input("Title: ")
        try:
            book_list = self._controller.search_book_by_title_utils(title)
            for book in book_list:
                print(book)
        except ValueError as ve:
            print(str(ve))

    def _search_book_by_year(self):
        """
        Prints a list of books with a given publish year
        """
        if not self._controller.get_book_list():
            print("The book list is clear.")
            return
        year = input("Publish year: ")
        try:
            year = int(year)
        except ValueError:
            print("The year needs to be an integer.")
            return
        try:
            book_list = self._controller.search_book_by_year_utils(year)
            for book in book_list:
                print(book)
        except ValueError as ve:
            print(str(ve))

    def _search_book_in_time_period(self):
        if not self._controller.get_book_list():
            print("The book list is clear.")
            return
        start_year = input("Start year: ")
        try:
            start_year = int(start_year)
        except ValueError:
            print("The year needs to be a valid positive integer.")
            return
        finish_year = input("Finish year: ")
        try:
            finish_year = int(finish_year)
        except ValueError:
            print("The year needs to be a valid positive integer.")
            return
        try:
            book_list = self._controller.search_book_in_time_period(start_year, finish_year)
            for book in book_list:
                print(book)
        except ValueError as ve:
            print(str(ve))
            return

    def _search_client_by_name(self):
        """
        Prints a list of clients with a give name
        """
        if not self._controller.get_client_list():
            print("The client list is clear.")
            return
        name = input("Name: ")
        try:
            client_list = self._controller.search_client_by_name_utils(name)
            for client in client_list:
                print(client)
        except ValueError as ve:
            print(str(ve))
            return

    def _search_client_by_subscription_age(self):
        if not self._controller.get_client_list():
            print("The client list is clear.")
            return
        sub_age = input("Searched subscription age: ")
        try:
            sub_age = int(sub_age)
        except ValueError:
            print("The subscription age needs to be an integer.")
        try:
            client_list = self._controller.search_client_by_subscription_age_utils(sub_age)
            for client in client_list:
                print(client)
        except ValueError as ve:
            print(str(ve))
            return

    def _rent_book(self):
        if not self._controller.get_client_list():
            print("The client list is clear.")
            return
        if not self._controller.get_book_list():
            print("The book list is clear.")
            return
        client_ids = [client.get_identity() for client in self._controller.get_client_list()]
        book_ids = [book.get_identity() for book in self._controller.get_book_list()]
        print("Available clients to rent a book to have these ids: ")
        for client_id in client_ids:
            print(client_id, end=' ')
        print("\n", end='')
        print("Type 'exit' to return.")
        client_input_id = input("Client id? ")
        if client_input_id == 'exit':
            print("Exiting...\n", end='')
            return
        while True:
            try:
                client_input_id = int(client_input_id)
            except ValueError:
                print("The id needs to be a valid integer.")
                return
            if client_input_id not in client_ids:
                print("Client id not found. Try another!")
                print("Type 'exit' to return.")
                client_input_id = input("Client id? ")
                if client_input_id == 'exit':
                    print("Exiting...\n", end='')
                    return
                continue
            break
        print("Available books to rent have these ids: ")
        for book_id in book_ids:
            print(book_id, end=' ')
        print("\n", end='')
        print("Type 'exit' to return.")
        book_input_id = input("Book id? ")
        if book_input_id == 'exit':
            print("Exiting...\n", end='')
            return
        while True:
            try:
                book_input_id = int(book_input_id)
            except ValueError:
                print("The id needs to be a valid integer.")
                return
            if book_input_id not in book_ids:
                print("Book id not found. Try another!")
                print("Type 'exit' to return.")
                book_input_id = input("Book id? ")
                if book_input_id == 'exit':
                    print("Exiting...\n", end='')
                    return
                continue
            break
        try:
            self._controller.rent_book_utils(client_input_id, book_input_id)
            print("The book was rented successfully!")
        except ValueError as ve:
            print(str(ve))
            return

    def _return_book(self):
        if not self._controller.get_rentals():
            print("No clients have rented books yet.")
            return
        rental_ids = [rental.get_identity() for rental in self._controller.get_rentals()]
        print("Available rentals to return have these ids: ")
        for rental_id in rental_ids:
            print(rental_id, end=' ')
        print('\n', end='')
        print("Type 'exit' to return.")
        rental_input_id = input("Rental id? ")
        if rental_input_id == 'exit':
            print("Exiting...\n", end='')
            return
        while True:
            if rental_input_id not in rental_ids:
                print("Rental id not found. Try another!")
                print("Type 'exit' to return.")
                rental_input_id = input("Rental id? ")
                if rental_input_id == 'exit':
                    print("Exiting...\n", end='')
                    return
                continue
            break
        try:
            self._controller.return_book_utils(rental_input_id)
            print("The book was returned successfully!")
        except ValueError as ve:
            print(str(ve))
            return

    def _search_client_in_rentals(self):
        try:
            client_list = self._controller.search_client_in_rentals()
            for client in client_list:
                print(client)
        except TypeError as te:
            print(str(te))
            return

    def _generate_random_book(self):
        self._controller.generate_random_book()
        print("Random book generated successfully!")

    # Statistics
    def _most_rented_books(self):
        try:
            book_list = self._controller.most_rented_books()
            print("The most rented books, in order of rentals, are:")
            for book, noRentals in book_list.items():
                print(f"{book} with {noRentals} rentals")
        except ValueError as ve:
            print(str(ve))

    def _sort_clients_by_name_and_no_rentals(self):
        try:
            client_list = self._controller.sort_clients_by_name_and_no_rentals()
            print("The clients sorted by their name and number of rentals are:")
            for client, noRentals in client_list.items():
                print(f"{client} with {noRentals} rentals")
        except ValueError as ve:
            print(str(ve))

    def _first_20_percent_most_active_clients(self):
        try:
            client_list = self._controller.first_20_percent_most_active_clients()
            print("The most active 20% clients sorted by name and number of rentals are:")
            for client, noRentals in client_list.items():
                print(f"{client} with {noRentals} rentals")
        except ValueError as ve:
            print(str(ve))

    def _sort_books_by_name(self):
        try:
            book_list = self._controller.sort_books_by_name()
            print("The books sorted by their names are: ")
            for book, noRentals in book_list.items():
                print(f"{book} with {noRentals} rentals")
        except ValueError as ve:
            print(str(ve))

    def run_ui(self):
        while True:
            print("Available commands:")
            print("1. Print")
            print("2. Books")
            print("3. Clients")
            print("4. Statistics")
            print("5. Rent book")
            print("6. Return book")
            print("7. Generate a random book")
            print("Type 'exit' to close the app.")

            option = input("Your option? ")
            if option == 'exit':
                print("\nClosing the application. Bye!")
                return

            elif option == '1':
                while True:
                    print("\n1. Print the book list")
                    print("2. Print the client list")
                    print("3. Print the rent list")
                    print("\nType 'exit' to return")
                    option_print = input("Your option? ")
                    if option_print == 'exit':
                        print("\nClosing the sub-menu...\n")
                        break
                    elif option_print == '1':
                        self._print_book_list()
                        print("\n", end='')
                    elif option_print == '2':
                        self._print_client_list()
                        print("\n", end='')
                    elif option_print == '3':
                        self._print_rentals()
                        print("\n", end='')
                    else:
                        print("\nInvalid command!\n")
            elif option == '2':
                while True:
                    print("\n1. Add book to list")
                    print("2. Modify book")
                    print("3. Delete book")
                    print("4. Search")
                    print("\nType 'exit' to return")
                    option_book = input("Your option? ")
                    if option_book == 'exit':
                        print("\nClosing the sub-menu...\n")
                        break
                    elif option_book == '1':
                        self._add_book()
                        print("\n", end='')
                    elif option_book == '2':
                        self._modify_book()
                        print("\n", end='')
                    elif option_book == '3':
                        self._delete_book()
                        print("\n", end='')
                    elif option_book == '4':
                        while True:
                            print("\n1. Search book by title")
                            print("2. Search book by publish year")
                            print("3. Search books in a time period")
                            print("\nType 'exit' to return")
                            option_search_book = input("Your option? ")
                            if option_search_book == 'exit':
                                print("\nClosing the sub-menu...\n")
                                break
                            elif option_search_book == '1':
                                self._search_book_by_title()
                                print("\n", end='')
                            elif option_search_book == '2':
                                self._search_book_by_year()
                                print("\n", end='')
                            elif option_search_book == '3':
                                self._search_book_in_time_period()
                                print("\n", end='')
                            else:
                                print("\nInvalid command!\n")
                    else:
                        print("\nInvalid command!\n")
            elif option == '3':
                while True:
                    print("\n1. Add client to list")
                    print("2. Modify client")
                    print("3. Delete client")
                    print("4. Search")
                    print("\nType 'exit' to return")
                    option_client = input("Your option? ")
                    if option_client == 'exit':
                        print("\nClosing the sub-menu...\n")
                        break
                    elif option_client == '1':
                        self._add_client()
                        print("\n", end='')
                    elif option_client == '2':
                        self._modify_client()
                        print("\n", end='')
                    elif option_client == '3':
                        self._delete_client()
                        print("\n", end='')
                    elif option_client == '4':
                        while True:
                            print("\n1. Search client by name")
                            print("2. Search client by subscription age")
                            print("3. Search client with rented books")
                            print("\nType 'exit' to return")
                            option_search_client = input("Your option? ")
                            if option_search_client == 'exit':
                                print("Closing the sub-menu...\n")
                                break
                            elif option_search_client == '1':
                                self._search_client_by_name()
                                print("\n", end='')
                            elif option_search_client == '2':
                                self._search_client_by_subscription_age()
                                print("\n", end='')
                            elif option_search_client == '3':
                                self._search_client_in_rentals()
                                print("\n", end='')
                            else:
                                print("\nInvalid command!\n")
                    else:
                        print("\nInvalid command!\n")
            elif option == '4':
                while True:
                    print("\n1. Show the most rented books")
                    print("2. Show the clients ordered by their name and number of rented books")
                    print("3. Show the 20% most active clients")
                    print("4. Show all the books sorted by their name")
                    print("\nType 'exit' to return")
                    option_statistics = input("Your option? ")
                    if option_statistics == 'exit':
                        print("Closing the sub-menu...\n")
                        break
                    elif option_statistics == '1':
                        self._most_rented_books()
                        print("\n", end='')
                    elif option_statistics == '2':
                        self._sort_clients_by_name_and_no_rentals()
                        print("\n", end='')
                    elif option_statistics == '3':
                        self._first_20_percent_most_active_clients()
                        print("\n", end='')
                    elif option_statistics == '4':
                        self._sort_books_by_name()
                        print("\n", end='')
                    else:
                        print("\nInvalid command!\n")
            elif option == '5':
                self._rent_book()
                print("\n", end='')
            elif option == '6':
                self._return_book()
                print("\n", end='')
            elif option == '7':
                self._generate_random_book()
                print("\n", end='')
            else:
                print("\nInvalid command!\n")
