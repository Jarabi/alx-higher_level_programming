#!/usr/bin/python3
"""
Roman to integer
"""


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer

    Args:
        roman_string (int): The Roman numeral string

    Returns:
        Integer
        0, if roman_string is not a string or None
    """
    value = 0

    if not isinstance(roman_string, str) or roman_string == 'None':
        return value

    symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    for idx in range(len(roman_string)):
        left = symbols[roman_string[idx]]
        right = symbols[roman_string[idx + 1]] \
            if idx < len(roman_string) - 1 else 0

        if left < right:
            value -= left
        else:
            value += left

    return value
