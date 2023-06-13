#!/usr/bin/bash
'''
    Class to JSON
'''


def class_to_json(obj):
    '''
        Returns the dictionary description with simple data structure
        JSON serialization of an object
    '''
    return (vars(obj))
