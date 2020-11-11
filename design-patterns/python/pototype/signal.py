"""Prototype"""
import copy


class Signal:
    def __init__(self):
        print("Very long-time method...")
        self.x = [1, 2, 1, 2, 1]

    def represent(self):
        print(self.x)

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    s1 = Signal()
    s2 = s1.clone()

    s1.represent()
    s2.x = [1, 3, 1, 3, 1]
    s2.represent()
