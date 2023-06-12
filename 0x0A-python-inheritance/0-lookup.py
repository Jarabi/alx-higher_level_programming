#!/usr/bin/python3

'''Returns the list of available attributes and methods
of an object.
'''


def lookup(obj):
    '''Get the available attributes and methods of an
    object, passed to function.

    Args:
        obj: The object

    Returns:
        List object of the attributes and methods
    '''
    new_list = []
    new_list.append(dir(obj))

    return (new_list)
