#!/usr/bin/python3
"""
program that contains the entry
point of the command interpreter
"""

import cmd
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb) "
    allClass = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_EOF(self, line):
        """to exit the program"""
        return True

    def help_quit(self):
        """displays the list of available commands"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """displays the list of available commands"""
        print("EOF command to exit the program")

    def emptyline(self):
        """print empty line"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it and prints the id
        """
        allClass = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]
        entry_arg = arg.split()
        if len(entry_arg) == 0:
            print("** class name missing **")
        else:
            if entry_arg[0] in allClass:
                if entry_arg[0] == "BaseModel":
                    new_inst = BaseModel()
                if entry_arg[0] == "User":
                    new_inst = User()
                if entry_arg[0] == "State":
                    new_inst = State()
                if entry_arg[0] == "City":
                    new_inst = City()
                if entry_arg[0] == "Amenity":
                    new_inst = Amenity()
                if entry_arg[0] == "Place":
                    new_inst = Place()
                if entry_arg[0] == "Review":
                    new_inst = Review()
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the str representation of an
        instancebased on the class name and id
        """
        allClass = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]
        entry_arg = arg.split()
        all_objs = storage.all()
        if len(entry_arg) == 0:
            print("** class name missing **")
        elif entry_arg[0] not in self.allClass:
            print("** class doesn't exist **")
        elif len(entry_arg) == 1:
            print("** instance id missing **")
        else:
            inst = entry_arg[0] + "." + entry_arg[1]
            if inst in all_objs:
                print(all_objs[inst])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        allClass = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]
        entry_arg = arg.split()
        all_objs = storage.all()
        if len(entry_arg) == 0:
            print("** class name missing **")
        elif entry_arg[0] not in allClass:
            print("** class doesn't exist **")
        elif len(entry_arg) == 1:
            print("** instance id missing **")
        else:
            inst = ("{}.{}".format(entry_arg[0], entry_arg[1]))
            if inst in all_objs:
                del all_objs[inst]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name.
        """
        allClass = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]
        entry_arg = arg.split()
        all_objs = storage.all()
        list_ins = []
        if entry_arg[0] not in self.allClass:
            print("** class doesn't exist **")
        else:
            try:
                for instance in all_objs:
                    inst_str = str(all_objs[instance])
                    list_ins.append(inst_str)
                    print(list_ins)
            except:
                pass

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        allClass = ["BaseModel", "User", "State",
                    "City", "Amenity", "Place", "Review"]
        entry_arg = arg.split()
        all_objs = storage.all()
        if len(entry_arg) == 0:
            print("** class name missing **")
        elif entry_arg[0] not in allClass:
            print("** class doesn't exist **")
        elif len(entry_arg) == 1:
            print("** instance id missing **")
        elif len(entry_arg) == 2:
            print("** attribute name missing **")
        elif len(entry_arg) == 3:
            print("** value missing **")
        else:
            inst = ("{}.{}".format(entry_arg[0], entry_arg[1]))
            if inst in all_objs:
                setattr(all_objs[inst], entry_arg[2], entry_arg[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
