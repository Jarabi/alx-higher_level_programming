#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x int elements of a list.

    Args:
        my_list: The list
        x: The number of elements to access
    """
    count = 0

    try:
        for m in range(x):
            try:
                print("{:d}".format(my_list[m]), end="")
                count += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        raise
    finally:
        print()
    return (count)
