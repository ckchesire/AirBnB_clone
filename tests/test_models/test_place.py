#!/usr/bin/python3
"""Module for testing Place class
"""

import unittest
import os
import models
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for place class
    """
    def setUp(self):
        self.test_file = "test_file.json"

        if os.path.exists("file.json"):
            os.rename("file.json", "temp_file.json")

        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """Method to destroy test case objects
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        if os.path.exists("temp_file.json"):
            os.rename("temp_file.json", "file.json")

    def test_user_attributes(self):
        """Test case for initialization of place attributes
        """
        test = Place()
        self.assertEqual(test.city_id, "")
        self.assertEqual(test.user_id, "")
        self.assertEqual(test.name, "")
        self.assertEqual(test.description, "")
        self.assertEqual(test.number_rooms, 0)
        self.assertEqual(test.number_bathrooms, 0)
        self.assertEqual(test.max_guest, 0)
        self.assertEqual(test.price_by_night, 0)
        self.assertEqual(test.latitude, 0.0)
        self.assertEqual(test.longitude, 0.0)
        self.assertEqual(test.amenity_ids, "")

    def test_user_inheritance_from_base_model(self):
        """Test case for inheritance from base model
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_user_str_attribute_representation(self):
        """Test case for string instance of place representation
        """
        test = Place()

        test.city_id = "047"
        test.user_id = "10057"
        test.name = "Nairobi"
        test.description = "Penthouse"
        test.number_rooms = 10
        test.number_bathrooms = 8
        test.max_guest = 10
        test.latitude = -1.2921
        test.longitude = 36.8219
        test.amenity_ids = "DV001 DV003"

        test_str = str(test)

        self.assertIn("Place", test_str)
        self.assertIn("047", test_str)
        self.assertIn("10057", test_str)
        self.assertIn("Nairobi", test_str)
        self.assertIn("10", test_str)
        self.assertIn("8", test_str)
        self.assertIn("10", test_str)
        self.assertIn("-1.2921", test_str)
        self.assertIn("36.8219", test_str)
        self.assertIn("DV001 DV003", test_str)

    def test_uuid(self):
        """Test case for unique identifier generation
        """
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_user_instance_conversion_to_dict(self):
        """Test case for to_dict function
        """
        listing = Place(
                city_id="047",
                user_id="10057",
                name="Nairobi",
                description="Penthouse",
                number_rooms=10,
                number_bathrooms=8,
                max_guest=10,
                latitude=-1.2921,
                longitude=36.8219,
                amenity_ids="DV001 DV003"
                )
        test_dict = listing.to_dict()
        self.assertEqual(test_dict['city_id'], "047")
        self.assertEqual(test_dict['user_id'], "10057")
        self.assertEqual(test_dict['name'], "Nairobi")
        self.assertEqual(test_dict['description'], "Penthouse")
        self.assertEqual(test_dict['number_rooms'], 10)
        self.assertEqual(test_dict['number_bathrooms'], 8)
        self.assertEqual(test_dict['max_guest'], 10)
        self.assertEqual(test_dict['latitude'], -1.2921)
        self.assertEqual(test_dict['longitude'], 36.8219)
        self.assertEqual(test_dict['amenity_ids'], "DV001 DV003")


if __name__ == "__main__":
    unittest.main()
