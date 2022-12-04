class Book:
    def __init__(self, identity, title, author, year, volume):
        self._identity = identity
        self._title = title
        self._author = author
        self._year = year
        self._volume = volume

    def get_identity(self):
        return self._identity

    def get_author(self):
        return self._author

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_volume(self):
        return self._volume

    def set_author(self, author):
        self._author = author

    def set_title(self, title):
        self._title = title

    def set_year(self, year):
        self._year = year

    def set_volume(self, volume):
        self._volume = volume

    def __str__(self):
        return f"{str(self.get_identity())} ; {str(self.get_title())} ; {str(self.get_author())} ; " \
               f"{str(self.get_year())} ; {str(self.get_volume())}"


class Client:
    def __init__(self, name, cnp, subscription_year):
        self._identity = cnp
        self._name = name
        self._cnp = cnp
        self._subscription_year = subscription_year

    def get_identity(self):
        return self._identity

    def get_name(self):
        return self._name

    def get_cnp(self):
        return self._cnp

    def get_subscription_year(self):
        return self._subscription_year

    def set_name(self, name):
        self._name = name

    def set_subscription_year(self, subscription_year):
        self._subscription_year = subscription_year

    def __eq__(self, other):
        return self.get_identity() == other.get_identity()

    def __hash__(self):
        return id(self)

    def __str__(self):
        return f"{str(self.get_identity())} ; {str(self.get_name())} ; {str(self.get_cnp())} ; " \
               f"{str(self.get_subscription_year())}"


class Rental:
    def __init__(self, client, book):
        self._identity = f"{client.get_identity()}_{book.get_identity()}"
        self._client = client
        self._book = book

    def get_identity(self):
        return self._identity

    def get_client(self):
        return self._client

    def get_book(self):
        return self._book

    def __eq__(self, other):
        return self.get_identity() == other.get_identity()

    def __str__(self):
        return f"{self.get_identity()} | {self.get_client()} | {self.get_book()}"
