#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class contains unit tests for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of BaseModel instances.

        Checks if the id, created_at, and updated_at attributes are initialized correctly.
        """

        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        """
        Test the save method of BaseModel instances.

        Checks if the updated_at attribute is updated after calling the save method.
        """

        model = BaseModel()
        
        init_updatedat = model.updated_at
        current = model.save()

        self.assertNotEqual(init_updatedat, current)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel instances.

        Checks if the to_dict method returns the expected dictionary representation of the instance.
        """

        model = BaseModel()

        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict) 
        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_str(self):
        """
        Test the string representation (__str__) method of BaseModel instances.

        Checks if the string representation of the instance contains the class name, id, and attributes.
        """

        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))

if __name__ == '__main__':
    unittest.main()
