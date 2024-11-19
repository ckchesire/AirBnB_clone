#!/usr/bin/python3
"""Module for the Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place that contains the attribute's for listed places
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = ""
