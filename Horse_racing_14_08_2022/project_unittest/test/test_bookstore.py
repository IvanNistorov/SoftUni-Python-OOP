import unittest
from unittest import TestCase

from project_unittest.bookstore import Bookstore


class TestBookstore(TestCase):
    BOOK_LIMIT = 100

    def setUp(self) -> None:
        self.book_store = Bookstore(self.BOOK_LIMIT)

    def test_init_method(self):
        self.assertEqual(self.BOOK_LIMIT, self.book_store.books_limit)
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_books_limit_setter_for_error(self):
        value = -1
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = value

        self.assertEqual(f"Books limit of {value} is not valid", str(ex.exception))

    def test_len_method_returns_correct_number(self):
        bookstore = Bookstore(3)
        result = len(bookstore)
        self.assertEqual(0, result)

        bookstore.receive_book("LOTR", 1)
        bookstore.receive_book("Witcher", 2)

        result = len(bookstore)
        self.assertEqual(3, result)

    def test_receive_book_method_if_there_is_not_enough_space_in_the_bookstore(self):
        book_title = "Knijka"
        number_of_books = 110
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book(book_title, number_of_books)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_method_if_there_is_enough_space_in_the_bookstore(self):
        book_title = "Knijka"
        number_of_books = 9
        self.book_store.availability_in_store_by_book_titles = {"Kniga": 2, "Kniga2": 3}
        self.book_store.receive_book(book_title, number_of_books)
        expected_dict = {"Kniga": 2, "Kniga2": 3, "Knijka": 9}
        self.assertEqual(expected_dict, self.book_store.availability_in_store_by_book_titles)
        book_title = "Knijka"
        new_number = 18
        result = self.book_store.receive_book(book_title, number_of_books)
        expected = f"{new_number} copies of {book_title} are available in the bookstore."
        self.assertEqual(result, expected)

    # def test_receive_book_method_taking_the_new_availability_of_that_book(self):
    #     book_title = "Knijka"
    #     new_number = 20
    #     result = self.book_store.receive_book(book_title, new_number)
    #     expected = f"{new_number} copies of {book_title} are available in the bookstore."
    #     self.assertEqual(result, expected)

    def test_sell_book_method_if_the_book_is_not_available_in_the_bookstore(self):
        book_title = "Knijka"
        number_of_books = 9
        self.book_store.availability_in_store_by_book_titles = {"Kniga": 2, "Kniga2": 3}

        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book(book_title, number_of_books)

        self.assertEqual(f"Book {book_title} doesn't exist!", str(ex.exception))

    def test_sell_book_method_if_there_is_not_enough_copies_of_that_book_to_sell(self):
        book_title = "Kniga"
        number_of_books = 6
        self.book_store.availability_in_store_by_book_titles = {"Kniga": 2, "Kniga2": 3}

        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book(book_title, number_of_books)

        self.assertEqual(f"{book_title} has not enough copies to sell. Left: {2}", str(ex.exception))
        self.assertEqual(self.book_store.availability_in_store_by_book_titles, {"Kniga": 2, "Kniga2": 3})

    def test_sell_book_method_if_can_sell_successfully(self):
        book_title = "Kniga"
        number_of_books = 6
        self.book_store.availability_in_store_by_book_titles = {"Kniga": 10, "Kniga2": 3}
        result = self.book_store.sell_book(book_title, number_of_books)
        expected = f"Sold {number_of_books} copies of {book_title}"
        self.assertEqual(result, expected)
        self.assertEqual(self.book_store.total_sold_books, number_of_books)

    def test_str_method(self):
        self.book_store.availability_in_store_by_book_titles = {"Kniga": 10, "Kniga2": 3}
        self.book_store.sell_book("Kniga", 6)
        self.book_store.sell_book("Kniga2", 1)
        result = f'Total sold books: {self.book_store.total_sold_books}\n'
        result += f'Current availability: {len(self.book_store)}\n'
        for book_title, number_of_copies in self.book_store.availability_in_store_by_book_titles.items():
            result += f" - {book_title}: {number_of_copies} copies\n"
        expected = result.strip()
        actual = str(self.book_store)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main
