import io

from domain.entities import Rental, Client, Book


class RentalRepository:
    def __init__(self):
        self._rentals_list = []

    def get_rentals_list(self):
        return self._rentals_list

    def set_rentals_list(self, rentals_list):
        self._rentals_list = rentals_list

    def add_rental_to_list(self, rental):
        """
        Adds the passed rental to the rental list
        :param rental: Rental
        :return: nothing, just adds the rental to the rental list
        """
        rental_list = self.get_rentals_list()
        rental_list.append(rental)
        self.set_rentals_list(rental_list)

    def delete_rental(self, rental):
        """
        Deletes a passed rental from the rental list
        :param rental: Rental
        :return: nothing, just deletes the passed rental from the rental list
        """
        rental_list = self.get_rentals_list()
        rental_list.remove(rental)
        self.set_rentals_list(rental_list)


class RentalRepositoryFile(RentalRepository):
    def __init__(self, filename):
        RentalRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _load_from_file(self):
        try:
            file = io.open(self._filename, mode='r', encoding='utf-8')
        except IOError:
            return

        lines = file.readlines()
        for line in lines:
            rental_id, rental_client_str, rental_book_str = [token.strip() for token in line.split('|')]
            rental_client_id, rental_client_name, \
                rental_client_cnp, rental_client_sub_year = [token.strip() for token in rental_client_str.split(';')]
            rental_book_id, rental_book_title, rental_book_author, \
                rental_book_year, rental_book_volume = [token.strip() for token in rental_book_str.split(';')]
            rental_client = Client(rental_client_name, int(rental_client_cnp), int(rental_client_sub_year))
            rental_book = Book(int(rental_book_id), rental_book_title, rental_book_author, int(rental_book_year),
                               rental_book_volume)
            rental = Rental(rental_client, rental_book)
            RentalRepository.add_rental_to_list(self, rental)
        file.close()

    def _save_to_file(self):
        rental_list = RentalRepository.get_rentals_list(self)
        with io.open(self._filename, mode='w', encoding='utf-8') as file:
            for rental in rental_list:
                rental_string = f"{rental.get_identity()} | {rental.get_client()} | " \
                                f"{rental.get_book()}\n"
                file.write(rental_string)

    def _clear_file(self):
        with io.open(self._filename, mode='w', encoding='utf-8'):
            pass

    def add_rental_to_list(self, rental):
        """
        Adds the passed rental to the rental list
        :param rental: Rental
        :return: -
        """
        RentalRepository.add_rental_to_list(self, rental)
        self._save_to_file()

    def delete_rental(self, rental):
        """
        Deletes the passed rental
        :param rental: Rental
        :return: -
        """
        RentalRepository.delete_rental(self, rental)
        self._save_to_file()
