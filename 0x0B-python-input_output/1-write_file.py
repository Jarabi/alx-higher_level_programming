#!/usr/bin/python3
'''
    Writes a string to a text file
'''


def write_file(filename="", text=""):
    '''Function that writes a string to a text file
    and returns the number of characters written.

    Args:
        filename: File to write to
        text: String to write in file
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        write_count = f.write(text)

    return (write_count)
