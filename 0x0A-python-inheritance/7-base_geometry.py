#!/usr/bin/python3
'''
    BaseGeometry class
'''


class BaseGeometry:
    '''
        A BaseGeometry class.
    '''
    def area(self):
        '''Public function that raises an exception

        Raises:
            Exception: area() is not implemented.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Public instance method that validates an integer value

        Args:
            name: string argument
            value: argument to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
