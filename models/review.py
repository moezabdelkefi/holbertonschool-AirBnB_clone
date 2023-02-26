#!/usr/bin/python3
""" defeine a classe that inherit from BaseModel"""


from base_model import BaseModel


class review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes Place instance
        """
        super().__init__(*args, **kwargs)
