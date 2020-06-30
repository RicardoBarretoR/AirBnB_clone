#!/usr/bin/python3
"""test for User class"""

from models.user import User
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
        """check class existence"""
        self.assertTrue(User.__doc__)

    def test_set_attr(self):
        """check for public class attributes"""
        self.assertTrue(hasattr(User, "__init__")
        self.assertTrue(hasattr(User, "created_at")
        self.assertTrue(hasattr(User, "updated_at")
        self.assertTrue(hasattr(User, "id")
