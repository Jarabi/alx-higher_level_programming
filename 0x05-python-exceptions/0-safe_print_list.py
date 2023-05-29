#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list

    Args:
        my_list: List of elements
        x: The number of elements to print
    """
    try:
        current = 0

        for i in range(x):
            current = my_list[i]
            print("{:d}".format(current), end="")
    except IndexError:
        pass
    finally:
        print()
    return (current)
