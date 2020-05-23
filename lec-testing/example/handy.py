def lin(a, b):
    """Solve equation: ax + b = 0"""
    return -b / a


def test_a_1__b_0():
    name = "test_a_1__b_0"
    a = 1
    b = 0
    x = lin(a, b)
    if x == 0:
        print(name, ": OK")
    else:
        print(name, ": FALSE: {} != 0".format(x))


def test_a_1__b_1():
    name = "test_a_1__b_1"
    a = 1
    b = 1
    x = lin(a, b)
    if x == -1:
        print(name, ": OK")
    else:
        print(name, ": FALSE: {} != -1".format(x))


def test_a_2__b_3():
    name = "test_a_2__b_3"
    a = 2
    b = 3
    x = lin(a, b)
    if abs(x - -3/2) < 0.000001:
        print(name, ": OK")
    else:
        print(name, ": FALSE: {} != -3/2".format(x))


def main():
    test_a_1__b_0()
    test_a_1__b_1()
    test_a_2__b_3()


main()
