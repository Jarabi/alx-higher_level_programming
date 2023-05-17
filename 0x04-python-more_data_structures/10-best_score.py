#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not a_dictionary:
        return (None)

    # Get first key to use for comparison
    highest_key = list(a_dictionary)[0]
    highest_value = a_dictionary.get(highest_key)

    for k, v in a_dictionary.items():
        if v > highest_value:
            highest_key = k
            highest_value = v
            print("Updated: {}: {}".format(k, v))
        print("Not updated: {}: {}".format(k, v))
    return (highest_key)
