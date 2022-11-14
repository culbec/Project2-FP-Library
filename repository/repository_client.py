from domain.client import Client


class ClientRepository:
    def __init__(self):
        self._client_list = []

    def get_client_list(self):
        return self._client_list

    @staticmethod
    def add_client_to_list(client, library_controller):
        """
        Adds a client to library_controller's client_list
        :param client: Client
        :param library_controller: LibraryController
        :return: nothing - just adds the client to library_controller's client_list
        """
        library_controller.get_client_list().append(client)
