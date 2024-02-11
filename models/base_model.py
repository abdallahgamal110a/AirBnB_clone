#!/usr/bin/python3
import uuid
import datetime


class BaseModel:
    """class BaseModel that defines all common attributes/methods for other classes

    Returns:
        str: id,updated_at,created_at,...etc
    """

    id = None
    updated_at = None
    created_at = None

    def __init__(self, *args, **kwargs):
        """Creates new instances of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """funcation return string

        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>_description_
        """
        return "[{}] ({}) {}".format((self.__class__.__name__), self.id, self.__dict__)

    def save(self):
        """the current datetime when an instance is created and it will be updated every time you change your object"""
        self.updated_at = datetime.datetime.now()

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
