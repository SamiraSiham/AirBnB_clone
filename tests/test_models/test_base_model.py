import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up test methods.
        """
        self.model = BaseModel()

    def test_initialization(self):
        """
        Test that a new instance is correctly initialized.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(uuid.UUID(self.model.id), uuid.UUID)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_save_method(self):
        """
        Test that the save method updates 'updated_at'.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict_method(self):
        """
        Test that to_dict method returns the correct dictionary.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_str_method(self):
        """
        Test the __str__ method for correct string representation.
        """
        model_str = str(self.model)
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(model_str, expected_str)


if __name__ == "__main__":
    unittest.main()
