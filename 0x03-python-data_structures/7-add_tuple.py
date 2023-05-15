#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds 2 tuples

    Args:
        tuple_a: First tuple
        tuple_b: Second tuple
    Return:
        Tuple with the summed up elements
    """
    lst_a = [0, 0]
    lst_b = [0, 0]

    check_tuple(lst_a, tuple_a)
    check_tuple(lst_b, tuple_b)

    a = lst_a[0] + lst_b[0]
    b = lst_a[1] + lst_b[1]

    return (a, b)

def check_tuple(lst, tupl):
    for idx, el in enumerate(tupl):
        lst[idx] = el
