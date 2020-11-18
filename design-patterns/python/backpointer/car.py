"""Back pointer example (whole-part)."""


class Car:
    """Car."""
    def __init__(self, num):
        self.__wheels = set()
        self.__num = num

    def add_wheel(self, whl):
        self.__wheels.add(whl)
        whl.set_car(self)

    def __repr__(self):
        s = "[{}]".format(self.__num)
        for w in self.__wheels:
            s += w.__repr__()
        return s


class Wheel:
    """Wheel of car."""
    def __init__(self, num):
        self.__num = num
        self.__car = None

    def set_car(self, car):
        self.__car = car

    def car(self):
        return self.__car

    def __repr__(self):
        return "({})".format(self.__num)


def main():
    """Entry point."""
    c = Car("xx567y")
    ws = [Wheel(1), Wheel(2), Wheel(3), Wheel(4)]
    for w in ws:
        c.add_wheel(w)

    for w in ws:
        print("wheel {} from car {}".format(w, w.car()))


if __name__ == "__main__":
    main()
