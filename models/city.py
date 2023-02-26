#!/usr/bin/python3
""" defeine a classe that inherit from BaseModel"""


from base_model import BaseModel


class city(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Place instance
        """
        super().__init__(*args, **kwargs)
