#!/usr/bin/python3
def safe_print_division(a, b):
    """Prints result of division of two integers

    Args:
        a: First integer
        b: Second integer
    """
    try:
        division = a / b
    except ZeroDivisionError:
        division = "None"
    finally:
        print("Inside result: {}".format(division))
    return (division)
