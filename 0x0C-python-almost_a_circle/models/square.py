#!/usr/bin/python3
'''
Square class
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Square class. Inherits from Rectangle
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''
        Returns width of square
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''
        Set width and height
        '''
        self.setter_validation("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        '''
        Overload the __str__ method
        '''
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.x}/{self.y} - {self.width}"
