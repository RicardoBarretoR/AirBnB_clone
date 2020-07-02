#!/usr/bin/python3
"""module test_amenity of unittest class Amenity """

import pep8
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """cases tests of amenity"""

    def setUp(self):
        """sets up objects for testing"""
        self.amenityOne = Amenity()
        self.amenityTwo = Amenity()

    def test_pep8(self):
        """check for pep8"""
        pep8style = pep8.StyleGuide(quite=True)
        result = pep8style.check_files(['./models/amenity.py'])
        self.assertEqual(result.total_errors, 0)

    def test_type(self):
        """test the type"""
        self.assertEqual(type(self.amenityOne.name), str)
        self.assertEqual(type(self.amenityTwo.name), str)
        self.assertIsInstance(self.amenityOne, Amenity)
        self.assertIsInstance(self.amenityTwo, Amenity)

    def test_attribute(self):
        """test the attibute"""
        self.assertTrue(hasattr(self.amenityOne, "name"))
        self.assertFalse(hasattr(self.amenityOne, "user_id"))
        self.assertTrue(self.amenityOne.id != self.amenityTwo.id)

if __name__ == '__main__':
    unittest.main()
