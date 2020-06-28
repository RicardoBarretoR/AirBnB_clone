#!/usr/bin/python3
"""a class that defines all common attributes/methods for other classes"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """class base"""
    def __init__(self, *args, **kwargs):
        """"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a srting representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        newdict = dict(self.__dict__)
        newdict["__class__"] = self.__class__.__name__
        newdict["created_at"] = datetime.isoformat(newdict["created_at"])
        newdict["updated_at"] = datetime.isoformat(newdict["updated_at"])
        return newdict
