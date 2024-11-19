#!/usr/bin/python3
"""Module for testing Review class
"""

import unittest
import os
import models
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for review class
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
        test = Review()
        self.assertEqual(test.place_id, "")
        self.assertEqual(test.user_id, "")
        self.assertEqual(test.text, "")

    def test_user_inheritance_from_base_model(self):
        """Test case for inheritance from base model
        """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_user_str_attribute_representation(self):
        """Test case for string instance of user representation
        """
        test = Review()
        test.place_id = "1004"
        test.user_id = "1057"
        test.text = "Great place."

        test_str = str(test)
        self.assertIn("1004", test_str)
        self.assertIn("1057", test_str)
        self.assertIn("Great place.", test_str)

    def test_uuid(self):
        """Test case for unique identifier generation
        """
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_user_instance_conversion_to_dict(self):
        """Test case for to_dict function
        """
        user_review = Review(
                place_id="1111",
                user_id="45",
                text="Splendid"
                )
        test_dict = user_review.to_dict()
        self.assertEqual(test_dict['place_id'], "1111")
        self.assertEqual(test_dict['user_id'], "45")
        self.assertEqual(test_dict['text'], "Splendid")


if __name__ == "__main__":
    unittest.main()
