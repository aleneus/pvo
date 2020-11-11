class Body:
    def __init__(self):
        self.gens = []

    def add_generator(self, g):
        self.gens.append(g)

    def get_next_value(self):
        s = 0
        for g in self.gens:
            s += g.get_next_value()
        return s


class SignalGenerator:
    def get_next_value(self):
        raise NotImplementedError


class Stomach(SignalGenerator):
    def get_next_value(self):
        return 1


class Heart(SignalGenerator):
    def get_next_value(self):
        return 2


class Brain(SignalGenerator):
    def get_next_value(self):
        return 3


if __name__ == "__main__":
    b = Body()
    b.add_generator(Stomach())
    b.add_generator(Heart())
    b.add_generator(Brain())

    for t in range(10):
        x = b.get_next_value()
        print(x)
