#!/usr/bin/python3
"""Base Module test"""


import unittest
from models.base import Base


class tests_0(unittest.TestCase):
    """Test for Base class when assigning id with each call"""
    def setUp(self):
        self.base1 = Base()

    def test_0(self):
        self.assertEqual(self.base1.id, 1)

    def test_1(self):
        self.assertEqual(self.base1.id, 2)

    def test_2(self):
        self.assertEqual(self.base1.id, 3)

    def test_3(self):
        self.assertEqual(self.base1.id, 4)

    def test_4(self):
        self.assertEqual(self.base1.id, 5)

    def test_5(self):
        self.assertEqual(self.base1.id, 6)


class tests_1(unittest.TestCase):
    """Tests for assigning and id and for calling
    the json functions", ie; to json from python
    and from json to python"""
    def setUp(self):
        self.base1 = Base(66)

    def test_1(self):
        self.assertEqual(self.base1.id, 66)

    def test_2(self):
        self.assertEqual(Base().to_json_string(None), '[]')

    def test_3(self):
        self.assertEqual(Base().to_json_string([]), '[]')

    def test_4(self):
        self.assertEqual(Base().to_json_string([{'id': 7}]), '[{"id": 7}]')

    def test_5(self):
        self.assertEqual(Base().from_json_string(None), [])

    def test_6(self):
        self.assertEqual(Base().from_json_string("[]"), [])

    def test_7(self):
        self.assertEqual(Base().from_json_string('[{"id": 77}]'), [{'id': 77}])


if __name__ == '__main__':
    unittest.main()
