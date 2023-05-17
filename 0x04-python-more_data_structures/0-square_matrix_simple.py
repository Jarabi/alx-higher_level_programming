#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    Args:
        matrix: A 2-dimensional array
    """
    squares = []

    # Make copy of matrix array
    for _ in range(0, len(matrix)):
        row = [0] * len(matrix[_])
        squares.append(row)

    # Update new array with squares of matrix elements
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            squares[row][col] = matrix[row][col] ** 2

    return (squares)
