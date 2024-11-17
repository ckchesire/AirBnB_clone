#!/usr/bin/python3
"""File storage module to serialize to and deserialize from Json files
"""
import json
from models.base_model import BaseModel
import datetime as dt


class FileStorage:
    """Class for Serializing to JSON file and deserializing from JSON file

        Args:
            __file_path(str): string path to Json file
            __objects(dict): stores base object with the <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Method to return dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """Method to assign __objects the obj using key of class name's id

            Args:
                obj(dict): dictionary of class key value pairs
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Method to serialize __objects to Json File
        """
        try:
            current_data = {}
            with open(self.__file_path, 'r') as file:
                current_data = json.load(file)
        except FileNotFoundError:
            pass

        serialized_objects = {}
        for obj in self.__objects.keys():
            serialized_objects[obj] = self.__objects[obj].to_dict()

        combined_data = {**current_data, **serialized_objects}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(combined_data, file, indent=4)

    def reload(self):
        """Method deserializes Json file to __objects if file exists
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_obj = json.load(file)

            for key, val in json_obj.items():
                class_name, obj_id = key.split('.')
                cls = eval(class_name)
                instance = cls(**val)
                FileStorage.__objects[key] = instance

        except FileNotFoundError:
            pass
