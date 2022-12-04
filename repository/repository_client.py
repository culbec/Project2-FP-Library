import io

from domain.entities import Client


class ClientRepository:
    def __init__(self):
        self._client_list = []

    def get_client_list(self):
        return self._client_list

    def set_client_list(self, client_list):
        self._client_list = client_list

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
        client_list = self.get_client_list()
        client_list.append(client)
        self.set_client_list(client_list)

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


class ClientRepositoryFile(ClientRepository):
    def __init__(self, filename):
        ClientRepository.__init__(self)
        self._filename = filename
        self._load_from_file()

    def _load_from_file(self):
        try:
            file = io.open(self._filename, mode='r', encoding='utf-8')
        except IOError:
            return

        lines = file.readlines()
        for line in lines:
            tokens = [token.strip() for token in line.split(';')]
            client_id, client_name, client_cnp, client_sub_year = tokens
            client = Client(client_name, int(client_cnp), int(client_sub_year))
            ClientRepositoryFile.add_client_to_list(self, client)
        file.close()

    def save_to_file(self):
        client_list = ClientRepositoryFile.get_client_list(self)
        with io.open(self._filename, mode='w', encoding='utf-8') as file:
            for client in client_list:
                client_string = f"{str(client.get_identity())} ; {client.get_name()} ; {str(client.get_cnp())} ; " \
                                f"{str(client.get_subscription_year())}\n"
                file.write(client_string)

    def _clear_file(self):
        with io.open(self._filename, mode='w', encoding='utf-8'):
            pass

    def add_client_to_list(self, client):
        """
        Adds a client to the client list
        :param client: Client
        :return: -
        """
        ClientRepository.add_client_to_list(self, client)
        self.save_to_file()

    def modify_client(self, client, client_name, client_sub_year):
        """
        Modifies the passed client with the passed arguments
        :param client: Client
        :param client_name: str
        :param client_sub_year: int
        :return: -
        """
        ClientRepository.modify_client(client, client_name, client_sub_year)
        self.save_to_file()

    def delete_client(self, client):
        """
        Removes the client from the client list
        :param client: Client
        :return: -
        """
        ClientRepository.delete_client(self, client)
        self.save_to_file()
