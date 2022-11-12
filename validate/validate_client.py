from datetime import datetime
import re


class ClientValidator:
    @staticmethod
    def validate_client(client, library_controller):
        """
        Checks if the passed object client was declared as a valid one.
        :param client: client
        :param library_controller: library_controller
        :return: nothing if the client is a valid object
        :raises ValueError: - if the identity of the client is not a strictly positive integer
                              the associated string is: "The identity needs to be greater than 0."
                            - if the name of the client contains other characters than letters and
                              it's names don't start with a capital letter
                              the associated string is: "The client's name needs to be a valid string."
                            - if the client's CNP is not a 13 digit positive integer
                              the associated string is "The client's CNP needs to be a valid one."
                            - if the client's subscription year is not a valid positive integer lower or equal than
                              {current_year}
                              the associated string is: "The client's subscription needs to be a positive integer
                                                         lower or equal than {current_year}.
                            - if the client's subscription year is greater than the current year or greater than 90
                              the associated string is "The client's subscription year cannot be greater
                                                        than {current_year} or more than 90 years of subscription."
                            - if another client with the same id already exits in library_controllers's client_list
                              the associated string is "Another client with the same identity or CNP already exists."
        """
        # Verifying the name of the client
        if not isinstance(client.get_name(), str):
            raise ValueError("The client's name needs to be a valid string.")
        else:
            list_of_names = re.split(r"\s+|-", client.get_name())
            for name in list_of_names:
                if not name[0].isupper():
                    raise ValueError("The client's name needs to be a valid string.")
                for character in name:
                    if not character.isalpha():
                        raise ValueError("The client's name needs to be a valid string.")

        # Verifying the CNP of the client
        if not isinstance(client.get_cnp(), int):
            raise ValueError("The client's CNP needs to be a valid one.")
        else:
            cnp = str(client.get_cnp())
            if len(cnp) != 13:
                raise ValueError("The client's CNP needs to be a valid one.")

        # Verifying the subscription year of the client
        if not isinstance(client.get_subscription_year(), int):
            raise ValueError(f"The client's subscription needs to be a positive integer "
                             f"lower or equal than {datetime.now().year}.")
        else:
            if (client.get_subscription_year() > datetime.now().year or
                    datetime.now().year - client.get_subscription_year() > 90):
                raise ValueError(f"The client's subscription year cannot be greater than {datetime.now().year} "
                                 f"or more than 90 years of subscription.")

        # Verifying if the client with the same id already exists in library_controller's client_list
        for _client in library_controller.get_client_list():
            if client.get_identity() == _client.get_identity() or client.get_cnp() == _client.get_cnp():
                raise ValueError("Another client with the same identity or CNP already exists.")

    @staticmethod
    def validate_name(name):
        """
        Validates the passed name
        :param name: str
        :return: -
        :raises ValueError: - if the name is not a valid string
                              the associated string is: "The name needs to be a valid string."
        """
        list_of_names = re.split(r"\s+|-", name)
        for name in list_of_names:
            if not name[0].isupper():
                raise ValueError("The name needs to be a valid string.")
            for character in name:
                if not character.isalpha() and character != '.':
                    raise ValueError("The name needs to be a valid string.")

