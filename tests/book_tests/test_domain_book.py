from domain.book import Book


def test_create_book():
    book1 = Book.create_book(15, 'Amintiri din copilarie', 'Ion Creanga',
                                                                 1892, 'Amintiri din copilarie')
    book2 = Book.create_book(21, 'Ulysses', 'James Joyce',
                                                                 1922, 'Ulysses')
    book3 = Book.create_book(23, 'The Great Gatsby', 'F. Scott Fitzgerald',
                                                                 1925, 'The Great Gatsby')
    assert book1.get_title() == 'Amintiri din copilarie'
    assert book1.get_status() == 'Available'

    assert book2.get_author() == 'James Joyce'
    assert book2.get_identity() == 21

    assert book3.get_volume() == 'The Great Gatsby'
    assert book3.get_year() == 1925