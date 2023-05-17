#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print dictionary by ordered keys."""

    sorted_dict = sorted(a_dictionary)

    for key in sorted_dict:
        print("{key}: {val}".format(key=key, val=a_dictionary[key]))
