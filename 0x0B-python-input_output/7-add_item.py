#!/usr/bin/python3
'''
    Adds arguments to a Python list, then save them to a file.
'''
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_list = []
filename = "add_item.json"
args = sys.argv[1:]

if len(args) > 0:
    # Get list from json file
    my_list = load_from_json_file(filename)

    # Update my_list
    my_list.extend(args)

# Save new list structure to json file
save_to_json_file(my_list, filename)
