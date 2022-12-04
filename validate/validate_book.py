import re
from datetime import datetime


class BookValidator:
    @staticmethod
    def validate_title(title):
        """
        Validates the string such that the string is a valid string and not the ' ' string
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
    def validate_volume(volume):
        """
        Validates the string such that the string is a valid string and not the ' ' string
        :param volume: str
        :return: -
        :raises ValueError: - if the volume is not a string or the ' ' string
                              the associated string is: "The volume needs to be a valid string."
        """
        if not isinstance(volume, str):
            raise ValueError("The volume needs to be a valid string.")
        else:
            if volume == '':
                raise ValueError("The volume needs to be a valid string.")

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

    @staticmethod
    def validate_author_name(author_name):
        """
        Validates a passed author_name.
        :param author_name: str
        :return: -
        :raises ValueError: - if the name of the author is not a string or the ' ' string;
                              the associated string is: "The author's name needs to be a valid string.";
        """
        # Verifying the name of the book's author
        if not isinstance(author_name, str):
            raise ValueError("The author's name needs to be a valid string.")
        elif author_name == '':
            raise ValueError("The author's name needs to be a valid string.")
        else:
            list_of_names = re.split(r"\s+|-", author_name)
            for name in list_of_names:
                if not name[0].isupper():
                    raise ValueError("The author's name needs to be a valid string.")
                for character in name:
                    if not character.isalpha() and character != '.':
                        raise ValueError("The author's name needs to be a valid string.")

    def validate_period(self, start_year, finish_year):
        """
        Validates year1 and year2 such that they are positive integers between 1680 and {current_year}.
        :param start_year: int
        :param finish_year: int
        :return: nothing
        :raises ValueError: - if either year1 or year2 are not positive integers between 1680 and {current_year}
                              the associated string is: "{start_year}/{finish_year} is not a positive integer between
                                                         1680 and {current_year}."
                            - if start_year is greater than finish_year
                              the associated string is: "The start year cannot be greater than the finish year."
        """
        self.validate_year(start_year)
        self.validate_year(finish_year)
        if start_year > finish_year:
            raise ValueError("The start year cannot be greater than the finish year.")
        if not (1680 <= start_year <= int(datetime.now().year)):
            raise ValueError(f"{start_year} is not a positive integer between 1680 and {datetime.now().year}")
        if not (1680 <= finish_year <= int(datetime.now().year)):
            raise ValueError(f"{finish_year} is not a positive integer between 1680 and {datetime.now().year}")

    @staticmethod
    def validate_status(status):
        """
        Validates the passed status.
        :param status: str
        :return: nothing
        :raises ValueError: - if the status is not 'Available' or 'Rented'
                              the associated string is: "The searched status needs to be 'Available' or 'Rented'."
        """
        if status != 'Available' and status != 'Rented':
            raise ValueError("The searched status needs to be'Available' or 'Rented'.")

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
        errors = []
        if not isinstance(book.get_author(), str):
            errors.append("The author's name needs to be a valid string.")
        elif book.get_author() == '':
            errors.append("The author's name needs to be a valid string.")
        else:
            list_of_names = re.split(r"\s+|-", book.get_author())
            for name in list_of_names:
                if name == '':
                    continue
                if not name[0].isupper():
                    errors.append("The author's name needs to be a valid string.")
                for character in name:
                    if not character.isalpha() and character != '.':
                        errors.append("The author's name needs to be a valid string.")

        # Verifying the book's title
        if not isinstance(book.get_title(), str):
            errors.append("The book's title needs to be a valid string.")
        else:
            if book.get_title() == '':
                errors.append("The book's title needs to be a valid string.")

        if not isinstance(book.get_year(), int):
            errors.append(f"The book's release year needs to be betwwen 1680 and {datetime.now().year}.")
        else:
            if book.get_year() < 1680 or book.get_year() > int(datetime.now().year):
                errors.append(f"The book's release year needs to be betwwen 1680 and {datetime.now().year}.")

        if not isinstance(book.get_volume(), str):
            errors.append("The book's volume needs to be a valid string.")
        else:
            if book.get_volume() == '':
                errors.append("The book's volume needs to be a valid string.")
        if errors:
            raise ValueError(" ".join(errors).strip())
