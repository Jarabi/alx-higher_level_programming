#!/usr/bin/python3
import unittest
from models.square import Square
"""
Test cases for square module
"""


class test_square(unittest.TestCase):
    """
    Test square instances
    """

    def setUp(self):
        """
        Initialize square width
        """
        self.sqr = Square(5)

    def tearDown(self):
        """
        Remove created instances
        """
        del self.sqr

    def test_width(self):
        """
        Testing width getter
        """
        self.assertEqual(self.sqr.width, 5)

    def test_height(self):
        """
        Testing height getter
        """
        self.assertEqual(self.sqr.height, 5)

    def test_x(self):
        """
        Test x getter
        """
        self.sqr.x = 9
        self.assertEqual(self.sqr.x, 9)
        self.assertEqual(self.sqr.y, 0)

    def test_y(self):
        """
        Test y getter
        """
        self.sqr.y = 11
        self.assertEqual(self.sqr.y, 11)
        self.assertEqual(self.sqr.x, 0)

    def test_id(self):
        """
        Test square id
        """
        sqr = Square(2, 3, 1, 99)
        self.assertEqual(sqr.id, 99)


if __name__ == "__main__":
    unittest.main()
