#!/usr/bin/python3

'''Square class definition'''


class Square:
    '''Definition of a square based ona private instance attribute'''
    def __init__(self, size=0):
        '''Attribute definition

        Args:
            size(int): Size of the square
        '''
        try:
            isinstance(size, int)

            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        except TypeError:
            print("size must be an integer")
