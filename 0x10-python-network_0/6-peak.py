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

    if not list_of_integers:
        return None

    peak_value = 0
    list_len = len(list_of_integers)

    if list_len == 1:
        peak_value = list_of_integers[0]

    elif list_len == 2:
        list_0 = list_of_integers[0]
        list_1 = list_of_integers[1]

        peak_value = list_0 if list_0 > list_1 else list_1
    else:
        peak_value = list_of_integers[0]
        index = 1

        while index < (list_len - 1):
            if list_of_integers[index] > list_of_integers[index - 1] and \
                    list_of_integers[index] > list_of_integers[index + 1]:
                peak_value = list_of_integers[index]
            index += 1

    return peak_value
