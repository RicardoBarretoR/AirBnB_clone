#!/usr/bin/python3
"""test for User class"""

from models.user import User
from models.base_model import BaseModel
import unittest
import json
import pep8


class User_Tests(unittest.TestCase):
    """tests for User class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/user.py'])
        self.assertEqual(result.total_errors, 0)

    def Test_User_cls(self):
        """check for existence class"""
        self.user = User()
        self.assertTrue(User.__doc__)

    def test_user_subclss(self):
        """check for subclass of Superclass"""
        self.user = User()
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "id"))

    def test_user_attributes(self):
        """checks for user attributes"""
        self.user = User()
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_user_str_(self):
        """check for public class attributes"""
        pass
