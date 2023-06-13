#!/usr/bin/python3
'''
    Class to JSON
'''


def class_to_json(obj):
    '''
        Returns the dictionary description with simple data structure
        JSON serialization of an object
    '''
    return (getattr(obj, '__dict__'))
