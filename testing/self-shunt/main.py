"""Self-shunt testing pattern."""

import unittest


class Model:
    def __init__(self, db):
        self.__db = db

    def add(self, data):
        self.__db.add(data)


class TestModel(unittest.TestCase):
    def setUp(self):
        self.__records = []

    def add(self, data):
        self.__records.append(data)

    def test_create(self):
        Model(self)
        self.assertEqual(len(self.__records), 0)

    def test_add(self):
        model = Model(self)
        model.add("record")
        self.assertEqual(len(self.__records), 1)


unittest.main()
