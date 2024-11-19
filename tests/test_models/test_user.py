#!/usr/bin/python3
"""Module for testing User class
"""

import unittest
import os
import models
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for user class
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
        """Test case for initialization of user attributes
        """
        test = User()
        self.assertEqual(test.email, "")
        self.assertEqual(test.password, "")
        self.assertEqual(test.first_name, "")
        self.assertEqual(test.last_name, "")

    def test_user_inheritance_from_base_model(self):
        """Test case for inheritance from base model
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str_attribute_representation(self):
        """Test case for string instance of user representation
        """
        test = User()
        test.email = "JohnyCage@airbnb.com"
        test.first_name = "Johny"
        test.last_name = "Cage"
        test.password = "password45"

        test_str = str(test)
        self.assertIn("User", test_str)
        self.assertIn("JohnyCage@airbnb.com", test_str)
        self.assertIn("Johny", test_str)
        self.assertIn("Cage", test_str)

    def test_uuid(self):
        """Test case for unique identifier generation
        """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_instance_conversion_to_dict(self):
        """Test case for to_dict function
        """
        user_test = User(
                email="admin@airbnb.com",
                password="password45",
                first_name="Brian",
                last_name="Chesky"
                )
        test_dict = user_test.to_dict()
        self.assertEqual(test_dict['email'], "admin@airbnb.com")
        self.assertEqual(test_dict['password'], "password45")
        self.assertEqual(test_dict['first_name'], "Brian")
        self.assertEqual(test_dict['last_name'], "Chesky")


if __name__ == "__main__":
    unittest.main()
