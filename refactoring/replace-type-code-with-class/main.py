"""Example of Replace Type Code with Class"""


class Quant:
    def __init__(self, code, units):
        self.__code = code
        self.__units = units

    def get_code(self):
        return self.__code

    def get_units(self):
        return self.__units

    def equals(self, another):
        return self.__code == another.get_code()


class Sample:
    """Sample of data"""
    def __init__(self, quant, value):
        self.__quant = quant  # initially here was just a numeric code
        self.__value = value

    def get_quant(self):
        return self.__quant

    def get_value(self):
        return self.__value

    def __repr__(self):
        return "{} {}".format(self.get_value(), self.get_quant().get_units())


class Guard:
    """Check if sample is appropriate."""
    def __init__(self, quant):
        self.__quant = quant

    def __call__(self, sample):
        return self.__quant.equals(sample.get_quant())


QUANT_U = Quant(0, "Volts")
QUANT_I = Quant(1, "Ampers")
QUANT_P = Quant(1, "Watts")


def main():
    """Create some samples, represent them in text form, and pass
    through guard."""

    samples = [
        Sample(QUANT_U, 15),
        Sample(QUANT_U, 14),
        Sample(QUANT_P, 13),
        Sample(QUANT_I, 12),
    ]

    guard = Guard(QUANT_U)

    for sample in samples:
        print(sample, end=" ")
        print("pass" if guard(sample) else "")


if __name__ == "__main__":
    main()
