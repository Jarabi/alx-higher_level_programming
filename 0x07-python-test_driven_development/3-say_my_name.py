#!/usr/bin/python3

'''
Print out names in the form My name is <first name> <last name>

    >>> say_my_name("Alex", "Jarabi")
    My name is Alex Jarabi
'''


def say_my_name(first_name, last_name=""):
    '''Printss formatted names to stdout

    Args:
        first_name: The first name
        last_name: The second name

    Raises:
        TypeError: first_name/last_name not type string
    '''
    err_msg = "{} must be a string"

    if not isinstance(first_name, str):
        raise TypeError(err_msg.format('first_name'))

    if not isinstance(last_name, str):
        raise TypeError(err_msg.format('last_name'))

    print("My name is {} {}".format(first_name, last_name))
