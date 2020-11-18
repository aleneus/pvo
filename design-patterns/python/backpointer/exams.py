"""Back pointer example (one-to-many)."""


class Patient:
    """Patient."""
    def __init__(self):
        self.__exams = set()

    def exams(self):
        """Return all examinations of patients."""
        return self.__exams


class Exam:
    """Examination."""
    def __init__(self, name, patient):
        self.__name = name
        self.__patient = patient
        self.__patient.exams().add(self)

    def __repr__(self):
        return "{}".format(self.__name)


def main():
    """Entry point."""
    pat = Patient()
    Exam("2020.01.01", pat)
    Exam("2020.01.02", pat)
    Exam("2020.01.03", pat)
    print(pat.exams())


if __name__ == "__main__":
    main()
