"""tests for City class"""

from models.city import City
import unittest
import json
import pep8


class City_Tests(unittest.TestCase):
    """tests for City class"""

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/city.py'])
        self.assertEqual(result.total_errors, 0)

    def test_City_clss(self):
        """check for class existence"""
        self.assertTrue(City.__doc__)

    def test_set_attr(self):
        """check for the public class attributes"""
        self.assertTrue(hasattr(City, "__init__"))
        self.assertTrue(hasattr(City, "created_at"))
        self.assertTrue(hasattr(City, "updated_at"))
        self.assertTrue(hasattr(City, "id"))
