#!/usr/bin/python3

"""
    Module for the console
"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    Console class for HBNB project
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True
    
    def help_quit(self, arg):
        """
        Print help message for exit command
        """
        print("Quit command to exit the program")
    
    def do_EOF(self, arg):
        """
        Handle End-of-File (EOF) input
        """
        print("")
        return True
    
    def emptyline(self):
        """
        Empty the last command
        """
        pass
    
if __name__ == "__main__":
    HBNBCommand().cmdloop