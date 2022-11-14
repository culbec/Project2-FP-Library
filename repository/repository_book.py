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
    def add_book_to_list(book, library_controller):
        """
        Adds a book to library_controller's book_list
        :param book: Book
        :param library_controller: LibraryController
        :return: nothing - just adds a boot to library_controller's book_list
        """
        library_controller.get_book_dict().update({book.get_identity(): book})
