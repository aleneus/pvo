"""Python classes introduction."""

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

        self._sex = sex

    def get_sex(self):
        """Returns sex."""
        return self._sex

    sex = property(get_sex, set_sex, "Sex of person.")

    def __repr__(self):
        name = self.__repr_name()
        sex = self.__repr_sex()
        return "{} ({})".format(name, sex)

    def __repr_name(self):
        if not self.name:
            return "Somebody"
        return self.name

    def __repr_sex(self):
        return "M" if self.sex == MALE else "F"


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
    def __init__(self, sex, name=None, health=100):
        super().__init__(sex, name)
        self._health = health

    def get_health(self):
        """Returns health value."""
        return self._health

    def set_healph(self, value):
        """Sets health value for the patient."""
        if value > 100:
            self._health = 100
        else:
            self._health = value

    health = property(get_health, set_healph, "Health value")


class Treatment:
    """Treatment represents the act of treatment."""
    def __init__(self, strength=1):
        self.strength = strength

    def __call__(self, patient):
        patient.health = patient.health + self.strength


def run(func):
    """Run example decorator."""
    print("Example: {}".format(func.__doc__))
    func()
    print()


def ex_two_persons():
    """Two persons"""
    p1 = Person(MALE, "Ivan")
    print(p1)
    p2 = Person(FEMALE, "Alina")
    print(p2)


def ex_inheritance():
    """Doctor and patient are persons"""
    d = Doctor(MALE, "Alex")
    print(d)
    p = Patient(FEMALE, "Nina")
    print(p)


def ex_property():
    """Property"""
    d = Doctor(MALE, "Peter")
    d.spec = "Surgeon"
    print(d.spec)


def ex_callable():
    """Callable object"""
    p = Patient(MALE, "Sergey", health=30)
    t = Treatment(strength=26)

    for i in range(4):
        t(p)
        print(p.health)


run(ex_two_persons)
run(ex_inheritance)
run(ex_property)
run(ex_callable)
