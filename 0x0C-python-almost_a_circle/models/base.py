#!/usr/bin/python3
'''
    Base class
'''
import json
import os


class Base:
    '''
        Base class for all other classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Class constructor

        Args:
            id: public instance attribute
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation to a file.
        """
        json_string = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                json_string.append(json_dict)

        filename = cls.__name__ + ".json"

        with open(filename, "w") as f:
            json.dump(json_string, f)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns list of JSON string representation
        """
        if json_string is None or not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        if cls.__name__ == "Square":
            polygon = cls(3)
        elif cls.__name__ == "Rectangle":
            polygon = cls(3, 5)

        polygon.update(**dictionary)
        return (polygon)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        """
        instances = []
        filename = cls.__name__ + ".json"

        try:
            with open(filename, encoding="utf-8") as f:
                data = f.read()

            json_string = cls.from_json_string(data)
        except IOError:
            return []

        for instance in json_string:
            instances.append(cls.create(**instance))

        return instances
