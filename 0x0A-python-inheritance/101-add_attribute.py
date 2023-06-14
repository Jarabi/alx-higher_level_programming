#!/usr/bin/python3
'''
    Add attribute to an object
'''


def add_attribute(obj, attr_name, value):
    '''
        Adds a new attribute to an object if possible
    '''

    # Check if  object is a type of class
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # Add attribute to object __dict__
    obj.__dict__[attr_name] = value
