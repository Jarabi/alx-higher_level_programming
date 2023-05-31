#!/usr/bin/python3

'''Square class definition'''


class Square:
    '''Definition of a square based ona private instance attribute'''
    def __init__(self, size=0):
        '''Attribute definition

        Args:
            size(int): Size of the square
        '''
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
