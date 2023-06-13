#!/usr/bin/python3
'''
    Appends a string at the end of a text file
'''


def append_write(filename="", text=""):
    '''Function that appends a string at the end of a
    text file and returns the number of characters added.

    Args:
        filename: File to append to
        text: String to append to file
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        write_count = f.write(text)

    return (write_count)
