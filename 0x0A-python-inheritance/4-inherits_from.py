#!/usr/bin/python3
'''A function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class; otherwise False.
'''


def inherits_from(obj, a_class):
    '''Returns True if obj inherits from a_class.

    Args:
        obj: the oject
        a_class: the class

    Returns:
        True if inherits, else False
    '''
    return (issubclass(obj, a_class))
