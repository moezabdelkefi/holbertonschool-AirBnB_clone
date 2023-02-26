#!/usr/bin/python3
"""define a class BaseModel"""
import models
import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """this is the main Module"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    # Convert datetime string to datetime object
                    # sets the value of an attribute on an object.
                    # It takes three arguments name, value,object
                    # strptime parse a string representing a datetime into
                    # a datetime.datetime object
                    #  used to convert datetime strings passed in as arguments
                    # to the __init__ method (if any) into datetime.
                    # datetime objects.
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            create = kwargs['created_at']
            update = kwargs['updated_at']
            self.created_at = datetime.datetime.strptime(create, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(update, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary"""
        # Isoformat()function is used to return a string of date, time ..
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
