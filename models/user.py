#!/usr/bin/python3
"""Module for the User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that contains user's attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
