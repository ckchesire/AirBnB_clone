#!/usr/bin/python3
"""Module to test FileStorage class and its integration with BaseModel"""
import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test cases"""
        self.test_file = "test_file.json"
        if os.path.exists("file.json"):
            os.rename("file.json", "temp_file.json")
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.test_file
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up variables after tests"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        if os.path.exists("temp_file.json"):
            os.rename("temp_file.json", "file.json")

    def test_all_empty(self):
        """Test all() method with empty storage"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test new() method"""
        model = BaseModel()
        self.storage.new(model)
        key = f"BaseModel.{model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], model)

    def test_save_and_reload(self):
        """Test save() and reload() methods"""
        model = BaseModel()
        model.name = "Test Model"
        model.my_number = 42
        self.storage.new(model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.test_file
        new_storage.reload()

        key = f"BaseModel.{model.id}"
        self.assertIn(key, new_storage.all())
        reloaded_model = new_storage.all()[key]

        self.assertEqual(reloaded_model.id, model.id)
        self.assertEqual(reloaded_model.name, model.name)
        self.assertEqual(reloaded_model.my_number, model.my_number)
        self.assertEqual(reloaded_model.created_at, model.created_at)
        self.assertEqual(reloaded_model.updated_at, model.updated_at)

    def test_save_file_content(self):
        """Test the content of the saved JSON file"""
        model = BaseModel()
        model.name = "Test Model"
        self.storage.new(model)
        self.storage.save()

        with open(self.test_file, 'r') as f:
            content = json.load(f)

        key = f"BaseModel.{model.id}"
        self.assertIn(key, content)
        self.assertEqual(content[key]['name'], "Test Model")
        self.assertEqual(content[key]['__class__'], "BaseModel")

    def test_reload_nonexistent_file(self):
        """Test reload() with nonexistent file"""
        # Ensure file doesn't exist
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"reload() raised {type(e)} unexpectedly!")

    def test_reload_with_invalid_json(self):
        """Test reload() with invalid JSON content"""
        with open(self.test_file, 'w') as f:
            f.write("Invalid JSON content")

        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    def test_storage_var_created(self):
        """Test storage variable is created and initialized"""
        self.assertIsInstance(storage, FileStorage)

    def test_storage_var_reload(self):
        """Test storage variable loads data correctly"""
        model = BaseModel()
        model.save()
        storage.reload()
        key = f"BaseModel.{model.id}"
        self.assertIn(key, storage.all())


class TestBaseModelFileStorageIntegration(unittest.TestCase):
    """Test integration between BaseModel and FileStorage"""

    def setUp(self):
        """Set up test cases"""
        if os.path.exists("file.json"):
            os.rename("file.json", "temp_file.json")
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("temp_file.json"):
            os.rename("temp_file.json", "file.json")

    def test_save_method_creates_file(self):
        """Test that save() creates a file"""
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_new_instance_in_storage(self):
        """Test that new instances are added to storage"""
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, storage.all())

    def test_storage_file_closing(self):
        """Test proper file handling (opening/closing)"""
        self.model.save()
        with open("file.json", 'r') as f:
            content = f.read()
        self.assertIsInstance(content, str)


if __name__ == '__main__':
    unittest.main()
