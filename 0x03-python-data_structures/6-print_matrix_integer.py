#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers

    Args:
        matrix: A 2-dimensional array
    Return:
        Nothing
    """
    for outer in matrix:
        for idx, elem in enumerate(outer):
            print("{:d}".format(elem), end="")

            if idx < len(outer) - 1:
                print(" ", end="")
        print()
