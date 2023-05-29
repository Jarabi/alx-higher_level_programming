#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer.

    Args:
        value: Value to be printed
    """
    try:
        if value:
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
