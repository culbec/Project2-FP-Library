class RentalValidator:
    @staticmethod
    def validate_rental(rental, rental_list):
        """
        Validates a rental such that a rental with the same id as the passed rental doesn't already exists
        in rental_list
        :param rental: Rental
        :param rental_list: rental list
        :return: nothing, if the passed rental is valid
        :raises ValueError: - if a rental with the same id as the passed rental already exists in rental_list
                              the associated string is: "A rental with the same id already exists!"
        """
        for _rental in rental_list:
            if rental == _rental:
                raise ValueError("A rental with the same id already exists!")
