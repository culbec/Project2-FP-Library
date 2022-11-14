from domain.book import Book


class BookRepository:
    """def __init__(self):
        self._book_list = []

    def get_book_list(self):
        return self._book_list"""

    def __init__(self):
        self._book_dict = {}

    def get_book_dict(self):
        return self._book_dict

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

    @staticmethod
    def add_book_to_list(book, library_controller):
        """
        Adds a book to library_controller's book_list
        :param book: Book
        :param library_controller: LibraryController
        :return: nothing - just adds a boot to library_controller's book_list
        """
        library_controller.get_book_dict().update({book.get_identity(): book})

    @staticmethod
    def search_book_by_title(title, library_controller):
        """
        Returns the list of books in library_controller's book_list that have the 'title' title
        :param title: str
        :param library_controller: LibraryController
        :return: a list of books with books in library_controller that have the 'title' title
        :raises ValueError: - if a book with the passed title doesn't exist in library_controller's book_list
                              the associated string is: "Books with the passed title do not exist!"
        """
        book_list = []
        for book in library_controller.get_book_dict().values():
            if book.get_title() == title:
                book_list.append(book)
        if not book_list:
            raise ValueError("Books with the passed title do not exist!")
        return book_list

    @staticmethod
    def search_book_by_year(year, library_controller):
        """
        Returns a list of books in library_controller's book_list that have the 'year' year
        :param year: int
        :param library_controller: LibraryController
        :return: a list of books with books in library_controller that have the 'year' year
        :raises ValueError: - if a book with the passed year doesn't exist in library_controller's book_list
                              the associated string is: "Books with the passed release year do not exist!"
        """
        book_list = []
        for book in library_controller.get_book_dict().values():
            if book.get_year() == year:
                book_list.append(book)
        if not book_list:
            raise ValueError("Books with the passed release year do not exist!")
        return book_list
