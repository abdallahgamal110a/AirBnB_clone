#!/usr/bin/python3
import datetime
import uuid


class BaseModel:

    def __init__(self):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):

        my_dict = {}

        for key, value in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                my_dict[key] = datetime.datetime.fromisoformat(value).isoformat()
            else:
                my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__

        return my_dict
