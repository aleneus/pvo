import unittest


def lin(a, b):
    """Solve equation: ax + b = 0"""
    return -b / a


class TestLin(unittest.TestCase):
    def test_a_1__b_0(self):
        a = 1
        b = 0
        x = lin(a, b)
        self.assertEqual(x, 0)

    def test_a_1__b_1(self):
        a = 1
        b = 1
        x = lin(a, b)
        self.assertEqual(x, -1)

    def test_a_2__b_3(self):
        a = 2
        b = 3
        x = lin(a, b)
        self.assertEqual(x, -3/2)


unittest.main()
