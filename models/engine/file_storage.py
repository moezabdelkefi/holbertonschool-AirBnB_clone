#!/usr/bin/python3
from models.base_model import BaseModel
import json
import models.user
from models.state import state
from models.city import city
from models.amenity import amenity
from models.place import place
from models.review import review
from models.user import User
from os import path


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary of objects
        """
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        else:
            return self.__objects

    def new(self, obj):
        """
        Sets the object in __objects with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objects = {}
        for k, v in self.__objects.items():
            serialized_objects[k] = v.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                objects_dict = json.load(f)
            for k, v in objects_dict.items():
                class_name = k.split('.')[0]
                obj = eval(class_name)(**v)
                self.__objects[k] = obj
