#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element from a list

    Args:
        my_list: the list
        idx: index at which to retrieve element
    Return:
        Retireved element or None
    """
    if idx < 0 or idx >= len(my_list):
        return ("None")
    return (my_list[idx])
