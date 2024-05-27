#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up the test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test the all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test the new method"""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], model)

    def test_save(self):
        """Test the save method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], model.id)

    def test_reload(self):
        """Test the reload method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, model.id)

class TestBaseModelStorageIntegration(unittest.TestCase):

    def setUp(self):
        """Set up the test environment"""
        self.storage = FileStorage()
        self.file_path = self.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up the test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_save_method_updates_storage(self):
        """Test that BaseModel's save method updates FileStorage"""
        model = BaseModel()
        model.save()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_new_instance_added_to_storage(self):
        """Test that a new BaseModel instance is added to FileStorage"""
        model = BaseModel()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_reload_loads_saved_model(self):
        """Test that reloading FileStorage loads saved BaseModel instance"""
        model = BaseModel()
        model.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, model.id)

if __name__ == '__main__':
    unittest.main()
