#!/usr/bin/python3
""" defeine a classe that inherit from BaseModel"""


from base_model import BaseModel


class review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
