class Component:
    def operation(self):
        pass


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("Decorator A (before)")
        self._component.operation()
        print("Decorator A (after)")


class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("Decorator B (before)")
        self._component.operation()
        print("Decorator B (after)")


class ConcreteComponent(Component):
    def operation(self):
        print("Component itself")


if __name__ == "__main__":
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()
