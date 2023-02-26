#!/usr/bin/python3
from models.base_model import BaseModel
import json
import models.user

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
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                json_objs = json.load(file)
                for k, v in json_objs.items():
                    if v['__class__'] == 'BaseModel':
                        obj = models.base_model.BaseModel(**v)
                    elif v['__class__'] == 'User':
                        obj = models.user.User(**v)
                    self.__objects[k] = obj
        except:
            pass
