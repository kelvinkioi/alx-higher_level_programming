#!/usr/bin/python3
"""Module"""


import unittest
from models.rectangle import Rectangle

class Tests_update(unittest.TestCase):
    """Test for update on id and width"""
    def test_0(self):
        self.r1 = Rectangle(17, 22)
        self.r1.update()
        self.assertEqual(self.r1.id, 13)
        self.r1.update(89)
        self.assertEqual(self.r1.id, 89)
        self.r1.update(89, 1)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 1)

class tests_value(unittest.TestCase):
    """Test for arguments"""
    def test_0(self):
        """Test for id passed as argument in class rectangle"""
        self.r1 = Rectangle(1, 2)
        self.assertEqual(self.r1.id, 16)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 2)
        self.r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(self.r2.id, 5)

    def test_1(self):
        """Test for various values passed as arguments in Rectangle"""
        with self.assertRaises(TypeError):
            Rectangle("6", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "9")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -4)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

class test_2(unittest.TestCase):
    def test_0(self):
        self.r3 = Rectangle(6, 6)
        self.r4 = Rectangle(1, 2)
        self.assertEqual(self.r3.area(), 36)
        self.assertEqual(self.r3.__str__(), '[Rectangle] (14) 0/0 - 6/6')
        self.assertEqual(self.r4.to_dictionary(), {'id': 15, 'width': 1, 'height': 2, 'x': 0, 'y': 0})
        self.assertEqual(Rectangle.load_from_file(), [])

if __name__ == '__main__':
    unittest.main()
