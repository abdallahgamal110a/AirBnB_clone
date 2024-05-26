#!/usr/bin/python3
""" Module Base model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Custom base for all the classes in the AirBnb console project

    Arttributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id, and creates dictionary
        representations of the input values
        save(self): updates instance arttributes with current datetime
        to_dict(self): returns the dictionary values of the instance obj

    """

    def __init__(self):
        """Public instance artributes initialization
        after creation

        Args:
            *args(args): arguments
            **kwargs(dict): attrubute values
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """
        Returns string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
        Method returns a dictionary containing all
        keys/values of __dict__ instance
        """
        copy_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                copy_dict[key] = value.isoformat()
            elif key == "__class__":
                copy_dict[key] = self.__class__.__name__
            else:
                copy_dict[key] = value
        return copy_dict
