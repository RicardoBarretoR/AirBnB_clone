#!/usr/bin/python3
"""class FileStorage that serializes instances to a JSON file"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serialization-deserialization """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets objects in dictionary with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new = {}
        filename = FileStorage.__file_path
        for key, obj in FileStorage.__objects.items():
            new[key] = obj.to_dict()
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(new))

    def reload(self):
        """deserializes the JSON file to __objects"""
        obj = {}
        filename = FileStorage.__file_path
        try:
            with open(filename, "r", encoding='UTF-8') as f:
                obj = json.load(f)
                for key, value in obj.items():
                    FileStorage.__objects[key] = eval(
                                                value["__class__"])(**value)
        except FileNotFoundError:
            pass
