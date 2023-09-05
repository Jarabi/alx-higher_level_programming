#!/usr/bin/python3
"""
Find peak value
"""


def find_peak(list_of_integers):
    """
    A function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: list of integers

    Return:
        Peak value
    """

    if not isinstance(list_of_integers, list):
        return None

    list_len = len(list_of_integers)

    if not list_of_integers or list_len == 0:
        return None

    if list_len == 1:
        return list_of_integers[0]

    start = 0
    end = list_len - 1

    while start < end:
        mid = (start + end) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
