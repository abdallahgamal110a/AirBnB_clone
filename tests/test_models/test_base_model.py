#!/usr/bin/python3
"""uinttest module"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up the test case environment"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if the BaseModel instance is correctly created"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_id_uniqueness(self):
        """Test if each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_type(self):
        """Test if 'created_at' is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_type(self):
        """Test if 'updated_at' is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method"""
        str_rep = str(self.model)
        self.assertIn("[BaseModel]", str_rep)
        self.assertIn(self.model.id, str_rep)
        self.assertIn("created_at", str_rep)
        self.assertIn("updated_at", str_rep)

    def test_save_method(self):
        """Test the save method updates 'updated_at'"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_instance_from_dict(self):
        """Test creating an instance from a dictionary"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertEqual(self.model.__class__.__name__, new_model.__class__.__name__)

if __name__ == '__main__':
    unittest.main()

