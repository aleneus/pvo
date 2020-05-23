"""Testing module."""

import unittest
from passwd import Passwd
from stub_data_driver import StubDataDriver


class TestPasswd(unittest.TestCase):
    def test_wrong_data_structure(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("xxx")

        try:
            Passwd(name="test.txt", driver=d)
        except RuntimeError:
            self.assertTrue(True)
            return

        self.assertTrue(False)

    def test_add_new_user(self):
        d = StubDataDriver()
        d.set_file_exists(False)

        p = Passwd(name="test.txt", driver=d)
        p.add_user("admin", "admin")
        p.commit()

        self.assertEqual(d.get_text(), "admin;admin\n")

    def test_user_exists(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("a;a\nb;b\nc;c\n")

        p = Passwd(name="test.txt", driver=d)
        self.assertTrue(p.user_exists("b"))
        self.assertFalse(p.user_exists("d"))

    def test_add_existing_user(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("a;a\nb;b\nc;c\n")

        p = Passwd(name="test.txt", driver=d)
        try:
            p.add_user("c", "c")
        except RuntimeError:
            self.assertEqual(True, True)
            return

        self.assertEqual(True, False)

    def test_check_user(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("a;a\nb;b\nc;c\n")

        p = Passwd(name="test.txt", driver=d)
        self.assertTrue(p.check_user("a", "a"))
        self.assertFalse(p.check_user("a", "b"))

    def test_remove_existing_user(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("a;a\nb;b\nc;c\n")

        p = Passwd(name="test.txt", driver=d)
        p.remove_user("b", "b")
        p.commit()
        self.assertEqual(d.get_text(), "a;a\nc;c\n")

    def test_remove_unexisting_user(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("a;a\nb;b\nc;c\n")

        p = Passwd(name="test.txt", driver=d)
        try:
            p.remove_user("d", "d")
        except RuntimeError:
            self.assertEqual(True, True)
            return

        self.assertEqual(True, False)

    def test_remove_existing_user_wrong_passwd(self):
        d = StubDataDriver()
        d.set_file_exists(True)
        d.set_text("a;a\nb;b\nc;c\n")

        p = Passwd(name="test.txt", driver=d)
        try:
            p.remove_user("b", "d")
        except RuntimeError:
            self.assertEqual(True, True)
            return

        self.assertEqual(True, False)


if __name__ == "__main__":
    unittest.main()
