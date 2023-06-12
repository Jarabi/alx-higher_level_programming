#!/usr/bin/python3
'''
    Rectangle class
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
        Implements a rectangle class. Inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''Validates argument and instantiates variables

        Args:
            width: width of rectangle
            height: height of rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def print(self):
        '''Prints rectangle description'''

        print("[{}] {}/{}".format(
            type(self).__name__,
            self.__width,
            self.__height
            )
        )

    def __str__(self):
        '''Returns rectangle description'''

        return "[{}] {}/{}".format(
                type(self).__name__,
                self.__width,
                self.__height
        )

    def area(self):
        '''Returns the area of rectangle'''

        return (self.__width * self.__height)
