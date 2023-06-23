#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''
    Testing for Base class
    '''
    def test_id_none(self):
        '''
        Sending no id to instance
        '''
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id(self):
        '''
        Sending valid id
        '''
        b = Base(23)
        self.assertEqual(b.id, 23)

    def test_zero(self):
        '''
        Send value of 0
        '''
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative(self):
        '''
        Send negative value
        '''
        b = Base(-1)
        self.assertEqual(b.id, -1)

    def test_string(self):
        '''
        Sending a string
        '''
        b = Base("Test")
        self.assertEqual(b.id, "Test")

    def test_list(self):
        '''
        Send a list
        '''
        b = Base([0, 9])
        self.assertEqual(b.id, [0, 9])


if __name__ == "__main__":
    unittest.main()
