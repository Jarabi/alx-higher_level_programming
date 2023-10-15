#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at a specific point.

    Args:
        my_list: list of elements
        idx: index at which to replace element
        element: Element to replace with

    Return: New list with replaced element
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)

    my_list[idx] = element
    return (my_list)
