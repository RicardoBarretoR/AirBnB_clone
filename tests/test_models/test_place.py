#!/usr/bin/python3
"""module test_place of unittest class place"""

import datetime
import uuid
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """case tests of place"""
    def setUp(self):
        self.placeOne = place()
        self.placeTwo = place()

    def tearDown(self):
        self.placeOne = None

    def test_attribute(self):
        self.assertTrue(hasattr(self.placeOne, "city_id"))
        self.assertTrue(hasattr(self.placeOne, "number_rooms"))
        self.assertTrue(hasattr(self.placeOne, "number_bathrooms"))
        self.assertTrue(hasattr(self.placeOne, "latitude"))
        self.assertTrue(hasattr(self.placeOne, "longitude"))
        self.assertTrue(hasattr(self.placeOne, "amenities"))
        self.assertTrue(hasattr(self.placeOne, "max_guest"))
        self.assertFalse(hasattr(self.placeOne, "no_guest"))
        self.assertTrue(hasattr(self.placeOne, "description"))
        self.assertTrue(hasattr(self.placeOne, "price_by_night"))
        self.assertTrue(hasattr(self.placeOne, "user_id"))
        self.assertTrue(hasattr(self.placeOne, "name"))
        self.assertTrue(type(self.placeOne.number_rooms) is int)
        self.assertTrue(type(self.placeOne.number_bathrooms) is int)
        self.assertTrue(type(self.placeOne.price_by_night) is int)
        self.assertTrue(type(self.placeOne.max_guest) is int)
        self.assertTrue(type(self.placeOne.latitude) is float)
        self.assertTrue(type(self.placeOne.longitude) is float)
        self.assertTrue(type(self.placeOne.name) is str)
        self.assertTrue(type(self.placeOne.city_id) is str)
        self.assertTrue(type(self.placeOne.user_id) is str)
        self.assertTrue(type(self.placeOne.description) is str)
        self.assertTrue(type(self.placeOne.amenities) is list)
        self.assertTrue(type(self.placeOne.id) is str)
        self.assertTrue(self.placeOne.id != self.placeTwo.id)
        test_created1 = self.placeOne.created_at
        test_created2 = self.placeTwo.created_at
        self.assertIsNot(test_created1, test_created2)
        self.assertTrue(type(test_created2) is datetime.datetime)

if __name__ == '__main__':
    unittest.main()
