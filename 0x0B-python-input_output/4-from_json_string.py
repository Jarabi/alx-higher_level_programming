#!/usr/bin/python3
'''
    Deserialize an object
'''
import json


def from_json_string(my_str):
    '''
        Returns an object represented bt a JSON string
    '''
    return (json.loads(my_str))
