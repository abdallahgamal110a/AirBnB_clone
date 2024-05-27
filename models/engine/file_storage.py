#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class.
"""

import json
from models.base_model import BaseModel


class FileStorage(BaseModel):
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, obj in obj_dict.items():
                    class_name = key.split(".")[0]
                    self.__objects[key] = eval(class_name)(**obj)
        except FileNotFoundError:
            pass  
