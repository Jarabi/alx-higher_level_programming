#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """A function that adds 2 tuples

    Args:
        tuple_a: First tuple
        tuple_b: Second tuple
    Return:
        Another tuple with the summed up elements
    """
    arr = []

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tup_b = (tuple_b[0], 0)
        else:
            tup_b = (0, 0)
    else:
        tup_b = tuple_b

    for el in range(0, len(tuple_a)):
        arr.append(tuple_a[el] + tup_b[el])

    return (tuple(arr))
