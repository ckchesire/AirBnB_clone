#!/usr/bin/python3
"""Test module for the base_model module
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel
    """
    def setUP(self):
        self.my_model = BaseModel()

    def test_init(self):
        self.my_model = BaseModel()
        self.assertIsNotNone(self.my_model.id)
        self.assertIsNotNone(self.my_model.created_at)
        self.assertIsNotNone(self.my_model.updated_at)

    def test_save(self):
        self.my_model = BaseModel()
        first_updated_at = self.my_model.updated_at
        second_updated_at = self.my_model.save()

        self.assertNotEqual(first_updated_at, second_updated_at)

    def test_to_dict(self):
        self.my_model = BaseModel()
        test_model_dict = self.my_model.to_dict()

        self.assertIsInstance(test_model_dict, dict)
        self.assertEqual(test_model_dict["__class__"], 'BaseModel')
        self.assertEqual(test_model_dict['id'], self.my_model.id)
        self.assertEqual(
                test_model_dict['created_at'],
                self.my_model.created_at.isoformat())
        self.assertEqual(
                test_model_dict['updated_at'],
                self.my_model.created_at.isoformat())

    def test_str(self):
        self.my_model = BaseModel()
        self.assertTrue(str(self.my_model).startswith('[BaseModel]'))
        self.assertIn(self.my_model.id, str(self.my_model))
        self.assertIn(str(self.my_model.__dict__), str(self.my_model))


if __name__ == "__main__":
    unittest.main()
