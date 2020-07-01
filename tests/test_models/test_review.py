#!/usr/bin/python3
"""module test_review of unittest class review"""

import unittest
from models.review import Review


class testReview(unittest.TestCase):
    """cases tests of review"""
    def setUp(self):
        """ Setup instances of the Review Class """
        self.reviewOne = Review()
        self.b_inst = Review()
        self.b_inst.save()

    def test_setup(self):
        """ Tests for creating instances """
        self.assertTrue(self.reviewOne .id != self.b_inst.id)
        self.assertFalse(hasattr(self.reviewOne, "updated_at"))
        self.assertTrue(hasattr(self.reviewOne, "place_id"))
        self.assertTrue(hasattr(self.b_inst, "place_id"))
        self.assertTrue(hasattr(self.reviewOne, "user_id"))
        self.assertTrue(hasattr(self.b_inst, "user_id"))
        self.assertTrue(hasattr(self.reviewOne, "text"))
        self.assertTrue(hasattr(self.b_inst, "text"))
        self.assertTrue(self.reviewOne .created_at != self.b_inst.created_at)

    def test_types(self):
        """ Testing for types """
        self.assertTrue(type(self.reviewOne.created_at) is datetime.datetime)
        self.assertTrue(type(self.reviewOne.place_id) is str)
        self.assertTrue(type(self.reviewOne.user_id) is str)
        self.assertTrue(type(self.reviewOne.text) is str)
        a_json = self.reviewOne.to_json()
        self.assertTrue(type(a_json["created_at"]) is str)

if __name__ == '__main__':
    unittest.main()
