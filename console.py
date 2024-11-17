#!/usr/bin/python3
"""Module for the command line interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command line interpreter methods
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit program
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
