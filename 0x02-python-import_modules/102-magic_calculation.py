#!/usr/bin/python3

def magic_calculation(a, b):
    """Python code that emulates Python bytecode

    Args:
        a: First argument
        b: Second argument
    Return:
        Calculated value
    """
    from magic_calculation_102 import add, sub  # import

    if a < b:  # comparison
        c = add(a, b)  # addition
        for i in range(4, 6):  # iteration using range
            c = add(c, i)
        return (c)  # return value of summation
    return (sub(a, b))  # return subtraction value
