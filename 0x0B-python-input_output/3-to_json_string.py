#!/usr/bin/python3
import json
'''
    String serialization
'''


def to_json_string(my_obj):
    '''Returns the JSON representation of an object

    Args:
        my_obj: Object to serialize

    Returns:
        Serialized string
    '''
    serialized = json.dumps(my_obj, sort_keys=True)
    return (serialized)
