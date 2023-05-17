#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if a_dictionary is None:
        return (None)

    highest_key = ""
    first_key = list(a_dictionary)[0]
    highest_value = a_dictionary.get(first_key)

    for k, v in a_dictionary.items():
        if v > highest_value:
            highest_key = k
    return (highest_key)
