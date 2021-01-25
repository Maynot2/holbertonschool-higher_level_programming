#!/usr/bin/python3

"""
    Contains test cases for Rectangle shape
"""

import unittest
from unittest.mock import patch
from io import StringIO
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

    def test_has_given_id(self):
        val = 357
        r = Rectangle(1, 2, 0, 0, val)
        self.assertEqual(r.id, val)

    def test_have_consecutive_ids_when_id_given(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(3, 4, 0, 0, 358)
        self.assertEqual(r2.id, 358)
        r3 = Rectangle(5, 6)
        self.assertEqual(r3.id, 2)

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

    def test_is_error_str_width(self):
        with self.assertRaises(TypeError) as error:
            Rectangle('1', 2, 3, 4)
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_is_error_float_width(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1.0, 2, 3, 4)
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_is_error_bool_width(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(True, 2, 3, 4)
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_is_error_complex__height(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, complex(2), 3, 4)
        self.assertEqual(str(error.exception), 'height must be an integer')

    def test_is_error_list_height(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, [2], 3, 4)
        self.assertEqual(str(error.exception), 'height must be an integer')

    def test_is_error_tuple_height(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, (2, ), 3, 4)
        self.assertEqual(str(error.exception), 'height must be an integer')

    def test_is_error_range_x(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, range(0, 3), 4)
        self.assertEqual(str(error.exception), 'x must be an integer')

    def test_is_error_byte_x(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, bytes(3), 4)
        self.assertEqual(str(error.exception), 'x must be an integer')

    def test_is_error_dict_x(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, {'three': 3, 'five': 5}, 4)
        self.assertEqual(str(error.exception), 'x must be an integer')

    def test_is_error_bytearray_y(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3, bytearray(4))
        self.assertEqual(str(error.exception), 'y must be an integer')

    def test_is_error_set_y(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3, set([4, 5]))
        self.assertEqual(str(error.exception), 'y must be an integer')

    def test_is_error_frozenset_y(self):
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 2, 3, frozenset([4, 5]))
        self.assertEqual(str(error.exception), 'y must be an integer')

    def test_is_error_negative_x(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 2, -3, 4)
        self.assertEqual(str(error.exception), 'x must be >= 0')

    def test_is_error_negative_y(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(error.exception), 'y must be >= 0')

    def test_is_error_negative_width(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(-1, 2, 3, 4)
        self.assertEqual(str(error.exception), 'width must be > 0')

    def test_is_error_null_width(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(0, 2, 3, 4)
        self.assertEqual(str(error.exception), 'width must be > 0')

    def test_is_error_negative_height(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(1, -2, 3, 4)
        self.assertEqual(str(error.exception), 'height must be > 0')

    def test_is_error_null_height(self):
        with self.assertRaises(ValueError) as error:
            Rectangle(1, 0, 3, 4)
        self.assertEqual(str(error.exception), 'height must be > 0')

    def test_computes_area_no_optional_args_1(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_computes_area_no_optional_args_2(self):
        r = Rectangle(68, 253)
        self.assertEqual(r.area(), 17204)

    def test_computes_area_optional_x(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.area(), 2)

    def test_computes_area_optional_x_y(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.area(), 2)

    def test_computes_area_optional_x_y_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.area(), 2)

    def test_display_rectangle_1x1_correctly(self):
        r = Rectangle(1, 1)
        expected_rec = '#\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_rec)

    def test_display_rectangle_4x4_correctly(self):
        r = Rectangle(4, 4)
        expected_rec = '####\n####\n####\n####\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_rec)

    def test_display_rectangle_3x2_correctly(self):
        r = Rectangle(3, 2)
        expected_rec = '###\n###\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_rec)

    def test_display_rectangle_3wX2h_1xX1y_correctly(self):
        r = Rectangle(3, 2, 1, 1)
        expected_rec = '\n ###\n ###\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_rec)

    def test_display_rectangle_3wX3h_2xX3y_correctly(self):
        r = Rectangle(3, 3, 2, 3)
        expected_rec = '\n\n\n  ###\n  ###\n  ###\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r.display()
        self.assertEqual(fake_out.getvalue(), expected_rec)

    def test_print_custom_str_representation_of_rectangele_2(self):
        r = Rectangle(4, 6)
        expected_rep = '[Rectangle] (1) 0/0 - 4/6\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_print_custom_str_representation_of_rectangele_3(self):
        r = Rectangle(4, 6, 1)
        expected_rep = '[Rectangle] (1) 1/0 - 4/6\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_print_custom_str_representation_of_rectangele_4(self):
        r = Rectangle(4, 6, 1, 1)
        expected_rep = '[Rectangle] (1) 1/1 - 4/6\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_print_custom_str_representation_of_rectangele_1(self):
        r = Rectangle(4, 6, 2, 1, 12)
        expected_rep = '[Rectangle] (12) 2/1 - 4/6\n'
        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(r)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.id, 1)
        r.update()
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_update_id_attr_1(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.id, 1)
        r.update(2)
        self.assertEqual(r.id, 2)

    def test_update_id_attr_2(self):
        r = Rectangle(10, 10, 10, 10, 12)
        self.assertEqual(r.id, 12)
        r.update(1)
        self.assertEqual(r.id, 1)

    def test_update_id_attr_3(self):
        r = Rectangle(10, 10, 10, 10, 12)
        self.assertEqual(r.id, 12)
        r.update(id=3)
        self.assertEqual(r.id, 3)

    def test_update_id_width_attrs(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.width, 10)
        r.update(2, 1)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 1)

    def test_update_id_width_height_attrs(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.height, 10)
        r.update(2, 1, 1)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)

    def test_update_id_width_height_x_attrs(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.height, 10)
        r.update(2, 1, 1, 1)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)

    def test_update_id_width_height_x_y_attrs(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.height, 10)
        r.update(2, 1, 1, 1, 1)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)

    def test_dictionary_representation_1(self):
        r = Rectangle(10, 2, 1, 9)
        dic_rep = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), dic_rep)

    def test_dictionary_representation_2(self):
        r = Rectangle(10, 2, 1, 9, 10)
        dic_rep = {'x': 1, 'y': 9, 'id': 10, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), dic_rep)

    def test_dictionary_representation_3(self):
        r = Rectangle(10, 2)
        dic_rep = {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), dic_rep)

    def test_dictionary_representation_4(self):
        r = Rectangle(10, 2, 1)
        dic_rep = {'x': 1, 'y': 0, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r.to_dictionary(), dic_rep)
