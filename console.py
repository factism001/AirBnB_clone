#!/usr/bin/python3
"""AirBnB console"""
import cmd



class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, line):
        """Quit command to exit the programm
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the programm
        """
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
