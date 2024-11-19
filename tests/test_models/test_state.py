#!/usr/bin/python3
"""Module for testing State class
"""

import unittest
import os
import models
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for state class
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
        """Test case for initialization of state attributes
        """
        test = State()
        self.assertEqual(test.name, "")

    def test_user_inheritance_from_base_model(self):
        """Test case for inheritance from base model
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_user_str_attribute_representation(self):
        """Test case for string instance of state representation
        """
        test = State()
        test.name = "LA"

        test_str = str(test)
        self.assertIn("LA", test_str)

    def test_uuid(self):
        """Test case for unique identifier generation
        """
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_user_instance_conversion_to_dict(self):
        """Test case for to_dict function
        """
        test_state = State(name="LA")
        test_dict = test_state.to_dict()

        self.assertEqual(test_dict['name'], "LA")


if __name__ == "__main__":
    unittest.main()
