from datetime import datetime
import re


class BookValidator:
    @staticmethod
    def validate_book(book):
        """
        Checks if the passed object book was declared as a valid one.
        :param book: book
        :return: nothing if the book is a valid object
        :raises ValueError: - if the identity of the book is not a strictly positive integer
                              the associated string is: "The identity needs to be greater than 0.";
                            - if the title of the book is not a string or the ' ' string;
                              the associated string is: "The book's title needs to be a valid string.";
                            - if the name of the author is not a string or the ' ' string;
                              the associated string is: "The author's name needs to be a valid string.";
                            - if the year of the book is not an integer between 1680 and the current year
                              the associated string is: "The book's release year needs to be between 1680
                                                         and {current_year}.";
                            - if the book's volume is not a string or the ' ' string;
                              the associated string is: "The book's volume needs to be a valid string.";
                            - if another book with the same id already exits in library_controllers's book_list
                              the associated string is "Another book with the same id already exists."
        """
        # Verifying the name of the book's author
        if not isinstance(book.get_author(), str):
            raise ValueError("The author's name needs to be a valid string.")
        else:
            list_of_names = re.split(r"\s+|-", book.get_author())
            for name in list_of_names:
                if not name[0].isupper():
                    raise ValueError("The author's name needs to be a valid string.")
                for character in name:
                    if not character.isalpha() and character != '.':
                        raise ValueError("The author's name needs to be a valid string.")

        # Verifying the book's title
        if not isinstance(book.get_title(), str):
            raise ValueError("The book's title needs to be a valid string.")
        else:
            if book.get_title() == '':
                raise ValueError("The book's title needs to be a valid string.")

        if not isinstance(book.get_year(), int):
            raise ValueError(f"The book's release year needs to be betwwen 1680 and {datetime.now().year}.")
        else:
            if book.get_year() < 1680 or book.get_year() > int(datetime.now().year):
                raise ValueError(f"The book's release year needs to be betwwen 1680 and {datetime.now().year}.")

        if not isinstance(book.get_volume(), str):
            raise ValueError("The book's volume needs to be a valid string.")
        else:
            if book.get_volume() == '':
                raise ValueError("The book's volume needs to be a valid string.")


    @staticmethod
    def validate_title(title):
        """
        Validates the title such that the title is a valid string and not the ' ' string
        :param title: str
        :return: -
        :raises ValueError: - if the title is not a string or the ' ' string
                              the associated string is: "The title needs to be a valid string."
        """
        if not isinstance(title, str):
            raise ValueError("The title needs to be a valid string.")
        else:
            if title == '':
                raise ValueError("The title needs to be a valid string.")

    @staticmethod
    def validate_year(year):
        """
        Validates the year such that the title is an integer between 1680 and the current year
        :param year: int
        :return: -
        :raises ValueError: - if the year is not an integer between 1680 and the current year
                              the associated string is: "The release year needs to be an integer
                                                         between 1680 and {current_year}.";
        """
        if not isinstance(year, int):
            raise ValueError(f"The release year needs to be an integer between 1680 and {datetime.now().year}.")
        else:
            if year < 1680 or year > int(datetime.now().year):
                raise ValueError(f"The release year needs to be an integer between 1680 and {datetime.now().year}.")
