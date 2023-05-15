#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: A 2-dimensional array
    Return:
        Nothing
    """
    for outer in matrix:
        for k in range(0, len(outer)):
            print("{:d}".format(outer[k]), end="")

            if k == 2:
                continue
            print(" ", end="")
        print()
