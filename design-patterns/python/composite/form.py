"""Composite pattern. Imitation of some GUI."""


class Component:
    """ Abstract component. """
    def __init__(self, caption=""):
        self.caption = caption

    def show(self):
        raise NotImplementedError


class Button(Component):
    def show(self):
        print("[{}]".format(self.caption))


class LineEdit(Component):
    def show(self):
        print("{} [               ]".format(self.caption))


class CheckBox(Component):
    def show(self):
        print("[ ] {}".format(self.caption))


class Frame(Component):
    """ Abstract frame. """
    def __init__(self, caption):
        super().__init__(caption)
        self._components = []

    def add_component(self, component):
        if component not in self._components:
            self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)


class Form(Frame):
    def show(self):
        print("======== {} ========".format(self.caption))
        for c in self._components:
            c.show()
        bottom_line = ""
        for i in range(len(self.caption)):
            bottom_line += "="
        print("========={}=========".format(bottom_line))


class CheckGroup(Frame):
    def show(self):
        print("-------- {} --------".format(self.caption))
        for c in self._components:
            c.show()
        # TODO: repeated from Form
        bottom_line = ""
        for i in range(len(self.caption)):
            bottom_line += "-"
        print("---------{}---------".format(bottom_line))


def main():
    f = Form("Human info")
    f.add_component(LineEdit("Name: "))
    f.add_component(LineEdit(" Age: "))
    c = CheckGroup("Options")
    c.add_component(CheckBox("Married"))
    c.add_component(CheckBox("Drives car"))
    c.add_component(CheckBox("Plays music"))
    c.add_component(CheckBox("Speacks English"))
    c.add_component(CheckBox("Likes sport"))
    f.add_component(c)
    f.add_component(Button("Save"))
    f.add_component(Button("Cancel"))
    f.show()


if __name__ == "__main__":
    main()
