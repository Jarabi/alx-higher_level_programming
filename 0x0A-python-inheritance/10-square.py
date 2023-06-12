#!/usr/bin/python3
'''
    Square class
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
        Square class that inherits from Rectangle
    '''
    def __init__(self, size):
        '''Instantiate with size

        Args:
            size: length of square side
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        '''
            Return area of square
        '''
        return (self.__size ** 2)
