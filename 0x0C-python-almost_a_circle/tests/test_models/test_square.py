#!/usr/bin/python3

"""
    Contains test cases for Square objects
"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        Tests for Square objects
    """

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_inherit_from_base(self):
        sqr = Square(1)
        self.assertIsInstance(sqr, Base)

    def test_inherit_from_rectangle(self):
        sqr = Square(1)
        self.assertIsInstance(sqr, Rectangle)

    def test_is_square(self):
        sqr = Square(1)
        self.assertIsInstance(sqr, Square)

    def test_display_square_3s_1xX1y_correctly(self):
        sqr = Square(3, 1, 1)
        expected_sqr = '\n ###\n ###\n ###\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sqr.display()
        self.assertEqual(fake_out.getvalue(), expected_sqr)

    def test_print_custom_str_representation_of_square_1(self):
        sqr = Square(4)
        expected_rep = '[Square] (1) 0/0 - 4\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(sqr)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_print_custom_str_representation_of_square_2(self):
        sqr = Square(4, 1, 1)
        expected_rep = '[Square] (1) 1/1 - 4\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(sqr)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_print_custom_str_representation_of_square_3(self):
        sqr = Square(4, 1, 1, 12)
        expected_rep = '[Square] (12) 1/1 - 4\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(sqr)
        self.assertEqual(fake_out.getvalue(), expected_rep)

    def test_get_size(self):
        sqr = Square(1)
        self.assertEqual(sqr.size, 1)

    def test_set_size(self):
        sqr = Square(1)
        sqr.size = 2
        self.assertEqual(sqr.size, 2)

    def test_set_invalid_null_int_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(ValueError) as error:
            sqr.size = 0
        self.assertEqual(str(error.exception), 'width must be > 0')

    def test_set_invalid_negative_int_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(ValueError) as error:
            sqr.size = -1
        self.assertEqual(str(error.exception), 'width must be > 0')

    def test_set_invalid_null_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = None
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_set_invalid_size_str_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = '2'
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_set_invalid_size_float_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = 2.0
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_set_invalid_size_list_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = [2, 3]
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_set_invalid_size_tuple_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = (2, )
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_set_invalid_size_set_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = set([2, 3])
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_set_invalid_size_range_type_raises_error(self):
        sqr = Square(1)
        with self.assertRaises(TypeError) as error:
            sqr.size = range(2, 3)
        self.assertEqual(str(error.exception), 'width must be an integer')

    def test_update_square_no_args(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)
        sqr.update()
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)

    def test_update_square_id_attr_via_args_1(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        sqr.update(2)
        self.assertEqual(sqr.id, 2)

    def test_update_square_id_attr_via_args_2(self):
        sqr = Square(10, 10, 10, 10)
        self.assertEqual(sqr.id, 10)
        sqr.update(2)
        self.assertEqual(sqr.id, 2)

    def test_update_square_id_attr_via_kargs_1(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        sqr.update(id=2)
        self.assertEqual(sqr.id, 2)

    def test_update_square_id_attr_via_kargs_2(self):
        sqr = Square(10, 10, 10, 10)
        self.assertEqual(sqr.id, 10)
        sqr.update(id=2)
        self.assertEqual(sqr.id, 2)

    def test_update_square_id_width_attrs_via_args(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        sqr.update(2, 3)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)

    def test_update_square_id_width_attrs_via_kargs_1(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        sqr.update(id=2, size=3)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)

    def test_update_square_id_width_attrs_via_kargs_2(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        sqr.update(size=3, id=2)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)

    def test_update_square_id_width_x_attrs_via_args(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        sqr.update(2, 3, 4)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)

    def test_update_square_id_width_x_attrs_via_kargs_1(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        sqr.update(id=2, size=3, x=4)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)

    def test_update_square_id_width_x_attrs_via_kargs_2(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        sqr.update(id=2, x=4, size=3)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)

    def test_update_square_id_width_x_y_attrs_via_args(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)
        sqr.update(2, 3, 4, 5)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 5)

    def test_update_square_id_width_x_y_attrs_via_kargs_1(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)
        sqr.update(id=2, size=3, x=4, y=5)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 5)

    def test_update_square_id_width_x_y_attrs_via_kargs_2(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)
        sqr.update(size=3, id=2, y=5, x=4)
        self.assertEqual(sqr.id, 2)
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 5)

    def test_update_square_id_width_x_y_extra_attrs_via_kargs(self):
        sqr = Square(10, 10, 10)
        sqr.update(size=3, id=2, y=5, x=4, z =12)
        with self.assertRaises(AttributeError) as error:
            sqr.z, 12
        self.assertEqual(str(error.exception),
                         "'Square' object has no attribute 'z'")

    def test_update_square_id_width_x_y_attrs_via_args_if_kargs(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)
        sqr.update(12, 13, 14, 15, size=3, id=2, y=5, x=4)
        self.assertEqual(sqr.id, 12)
        self.assertEqual(sqr.size, 13)
        self.assertEqual(sqr.x, 14)
        self.assertEqual(sqr.y, 15)

    def test_update_square_id_width_x_y_attrs_via_args_if_kargs(self):
        sqr = Square(10, 10, 10)
        self.assertEqual(sqr.id, 1)
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)
        sqr.update(12, 13, 14, 15, size=3, id=2, y=5, x=4)
        self.assertEqual(sqr.id, 12)
        self.assertEqual(sqr.size, 13)
        self.assertEqual(sqr.x, 14)
        self.assertEqual(sqr.y, 15)

    def test_dictionary_representation_square_1(self):
        sqr = Square(10, 2, 1)
        dic_rep = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(sqr.to_dictionary(), dic_rep)

    def test_dictionary_representation_square_2(self):
        sqr = Square(10, 2, 1, 9)
        dic_rep = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertEqual(sqr.to_dictionary(), dic_rep)

    def test_dictionary_representation_square_3(self):
        sqr = Square(10, 2)
        dic_rep = {'x': 2, 'y': 0, 'id': 1, 'size': 10}
        self.assertEqual(sqr.to_dictionary(), dic_rep)

    def test_dictionary_representation_square_4(self):
        sqr = Square(10)
        dic_rep = {'x': 0, 'y': 0, 'id': 1, 'size': 10}
        self.assertEqual(sqr.to_dictionary(), dic_rep)

if __name__ == '__main__':
    unittest.main()
