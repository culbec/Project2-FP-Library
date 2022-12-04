import re
from datetime import datetime


class ClientValidator:
    @staticmethod
    def validate_name(name):
        """
        Validates the passed name
        :param name: str
        :return: -
        :raises ValueError: - if the name is not a valid string
                              the associated string is: "The name needs to be a valid string."
        """
        if not isinstance(name, str):
            raise ValueError("The name needs to be a valid string.")
        list_of_names = re.split(r"\s+|-", name)
        for name in list_of_names:
            if name == '':
                raise ValueError("The name needs to be a valid string.")
            elif not name[0].isupper():
                raise ValueError("The name needs to be a valid string.")
            for character in name:
                if not character.isalpha() and character != '.':
                    raise ValueError("The name needs to be a valid string.")

    @staticmethod
    def validate_cnp(cnp):
        """
        Validates the passed cnp.
        :param cnp: int
        :return: -
        :raises ValueError: - if the CNP is not a 13 digit positive integer
                              the associated string is "The CNP needs to be a valid one."
        """
        if not isinstance(cnp, int):
            raise ValueError("The CNP needs to be a valid one.")
        else:
            cnp = str(cnp)
            if len(cnp) != 13:
                raise ValueError("The CNP needs to be a valid one.")

    @staticmethod
    def validate_sub_year(sub_year):
        """
        Validates the sub_year
        :param sub_year: int
        :return: -
        :raises ValueError: - if the subscription year is greater than the current year or greater than 90
                              the associated string is "The subscription year cannot be greater
                                                        than {current_year} or more than 90 years of subscription."
        """
        # Verifying the subscription year of the client
        if not isinstance(sub_year, int):
            raise ValueError(f"The client's subscription needs to be a positive integer "
                             f"lower or equal than {datetime.now().year}.")
        else:
            if (sub_year > datetime.now().year or
                    datetime.now().year - sub_year >= 90):
                raise ValueError(f"The subscription year cannot be greater than {datetime.now().year} "
                                 f"or more than 90 years of subscription.")

    @staticmethod
    def validate_subscription_age(sub_age):
        """
        Validates the passed sub_age such that 0 <= sub_age <= 90.
        :param sub_age: int
        :return: nothing
        :raises ValueError: - if the sub_age doesn't respect 0 <= sub_age <= 90
                              the associated string is: "The subscription age needs to be an integer between 0 and 90."
        """
        if not isinstance(sub_age, int):
            raise ValueError("The subscription age needs to be an integer between 0 and 90.")
        elif not 0 <= sub_age <= 90:
            raise ValueError("The subscription age needs to be an integer between 0 and 90.")

    @staticmethod
    def validate_client(client, client_repo):
        """
        Checks if the passed object client was declared as a valid one.
        :param client: client
        :param client_repo: ClientRepository()
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
        errors = []
        # Verifying the name of the client
        if not isinstance(client.get_name(), str):
            errors.append("The client's name needs to be a valid string.")
        else:
            list_of_names = re.split(r"\s+|-", client.get_name())
            for name in list_of_names:
                if not name[0].isupper():
                    errors.append("The client's name needs to be a valid string.")
                for character in name:
                    if not character.isalpha():
                        errors.append("The client's name needs to be a valid string.")

        # Verifying the CNP of the client
        if not isinstance(client.get_cnp(), int):
            errors.append("The client's CNP needs to be a valid one.")
        else:
            cnp = str(client.get_cnp())
            if len(cnp) != 13:
                errors.append("The client's CNP needs to be a valid one.")

        # Verifying the subscription year of the client
        if not isinstance(client.get_subscription_year(), int):
            errors.append(f"The client's subscription needs to be a positive integer "
                          f"lower or equal than {datetime.now().year}.")
        else:
            if (client.get_subscription_year() > datetime.now().year or
                    datetime.now().year - client.get_subscription_year() > 90):
                errors.append(f"The client's subscription year cannot be greater than {datetime.now().year} "
                              f"or more than 90 years of subscription.")

        # Verifying if the client with the same id already exists in library_controller's client_list
        for _client in client_repo.get_client_list():
            if client == _client:
                errors.append("Another client with the same identity or CNP already exists.")
        if errors:
            raise ValueError(" ".join(errors).strip())
