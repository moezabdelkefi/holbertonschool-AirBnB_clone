#!/usr/bin/python3
"""define a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        self.id = str(uuid.uuid4())
        # returns the current date and time
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at attribute with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary"""
        # Isoformat()function is used to return a string of date, time ..
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['class'] = type(self).__name__
        return dict_copy
