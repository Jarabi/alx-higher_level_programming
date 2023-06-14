#!/usr/bin/python3
'''
    Add attribute to an object
'''


def add_attribute(obj, attr_name, value):
    '''
        Adds a new attribute to an object if possible
    '''
    # If object is type of a class
    if type(obj).__name__ != 'MyClass':
        raise TypeError("can't add new attribute")

    # If object already hass the attribute
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")

    # Add attribute to object __dict__
    obj.__dict__[attr_name] = value
