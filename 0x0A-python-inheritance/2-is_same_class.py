#!/usr/bin/python3
'''
    Returns True if an object is excatly an instance of the specified class,
    otherwise False
'''


def is_same_class(obj, a_class):
    '''Return true if obj is instance of a_class.

    Args:
        obj: object to check
        a_class: the class

    Returns:
        True is obj is instance of a_class. False otherwise
    '''
    return (type(obj).__name__ == a_class.__name__)
