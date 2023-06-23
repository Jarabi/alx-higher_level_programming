#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    '''
    Testing for Rectangle class
    '''
    def setUp(self):
        '''
        Initialize instance with width and height
        '''
        self.rect = Rectangle(10, 2)

    def tearDown(self):
        '''
        Destroy instance
        '''
        del self.rect

    def test_width(self):
        '''
        Testing width getter
        '''
        self.assertEqual(self.rect.width, 10)

    def test_height(self):
        '''
        Testing height getter
        '''
        self.assertEqual(self.rect.height, 2)

    def test_x(self):
        '''
        Test x getter and setter
        '''
        self.rect.x = 11
        self.assertEqual(self.rect.x, 11)

    def test_y(self):
        '''
        Test y getter and setter
        '''
        self.rect.y = 9
        self.assertEqual(self.rect.y, 9)

    def test_rect_id(self):
        '''
        Test rectangle id
        '''
        rect = Rectangle(10, 2, 11, 9, 23)
        self.assertEqual(rect.id, 23)

    def test_width_string(self):
        '''
        Test for string width
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle("3", 5)

    def test_width_list(self):
        '''
        Test for list width
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle([1, 2], 3)

    def test_height_string(self):
        '''
        Test for string height
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(47, "9")

    def test_height_list(self):
        '''
        Test for list height
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(90, [4, 5, 6])
