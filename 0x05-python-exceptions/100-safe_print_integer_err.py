#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer.

    Args:
        value: Value to be printed
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as e:
        sys.stderr.write("Exception: " + str(e) + "\n")
        return False
