#!/usr/bin/python3

"""
    Contains test cases for Rectangle shape
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
        Tests for Rectangle shape
    """

    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_inherit_from_base(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Base)

    def test_is_rectangle(self):
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    def test_has_id(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)

    def test_have_consecutive_ids(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 4)
        self.assertEqual(r2.id, 2)

    def test_have_consecutive_ids_when_id_given(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 4, 0, 0, 358)
        self.assertEqual(r2.id, 358)
        r3 = Rectangle(5, 6)
        self.assertEqual(r3.id, 2)

    def test_has_given_id(self):
        val = 357
        r = Rectangle(1, 2, 0, 0, val)
        self.assertEqual(r.id, val)

    def test_raises_error_if_no_height(self):
        self.assertRaises(TypeError, Rectangle.__init__, 1)

    def test_raises_error_if_no_width(self):
        self.assertRaises(TypeError, Rectangle.__init__)

    def test_has_given_width(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_has_given_height(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    def test_x_defaults_to_0(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.x, 0)

    def test_y_defaults_to_0(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.y, 0)

    def test_has_given_x(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)

    def test_has_given_y(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)
