#!/usr/bin/python3
'''This module demonstrates real definition of a rectangle.'''


class Rectangle:
    '''This class defines a rectangle based on provided width and height.'''

    def __init__(self, width=0, height=0):
        '''Instantiation of width and height

        Args:
            width: width of rectangle
            height: height of rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method to retrieve width.

        Returns:
            width of rectangle
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''Property setter to update width

        Args:
            value: Used to set the width

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0
        '''
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        '''Getter method to retrieve height.

        Returns:
            Height of rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''Property setter to update height

        Args:
            value: Used to set the height

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0
        '''
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        '''Public instance method that returns the area of a rectangle.

        Returns:
            The area of a rectangle.
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Public instance method that returns the perimeter of a rectangle.

        Returns:
            The perimeter of rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
