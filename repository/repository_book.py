class BookRepository:
    def __init__(self):
        self._book_list = []

    def get_book_list(self):
        return self._book_list

    def add_book_to_list(self, book):
        """
        Adds a book to library_controller's book_list
        :param book: Book
        :return: nothing - just adds a book to book_repository's book_list
        """
        self._book_list.append(book)

    def search_book_by_id(self, identity):
        """
        Searches a book by its identity.
        :param identity: int
        :return: the book with its id equal to 'identity'
        :raises ValueError: - if no book with the passed id exists in the book_list
                            - the associated string is: "There are no books with the passed id."
        """
        for book in self._book_list:
            if book.get_identity() == identity:
                return book
        raise ValueError("There are no books with the passed id.")

    @staticmethod
    def modify_book(book, title, author, year, volume):
        """
        Modifies a book with its identity equal to the passed identity.
        :param title: str
        :param author: str
        :param year: str
        :param volume: str
        :param book: Book
        :return: nothing, just modifies the book with the passed id
        """
        book.set_title(title)
        book.set_author(author)
        book.set_year(year)
        book.set_volume(volume)

    def delete_book(self, book):
        """
        Deletes a book with its id equal to identity
        :param book: Book
        :return: nothing, just deletes that certain book
        """
        self._book_list.remove(book)
