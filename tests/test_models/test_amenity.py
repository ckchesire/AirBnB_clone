#!/usr/bin/python3
"""Module for testing Amenity class
"""

import unittest
import os
import models
from models.amenity import Amenity
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for Amenity class
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
        """Test case for initialization of amenity attributes
        """
        test = Amenity()
        self.assertEqual(test.name, "")

    def test_user_inheritance_from_base_model(self):
        """Test case for inheritance from base model
        """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_user_str_attribute_representation(self):
        """Test case for string instance of state representation
        """
        test = Amenity()
        test.name = "Condominium"

        test_str = str(test)
        self.assertIn("Condominium", test_str)

    def test_uuid(self):
        """Test case for unique identifier generation
        """
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_user_instance_conversion_to_dict(self):
        """Test case for to_dict function
        """
        test_amenity = Amenity(name="Condominium")
        test_dict = test_amenity.to_dict()

        self.assertEqual(test_dict['name'], "Condominium")


if __name__ == "__main__":
    unittest.main()
