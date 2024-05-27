#!/usr/bin/python3
"""uinttest module"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBasemodel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def setUp(self):
        """Set up the test case environment"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test if the BaseModel instance is correctly created"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, str)
        self.assertIsInstance(self.model.updated_at, str)

    def test_id(self):
        """Test if each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(model2.id, self.model.id)

    def test_created_at(self):
        """Test if 'created_at' is a string in ISO format"""
        try:
            datetime.fromisoformat(self.model.created_at)
        except ValueError:
            self.fail("'created_at' is not in ISO format")

    def test_update_at(self):
        """Test if 'updated_at' is a string in ISO format"""
        try:
            datetime.fromisoformat(self.model.updated_at)
        except ValueError:
            self.fail("'updated_at' is not in ISO format")

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
        try:
            datetime.fromisoformat(self.model.updated_at)
        except ValueError:
            self.fail("'updated_at' is not in ISO format after save()")

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"], self.model.created_at)
        self.assertEqual(model_dict["updated_at"], self.model.updated_at)


if __name__ == "__main__":
    unittest.main()
