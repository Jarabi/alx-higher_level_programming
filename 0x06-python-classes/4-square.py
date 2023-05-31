#!/usr/bin/python3

'''Square class definition'''


class Square:
    '''Definition of a square based ona private instance attribute'''
    def __init__(self, size=0):
        '''Attribute definition

        Args:
            size(int): Size of the square
        '''
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        '''Class method area

        Returns:
            Current square area
        '''
        return self.__size * self.__size
