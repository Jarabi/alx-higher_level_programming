#!/usr/bin/python3
'''
    Student module
'''


class Student:
    '''
        Student class
    '''
    def __init__(self, first_name, last_name, age):
        '''
            Initialize instance variables
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
            Retrieve dictionary representation of a class
        '''
        class_dict = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if not isinstance(attr, str):
                    class_dict = self.__dict__
                    break
                try:
                    class_dict[attr] = getattr(self, attr)
                except AttributeError:
                    pass
        else:
            class_dict = self.__dict__

        return (class_dict)

    def reload_from_json(self, json):
        '''
            Replaces all attributes of the Student instance
        '''
        for key, val in json.items():
            self.__setattr__(key, val)
