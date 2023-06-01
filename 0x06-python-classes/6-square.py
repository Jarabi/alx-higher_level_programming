#!/usr/bin/python3
'''Square class definition'''


class Square:
    '''Definition of a square based ona private instance attribute'''
    def __init__(self, size=0, position=(0, 0)):
        '''Attribute definition

        Args:
            size (int): Size of the square
            position (tuple): Coordinates
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Retrieves private attribute - size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Updates private attribute.

        Args:
            value (int): Positive integer to update size attribute
        '''
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        '''Retrieves attribute'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Update private attribute - position

        Args:
            value: Tuple of two positive numbers
        '''
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and value[0] >= 0:
                if isinstance(value[1], int) and value[0] >= 0:
                    self.__position = value
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''Class method area

        Returns:
            Current square area
        '''
        return self.__size * self.__size

    def my_print(self):
        '''Class method my_print

        Prints in stdout the square with the character #
        '''
        if self.__size > 0:
            for _ in range(self.__position[1]):
                print()
            for col in range(self.__size):
                print("{}{}".format(" "*self.__position[0], "#"*self.__size))
        else:
            print()
