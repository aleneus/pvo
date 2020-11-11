class Invoker:
    """"""
    def __init__(self):
        self._commands = []

    def store(self, command):
        self._commands.append(command)

    def execute(self):
        for command in self._commands:
            command.execute()


class Command:
    """Base class for commands."""
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        """Execute command."""
        raise NotImplementedError


class CommandInc(Command):
    """Increase value."""
    def execute(self):
        self._receiver.inc()


class CommandDec(Command):
    def execute(self):
        self._receiver.dec()


class Score:
    def __init__(self):
        self.amount = 0

    def inc(self):
        self.amount += 1

    def dec(self):
        self.amount -= 1

    def __repr__(self):
        return "Amount = {}".format(self.amount)


def main():
    score = Score()
    inc = CommandInc(score)
    dec = CommandDec(score)

    inv = Invoker()
    inv.store(inc)
    inv.store(inc)
    inv.store(inc)
    inv.store(dec)
    inv.execute()

    print(score)


if __name__ == "__main__":
    main()
