#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertIsInstance(self.model.id, str)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
