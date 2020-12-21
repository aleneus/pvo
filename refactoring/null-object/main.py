"""Introduce Null Object example."""
import random


class C:
    def is_none(self):
        return False

    # REF
    def method(self):
        return "not None"
    #


# REF
class NoneC:
    def is_none(self):
        return True

    def method(self):
        """Overloaded method."""
        return "None"
#


def get_c():
    # REF
    if random.randint(0, 3) == 1:
        return NoneC()
    return C()
    # if random.randint(0, 3) == 1:
    #     return None
    # return C()


def f(c):
    # REF
    print("c is ", c.method())
    # if c.is_none():
    #     print("c is None")
    # else:
    #     print("c is not None")


def main():
    for _ in range(10):
        f(get_c())


if __name__ == "__main__":
    main()
