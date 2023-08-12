#!/usr/bin/python3

"""
This module has a function that prints a text with 2 new lines
after each of these characters: '.', '?' and ':'
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after
    specified delimiters.

    Args:
        text: A string of text

    Returns:
        (str): Indented text

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delims = {'.', ':', '?'}
    is_delim = False

    for char in text:
        if is_delim and char == ' ':
            continue
        if char in delims:
            print(f"{char}")
            print()
            is_delim = True
        else:
            print(f"{char}", end="")
            is_delim = False
