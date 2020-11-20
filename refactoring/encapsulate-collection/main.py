class Train:
    """Train. Consists loco and a number of wagons."""
    def __init__(self):
        self.__wagons = []

    def add_wagon(self, wagon):
        """Add wagon to train."""
        self.__wagons.append(wagon)

    def del_wagon(self, wagon):
        """Remove wagon from train."""
        self.__wagons.remove(wagon)

    def get_wagons(self):
        """Get all wagons from the train"""

        # NOTE: prohibit changing a collection outside of this class
        return self.__wagons.copy()

    def __repr__(self):
        loco = "/oooTT--"

        wags = ""
        for wagon in self.__wagons:
            wags += "{}-".format(wagon)

        return loco + wags


class Wagon:
    """Wagon."""
    def __init__(self, ID):
        self.__id = ID

    def __repr__(self):
        return "[{}___]".format(self.__id)


def main():
    """Create train and add wagons. Then get collection from train and
    show that changes on it has no effect for train."""

    t = Train()
    w1 = Wagon(1)
    w2 = Wagon(2)
    t.add_wagon(w1)
    t.add_wagon(w2)
    print("t:", t)

    print()
    ws = t.get_wagons()
    ws.append(Wagon(3))
    print("ws:", ws)
    print("t:", t)


if __name__ == "__main__":
    main()
