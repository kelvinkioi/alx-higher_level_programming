#!/usr/bin/python3
"""Test nodule for square class"""


import unittest
from models.square import Square


class tests_1(unittest.TestCase):
    def test_0(self):
        self.s1 = Square(24, 16)
        self.s1.update()
        self.assertEqual(self.s1.id, 17)
        self.s1.update(89)
        self.assertEqual(self.s1.id, 89)
        self.s1.update(89, 2)
        self.assertEqual(self.s1.id, 89)
        self.assertEqual(self.s1.size, 2)

    def test_1(self):
        self.s2 = Square(8)
        self.assertEqual(self.s2.id, 18)
        self.assertEqual(self.s2.size, 8)
        self.s3 = Square(1, 2)
        self.assertEqual(self.s3.id, 19)
        self.s4 = Square(1, 2, 3)
        self.assertEqual(self.s4.id, 20)
        self.s4 = Square(1, 2, 3, 4)
        self.assertEqual(self.s4.id, 4)
        with self.assertRaises(TypeError):
            Square("9")
        with self.assertRaises(TypeError):
            Square(1, "3")
        with self.assertRaises(TypeError):
            Square(1, 2, "8")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -7)
        with self.assertRaises(ValueError):
            Square(0)
        self.s5 = Square(2)
        self.assertEqual(self.s5.__str__(), '[Square] (21) 0/0 - 2')
        self.assertEqual(self.s5.to_dictionary(), {'id': 21, 'size': 2, 'x': 0, 'y': 0})


class tests_2(unittest.TestCase):
    def test_0(self):
        self.s6 = Square.create(**{'id': 89, 'size': 2})
        self.assertEqual(self.s6.size, 2)
        self.assertEqual(self.s6.id, 89)


class tests_3(unittest.TestCase):
    def test_0(self):
        self.s = Square(3)
        self.assertEqual(Square.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
