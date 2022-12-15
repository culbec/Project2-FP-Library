import io

from domain.entities import Book


class BookRepository:
    def __init__(self):
        self._book_list = []

    def get_book_list(self):
        return self._book_list

    def set_book_list(self, book_list):
        self._book_list = book_list

    def add_book_to_list(self, book):
        """
        Adds a book to library_controller's book_list
        :param book: Book
        :return: nothing - just adds a book to book_repository's book_list
        """
        book_list = self.get_book_list()
        book_list.append(book)
        self.set_book_list(book_list)

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
        book_list = self.get_book_list()
        book_list.remove(book)
        self.set_book_list(book_list)


class BookRepositoryFile(BookRepository):
    def __init__(self, filename):
        BookRepository.__init__(self)
        self._filename = filename
        self._load_from_file_attr()

    def _load_from_file(self):
        """
        Reads data from a file
        :return: book list from a file
        """
        try:
            file = io.open(self._filename, mode='r', encoding='utf-8')
        except IOError:
            return

        lines = file.readlines()
        for line in lines:
            book_id, book_title, book_author, book_year, book_volume = \
                [token.strip() for token in line.split(';')]
            book_id = int(book_id)
            book_year = int(book_year)

            book = Book(book_id, book_title, book_author, book_year, book_volume)
            BookRepositoryFile.add_book_to_list(self, book)

        file.close()

    def _load_from_file_attr(self):
        try:
            file = io.open(self._filename, mode='r', encoding='utf-8')
        except IOError:
            return

        line = file.readline()
        while line != '':
            book_id = int(line.strip())
            book_title = file.readline().strip()
            book_author = file.readline().strip()
            book_year = int(file.readline().strip())
            book_volume = file.readline().strip()
            book = Book(book_id, book_title, book_author, book_year, book_volume)
            BookRepositoryFile.add_book_to_list_attr(self, book)
            line = file.readline()
        file.close()

    def save_to_file(self):
        """
        Saves data to the file
        :return: -
        """
        book_list = BookRepository.get_book_list(self)
        with open(self._filename, 'w') as file:
            for book in book_list:
                book_string = f"{str(book.get_identity())} ; {book.get_title()} ; {book.get_author()} ; " \
                              f"{str(book.get_year())} ; {book.get_volume()}\n"
                file.write(book_string)

    def _clear_file(self):
        with io.open(self._filename, mode='w', encoding='utf-8'):
            pass

    def save_to_file_attr(self):
        book_list = BookRepository.get_book_list(self)
        with io.open(self._filename, mode='w', encoding='utf-8') as file:
            for book in book_list:
                file.write(f"{book.get_identity()}\n")
                file.write(f"{book.get_title()}\n")
                file.write(f"{book.get_author()}\n")
                file.write(f"{book.get_year()}\n")
                file.write(f"{book.get_volume()}\n")

    def add_book_to_list(self, book):
        """
        Adds a book to the book list
        :param book: Book
        :return:
        """
        BookRepository.add_book_to_list(self, book)
        self.save_to_file()

    def add_book_to_list_attr(self, book):
        BookRepository.add_book_to_list(self, book)
        self.save_to_file_attr()

    def modify_book(self, book, title, author, year, volume):
        """
        Modifies the passed book with the passed arguments
        :param book: Book
        :param title: str
        :param author: str
        :param year: int
        :param volume: str
        :return: -
        """
        BookRepository.modify_book(book, title, author, year, volume)
        self.save_to_file()

    def modify_book_attr(self, book, title, author, year, volume):
        BookRepository.modify_book(book, title, author, year, volume)
        self.save_to_file_attr()

    def delete_book(self, book):
        """
        Deletes a book from the book list
        :param book: Book
        :return:
        """
        BookRepository.delete_book(self, book)
        self.save_to_file()

    def delete_book_attr(self, book):
        BookRepository.delete_book(self,book)
        self.save_to_file_attr()
