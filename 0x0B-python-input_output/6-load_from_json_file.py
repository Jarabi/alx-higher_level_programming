#!/usr/bin/python3
'''
    Create object from a JSON file
'''
import json


def load_from_json_file(filename):
    '''
      A function that creates an Object from a “JSON file”
    '''
    with open(filename, encoding="utf-8") as f:
        read_str = f.read()

    return (json.loads(read_str))
