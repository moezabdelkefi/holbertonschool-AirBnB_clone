#!/usr/bin/python3
from models.base_model import BaseModel
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to
    instances
    """
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel}

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        if cls is not None:
            if isinstance(cls, str):
                cls = self.classes.get(cls, None)
            if cls is None:
                return {}
            return {k: v for k, v in self.__objects.items() if type(v) == cls}
        else:
            return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
