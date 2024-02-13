#!/usr/bin/python3
"""
This file defines  the BaseModel class which will
serve as the base of ou model.
"""
import uuid
import datetime
import models


class BaseModel:
    """class BaseModel that defines all common attributes/methods for other classes

    Returns:
        str: id,updated_at,created_at,...etc
    """

    def __init__(self, *args, **kwargs):
        """Creates new instances of BaseModel"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.fromisoformat(value)
                    setattr(self, key, value)
            return
        models.storage.new(self)

    def __str__(self):
        """funcation return string

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>_description_
        """
        return "[{}] ({}) {}".format((self.__class__.__name__), self.id, self.__dict__)

    def save(self):
        """the current datetime when an instance is created and it will be updated every time you change your object"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """create a dictionary representation with “simple object type” of our BaseModel

        Returns:
            dictionary : copy dictionary
        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
