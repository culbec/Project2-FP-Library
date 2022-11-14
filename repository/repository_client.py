from domain.client import Client


class ClientRepository:
    def __init__(self):
        self._client_list = []

    def get_client_list(self):
        return self._client_list

    @staticmethod
    def create_client(identity, name, cnp, subscription_year):
        """
        Creates a Client object with the passed arguments.
        :param identity: int
        :param name: str
        :param cnp: int
        :param subscription_year: int
        :return: a Client object with the passed arguments
        """
        return Client(identity, name, cnp, subscription_year)

    @staticmethod
    def add_client_to_list(client, library_controller):
        """
        Adds a client to library_controller's client_list
        :param client: Client
        :param library_controller: LibraryController
        :return: nothing - just adds the client to library_controller's client_list
        """
        library_controller.get_client_list().append(client)

    @staticmethod
    def search_client_by_name(name, library_controller):
        """
        Returns a list of clients in library_controller's client_list with the 'name' name
        :param name: str
        :param library_controller: LibraryController
        :return: a list of clients in library_controller's client_list with the 'name' name
        :raises ValueError: - if a client with the 'name' name does not exist in library_controller's client_list
                              the associated string is: "Clients with the passed name do not exist!"
        """
        client_list = []
        for client in library_controller.get_client_list():
            if client.get_name() == name:
                client_list.append(client)
        if not client_list:
            raise ValueError("Clients with the passed name do not exist!")
        return client_list
