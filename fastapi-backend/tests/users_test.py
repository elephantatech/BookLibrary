import unittest
from models.users import user
import datetime
from pydantic import ValidationError


class test_users_model(unittest.TestCase):
    def test_user(self):
        userdata = {
            "first_name": "joe",
            "last_name": "doe",
            "email": "joe.doe@example.com",
            "password": "password",
            "phone": "6476476476",
            "dob": datetime.datetime(2009, 10, 5, 18, 00),
            "comments": None,
        }
        actual = user(**userdata)

        self.assertEqual(userdata, actual)

    def test_user_validatedate(self):
        userdata = {
            "first_name": "joe",
            "last_name": "doe",
            "email": "joe.doe@example.com",
            "password": "password",
            "phone": "6476476476",
            "dob": None,
            "comments": None,
        }

        self.assertRaises(ValidationError, user, **userdata)

    def test_user_validate_email(self):
        userdata = {
            "first_name": "joe",
            "last_name": "doe",
            "email": "example.com",
            "password": "password",
            "phone": "6476476476",
            "dob": datetime.datetime(2009, 10, 5, 18, 00),
            "comments": None,
        }

        self.assertRaises(ValidationError, user, **userdata)
