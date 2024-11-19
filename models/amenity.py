#!/usr/bin/python3
"""Module for the Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity that contains an amenitie's name
    """
    name = ""
