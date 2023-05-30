#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element in two lists

    Args:
        my_list_1: First list
        my_list_2: Second list
        list_length: New list with all divisions
    """
    result = []

    for k in range(list_length):
        try:
            el_1 = my_list_1[k]
            el_2 = my_list_2[k]

            result.append(el_1 / el_2)
        except(TypeError, ZeroDivisionError, IndexError) as e:
            if (isinstance(e, TypeError)):
                print("wrong type")
            elif (isinstance(e, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(e, IndexError)):
                print("out of range")
            result.append(0)
        finally:
            pass
    return result
