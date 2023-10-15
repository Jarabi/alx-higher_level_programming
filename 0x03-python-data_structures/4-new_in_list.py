#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position
        without modifying the original list.
    Args:
        my_list: Original list
        idx: Index at wich to replace element
        element: Element to replace with
    Return:
        Copy of the list
    """
    new_list = my_list[:]

    if idx < 0 or idx >= len(my_list):
        return (new_list)

    new_list[idx] = element
    return (new_list)
