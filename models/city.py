#!/usr/bin/python3
"""Module for the City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that contains details about a city
    """
    state_id = ""
    name = ""
