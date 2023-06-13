#!/usr/bin/python3
'''
    Reads a file.
'''


def read_file(filename=""):
    '''Read a file and print to stdout

    Args:
        filename: File to read
    '''
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data, end="")
