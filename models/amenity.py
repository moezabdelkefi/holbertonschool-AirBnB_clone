#!/usr/bin/python3
""" defeiene a classe that inherit from BaseModel"""


from base_model import BaseModel


class amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Place instance
        """
        super().__init__(*args, **kwargs)
