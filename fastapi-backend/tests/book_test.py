import unittest
from models import books
import datetime
from pydantic import ValidationError


class test_book_model(unittest.TestCase):
    def test_book(self):
        bookdata = {
            "title": "12312",
            "book_synopsis": None,
            "author": "dsfksdj",
            "published_date": datetime.datetime(2009, 10, 5, 18, 00),
            "edition": "1",
            "ISDN_number": None,
            "comments": None,
        }
        actual = books.book(**bookdata)

        self.assertEqual(bookdata, actual)

    def test_book_validatedate(self):
        bookdata = {
            "title": "12312",
            "book_synopsis": None,
            "author": "dsfksdj",
            "published_date": "",
            "edition": "1",
            "ISDN_number": None,
            "comments": None,
        }

        self.assertRaises(ValidationError, books.book, **bookdata)
