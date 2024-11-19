#!/usr/bin/python3
"""Module for testing City class
"""

import unittest
import os
import models
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for city class
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
        """Test case for initialization of city attributes
        """
        test = City()
        self.assertEqual(test.state_id, "")
        self.assertEqual(test.name, "")

    def test_user_inheritance_from_base_model(self):
        """Test case for inheritance from base model
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_user_str_attribute_representation(self):
        """Test case for string instance of state representation
        """
        test = City()
        test.name = "Nairobi"
        test.state_id = "47"

        test_str = str(test)
        self.assertIn("City", test_str)
        self.assertIn("Nairobi", test_str)
        self.assertIn("47", test_str)

    def test_uuid(self):
        """Test case for unique identifier generation
        """
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_user_instance_conversion_to_dict(self):
        """Test case for to_dict function
        """
        test_city = City(name="Nairobi", state_id="47")
        test_dict = test_city.to_dict()

        self.assertEqual(test_dict['name'], "Nairobi")
        self.assertEqual(test_dict['state_id'], "47")


if __name__ == "__main__":
    unittest.main()
