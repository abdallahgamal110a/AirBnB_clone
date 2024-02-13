#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __object = {}

    def all(self):
        """
            Method return the dictionary __objects
        Returns:
            dic: the dictionary __objects
        """
        return FileStorage.__object

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        Args:
            obj (dict): dictionary
        """
        self.__object = obj
        key = "{}.{}".format(type(obj.__name__), obj.id)
        FileStorage.__object[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w") as file:
            json.dump({k: v.to_dic() for v, k in FileStorage.__object.items()}, file)

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file:
            deserialized = None

        try:
            deserialized = json.load(file)
        except json.JSONDecodeError:
            pass
        if deserialized is None:
            return
