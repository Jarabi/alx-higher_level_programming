#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Returns a set of common elements present in only one set."""
    return (set_1 ^ set_2)
