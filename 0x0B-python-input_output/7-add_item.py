#!/usr/bin/python3
'''
    Adds arguments to a Python list, then save them to a file.
'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args(args):
    '''
        A script that adds all arguments to a Python list
        and saves them to a file
    '''
    filename = "add_item.json"

    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    # Update my_list
    my_list.extend(args)

    # Save new list structure to json file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_args(args)
