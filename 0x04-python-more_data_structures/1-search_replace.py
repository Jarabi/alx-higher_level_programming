#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.
    """
    replaced = []

    for _ in my_list:
        if _ == search:
            _ = replace
        replaced.append(_)
    return (replaced)
