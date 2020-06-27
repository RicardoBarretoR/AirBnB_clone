#!/usr/bin/python3
"""
program called console.py that contains the 
entry point of the command interpreter
"""
import cmd
import models.base_model 


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb)" 

    def do_quit(self, arg):
        """to exit the program"""
        self.close()
        return True

    def do_EOF(self, arg):
        """"""
        self.close()
        return True

    def do_help_quit(self, arg):
        """"""
        print("Quit command to exit the program")

    def do_help_EOF(self, arg):
        """"""
        print("EOF command to exit the program")

    def emptyline(self):
         pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()