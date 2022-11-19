from domain.client import Client


class ClientRepository:
    def __init__(self):
        self._client_list = []

    def get_client_list(self):
        return self._client_list

    def search_client_by_id(self, client_id):
        """
        Returns the client with its id equal to 'client_id'
        :param client_id: int
        :return: the client with the passed id equal to 'client_id'
        :raises ValueError: - if no client with the passed id exists in client_list
                              the associated string is: "There are no clients with the passed id."
        """
        for client in self.get_client_list():
            if client.get_identity() == client_id:
                return client
        raise ValueError("There are no clients with the passed id.")

    def add_client_to_list(self, client):
        """
        Adds a client to client_repo's client_list
        :param client: Client
        :return: nothing - just adds the client to client_repo's client_list
        """
        self.get_client_list().append(client)

    @staticmethod
    def modify_client(client, client_name, client_sub_year):
        """
        Modifies the passed client.
        :param client: Client
        :param client_name: str
        :param client_sub_year: int
        :return: nothing - just modifies the client in client_repo's client_list
        """
        client.set_name(client_name)
        client.set_subscription_year(client_sub_year)

    def delete_client(self, client):
        """
        Deletes a passed client.
        :param client: Client
        :return: nothing, just deletes the client.
        """
        self.get_client_list().remove(client)
