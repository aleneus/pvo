"""Observer example."""
import unittest


class Observer:
    """Base class for observers."""
    def update(self, val):
        """Update value."""
        raise NotImplementedError


class A:
    def __init__(self):
        self.__val = None
        self.__views = []

    def set_val(self, val):
        self.__val = val
        self.__update_views()

    def __update_views(self):
        for view in self.__views:
            view.update(self.__val)

    def register(self, view):
        self.__views.append(view)


class B(Observer):
    def __init__(self, viewed):
        self.__viewed = viewed
        self.__viewed.register(self)
        self.__val = None

    def update(self, val):
        self.__val = val

    def get_val(self):
        """Return value."""
        return self.__val


class TestObserver(unittest.TestCase):
    def test_single(self):
        a = A()
        b = B(a)
        a.set_val(10)
        self.assertEqual(b.get_val(), 10)

    def test_many(self):
        a = A()
        b1 = B(a)
        b2 = B(a)
        a.set_val(10)
        self.assertEqual(b1.get_val(), 10)
        self.assertEqual(b2.get_val(), 10)


unittest.main()
