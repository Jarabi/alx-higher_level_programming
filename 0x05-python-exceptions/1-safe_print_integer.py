#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer.

    Args:
        value: Value to be printed
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
