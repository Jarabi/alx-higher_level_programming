#!/usr/bin/python3
'''Print a square using the character #

    >>> print_square(2)
    ##
    ##
'''


def print_square(size):
    '''Function prints a square with length ``size`` using #

    Args:
        size: The length of the square

    Raises:
        TypeError: size is not an integer
        ValueError: size < 0
    '''
    type_err = "size must be an integer"
    value_err = "size must be >= 0"

    if not isinstance(size, int):
        raise TypeError(type_err)

    if size < 0:
        raise ValueError(value_err)

    if isinstance(size, float) and size < 0:
        raise TypeError(type_err)

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
