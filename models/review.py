#!/usr/bin/python3
"""Module for the Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that contains details regarding user reviews
    """
    place_id = ""
    user_id = ""
    text = ""
