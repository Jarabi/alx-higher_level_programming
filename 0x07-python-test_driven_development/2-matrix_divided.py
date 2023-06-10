#!/usr/bin/python3

'''
Divide elements of a matrix by a number. Usage:
    matrix_divided(matrix, div)
Example:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]])
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix

    Args:
        matrix: a list of integers or floats, each row of the same size
        div: an integer or float that will be used as the divisor
    Raises:
        TypeError: if not a list of integers or floats, or if each row
                    of matrix is not the same size, or div is 0
    Returns:
        A new matrix
    '''
    new_matrix = []
    type_err = "matrix must be a matrix (list of lists) of integers/floats"
    list_size_err = "Each row of the matrix must have the same size"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(type_err)

    for row in matrix:
        new_row = []

        if not isinstance(row, list):
            raise TypeError(type_err)

        if len(row) != len(matrix[0]):
            raise TypeError(list_size_err)

        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(type_err)
            quotient = round((el / div), 2)
            new_row.append(quotient)
        new_matrix.append(new_row)
    return (new_matrix)
