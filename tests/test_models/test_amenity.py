#!/usr/bin/python3
"""module test_amenity of unittest class Amenity """

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """cases tests of amenity"""

    def setUp(self):
        self.amenityOne = Amenity()
        self.amenityTwo = Amenity()

    def test_type(self):
        """test the type"""
        self.assertEqual(type(self.amenityOne.name), str)
        self.assertEqual(type(self.amenityTwo.name), str)
        self.assertIsInstance(self.amenity, Amenity)

    def test_attribute(self):
        """test the attibute"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(self.amenityOne != self.amenityTwo)

if __name__ == '__main__':
    unittest.main()
