"""tests for City class"""

from models.city import City
from models.base_model import BaseModel
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
        """check for public class attributes"""
        self.city = City()
        self.assertIsInstance(self.city, BaseModel)
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "id"))

    def test_user_attributes(self):
        """"""
        self.city = City()
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")
