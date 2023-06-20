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

    def __str__(self):
        '''
        Overload the __str__ method
        '''
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.x}/{self.y} - {self.width}"
