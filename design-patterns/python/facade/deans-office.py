"""Facade example."""


class DeansOffice:
    def __init__(self):
        self.d = Dean()
        self.c = Clerk()
        self.p = PrintSystem()

    def give_exam_sheet(self):
        self.c.give_exam_sheet()

    def give_certificate(self):
        self.c.give_certificate()

    def resolve_important_problem(self):
        self.d.appointment()

    def please_print_little_doc(self):
        self.p.print_something()


class Person:
    pass


class Dean(Person):
    def appointment(self):
        print("Dean talks with visitor")


class Clerk(Person):
    def give_exam_sheet(self):
        print("Clerk gives a sheet")

    def give_certificate(self):
        print("Clerk gives a certificate")


class Equipment:
    pass


class PrintSystem(Equipment):
    def print_something(self):
        print("Printer works...")


if __name__ == "__main__":
    office = DeansOffice()
    office.please_print_little_doc()
    office.resolve_important_problem()
    office.give_certificate()
    office.give_certificate()
    office.give_exam_sheet()
    office.please_print_little_doc()
