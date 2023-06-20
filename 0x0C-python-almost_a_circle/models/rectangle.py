#!/usr/bin/python3
'''
Rectangle class
'''
from models.base import Base


class Rectangle(Base):
    '''
    Rectangle class
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''
        Return a private attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        Set value for private attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
        Return a private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        Setter for private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
        Return private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
        Setter for private attribute
        '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''
        Return private atriibute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
        Setter for private attribute
        '''
        self.setter_validation("y", value)
        self.__y = value

    @staticmethod
    def setter_validation(attr, value):
        '''
        Validates setter attributes
        '''
        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")

        if attr == "width" or attr == "height":
            if value <= 0:
                raise ValueError(f"{attr} must be > 0")
        elif value < 0:
            raise ValueError(f"{attr} must be >= 0")

    def area(self):
        '''
        Return the area of a rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''
        Print rectangle representation using # character
        '''
        rect = ""
        print("\n" * self.y, end="")
        for _ in range(self.__height):
            rect += (" " * self.x) + ("#" * self.width) + "\n"
        print(rect, end="")

    def __str__(self):
        '''
        Override the __str__ method to return string representation
        of rectangle attributes
        '''
        class_name = self.__class__.__name__
        w = self.__width
        h = self.__height
        return f"[{class_name}] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        '''
        Updates class attributes
        '''
        if len(args) == 0:
            for key in val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
