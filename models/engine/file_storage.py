#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file"""
from models.base_model import BaseModel
import json


class FileStorage:
    """ """
    __file_path = "file.json"
    __objects = {}

def all(self):
    """Public instance method"""
    return self.__objects

def new(self, obj):
    """sets in __objects"""
    key = "{}.{}".format(type(obj).__name__, obj.id)
    self.__objects = key

def save(self):
    """ serializes __objects to the JSON file"""
    new = {}
    for key, obj in __objects.items():
        new[key] = obj.to_dict()
    with open(__file_path, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(new))

def reload(self):
    """
    deserializes the JSON file
    if os.path.isfile(self.__file_path) is True:
    """
    obj = {}
    try:
        with open(self.__file_path, 'r', encoding='UTF-8') as f:
            obj = json.load(f)
            for key, value in obj.items():
                if class_name in self.__class__:
                    class_name = obj['__class__']
    except FileNotFoundError:
        pass
