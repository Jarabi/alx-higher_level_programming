#!/usr/bin/python3
'''
This module supplies one function: add_integer(a, b). Example usage:
    >>> add_integer(10, 5)
    15
'''


def add_integer(a, b=98):
    '''Returns the sum of two integers

    Args:
        a: first parameter
        b: optional parameter. Default set to 98

    Raises:
        TypeError: If a or b are neither int nor float

    Returns:
        Sum of a and b
    '''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
