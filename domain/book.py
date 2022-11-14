class Book:
    def __init__(self, identity, title, author, year, volume):
        self._identity = identity
        self._title = title
        self._author = author
        self._year = year
        self._volume = volume
        self._status = 'Available'

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

    def get_status(self):
        return self._status

    def set_identity(self, identity):
        self._identity = identity

    def set_author(self, author):
        self._author = author

    def set_title(self, title):
        self._title = title

    def set_year(self, year):
        self._year = year

    def set_volume(self, volume):
        self._volume = volume

    def set_status(self, status):
        self._status = status

    @staticmethod
    def create_book(identity, title, author, year, volume):
        """
        Creates a Book type object with the passed arguments.
        :param identity: int
        :param title: str
        :param author: str
        :param year: int
        :param volume: str
        :return: a Book type object
        """
        return Book(identity, title, author, year, volume)
