#!/usr/bin/python3
"""module test_state of unittest class state"""

import unittest
from models.state import State


class testState(unittest.TestCase):
    """cases tests of state"""

    def setUp(self):
        self.stateOne = State()
        self.stateTwo = State()

    def test_type(self):
        """test the type"""
        self.assertEqual(type(self.stateOne.name), str)
        self.assertEqual(type(self.stateTwo.name), str)
        self.assertIsInstance(self.state, State)

    def test_attribute(self):
        """test the attibute"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(self.stateOne != self.stateTwo)

if __name__ == '__main__':
    unittest.main()
