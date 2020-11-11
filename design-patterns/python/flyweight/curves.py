"""Flyweight example."""


class CurveFactory:
    def __init__(self):
        self.curves = {}

    def get_curve(self, curve_id):
        if curve_id in self.curves.keys():
            return self.curves[curve_id]
        else:
            new_curve = Curve()
            self.curves[curve_id] = new_curve
            return new_curve

    def curves_number(self):
        return len(self.curves)


class Curve:
    def __init__(self):
        self.x = None
        self.y = None

    def set_data(self, x, y):
        self.x = x
        self.y = y


class CurveSettings:
    def __init__(self):
        self.color = None


class Plot:
    def __init__(self):
        self.curve = None
        self.curve_settings = CurveSettings()

    def set_curve(self, curve):
        self.curve = curve

    def show(self):
        print(self.curve.x)
        print(self.curve.y)
        print(self.curve_settings.color)


def process(x, y):
    new_y = [v**2 for v in y]
    return x, new_y


def main():
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 1, 2, 1]

    cf = CurveFactory()
    curve = cf.get_curve("source")
    curve.set_data(x, y)
    plot1 = Plot()
    plot1.set_curve(curve)
    plot1.curve_settings.color = "blue"
    plot1.show()

    # ...... and somewere
    c = cf.get_curve("source")
    plot2 = Plot()
    plot2.set_curve(c)
    plot2.curve_settings.color = "red"
    plot2.show()

    print()
    x, y = process(x, y)
    curve.set_data(x, y)
    plot1.show()
    plot2.show()


if __name__ == "__main__":
    main()
