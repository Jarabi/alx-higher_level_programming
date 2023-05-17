#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""

    double_dict = {}

    for k, v in a_dictionary.items():
        double_dict[k] = v * 2

    return (double_dict)
