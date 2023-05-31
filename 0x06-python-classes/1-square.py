#!/usr/bin/python3

'''Square definition class'''


class Square:
    '''Defines a square using a private attribute'''
    def __init__(self, size):
        '''Definition of private attribute

        Args:
            size(int): Size of the square
        '''
        self.__size = size
