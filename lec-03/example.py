"""Classes example."""


MALE = False
FEMALE = True


class Person:
    """Person represents the person."""
    def __init__(self, sex, name=None):
        self.set_sex(sex)
        self.name = name

    def set_sex(self, sex):
        """Sets the sex of person."""
        if sex not in [MALE, FEMALE]:
            raise ValueError("Unknown sex")

        self.sex = sex

    def __repr__(self):
        name = self.__repr_name()
        sex = self.__repr_sex()

        s = "{} ({})".format(name, sex)
        return s

    def __repr_name(self):
        if not self.name:
            return "Somebody"
        return self.name

    def __repr_sex(self):
        sex = "M" if self.sex == MALE else "F"
        return sex


class Doctor(Person):
    """Doctor represents the doctor."""
    def __init__(self, sex, name):
        super().__init__(sex, name)
        self._spec = None

    def set_spec(self, spec):
        """Sets speciality."""
        self._spec = spec

    def get_spec(self):
        """Returns the speciality."""
        return self._spec

    spec = property(get_spec, set_spec, "Speciality")


class Patient(Person):
    """Patient represents the patient."""
    pass


def example_1():
    p1 = Person(MALE, "Ivan")
    print(p1)
    p2 = Person(FEMALE, "Alina")
    print(p2)


def example_2():
    d = Doctor(MALE, "Alex")
    print(d)
    p = Patient(FEMALE, "Nina")
    print(p)


def example_3():
    d = Doctor(MALE, "Alex")
    d.spec = "Surgeon"
    print(d.spec)


def main():
    """Entry point."""
    run("two persons", example_1)
    run("doctor and patient are persons", example_2)
    run("spec property", example_3)


def run(name, func):
    """Runs example (decorator)."""
    print("==== {} ====".format(name))
    func()
    print()


main()

# TODO: treatment task
# TODO: call method
