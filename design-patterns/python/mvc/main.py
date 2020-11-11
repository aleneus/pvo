import cmd, argparse

from model import *
from view import *
from controller import *


class BuildingShell(cmd.Cmd):
    intro = '\nWelcome to the Building shell. Type help or ? to list commands.\n'
    prompt = 'building> '

    def do_quit(self, arg):
        """ Close data base and exit igrouper. """
        return True

    def do_info(self, arg):
        controller.set_view(tv)
        controller.info()

    def do_purpose(self, arg):
        """
        Syntax: purpose number

        Get purpose of room.
        """
        args = arg.split()
        controller.set_view(tv)
        controller.purpose(args[0])

    def do_numbers(self, arg):
        """
        Syntax: numbers pupose
        """
        args = arg.split()
        controller.set_view(tv)
        controller.numbers_by_purpose(args[0])

    def do_html_info(self, arg):
        args = arg.split()
        controller.set_view(hv)
        controller.info()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="Name of data base")
    args = parser.parse_args()

    model = BuildingModel()
    tv = BuildingTextView()
    hv = BuildingHtmlView('info.html')
    controller = BuildingController(model)

    controller.open_or_create_db(args.file_name)

    BuildingShell().cmdloop()
