#!/usr/bin/python3

"""
    Contains test cases for Basic shape
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
        Tests for Basic shape instances and class
    """

    def setUp(self):
        setattr(Base, '_Base__nb_objects', 0)

    def test_is_instance_of_base(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_has_given_id(self):
        val = 356
        b = Base(val)
        self.assertEqual(b.id, val)

    def test_is_generated_id_when_no_arg_is_passed(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_are_generated_ids_in_consecutive_order(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_instance_with_passed_arg_dont_affect_id_attribution(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
