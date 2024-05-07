#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        copy_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                copy_dict[key] = value.isoformat()
            else:
                copy_dict[key] = value
        copy_dict["__class__"] = self.__class__.__name__
        return copy_dict
