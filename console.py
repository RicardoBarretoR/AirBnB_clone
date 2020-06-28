#!/usr/bin/python3
"""
program called console.py that contains the
entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb) "

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
        """Creates a new instance of BaseModel, saves it and prints the id"""
        allClass = ["BaseModel"]
        entry_arg = arg.split()
        if len(entry_arg) == 0:
            print("** class name missing **")
        else:
            if entry_arg[0] in allClass:
                if entry_arg[0] == "BaseModel":
                    new_inst = BaseModel()
                    new_inst.save()
                    print(new_inst.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the str representation of an instance
        based on the class name and id
        """
        allClass = ["BaseModel"]
        entry_arg = arg.split()
        all_objs = storage.all()
        if len(entry_arg) == 0:
            print("** class name missing **")
        elif entry_arg[0] not in allClass:
            print("** class doesn't exist **")
        elif len(entry_arg) == 1:
            print("** instance id missing **")
        else:
            try:
                for k in all_objs.keys():
                    if obj.id == entry_arg[0] and entry_arg[1] in keys:
                        print("{}.{}".format(type(obj).__name__, obj.id))
            except:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        allClass = ["BaseModel"]
        entry_arg = arg.split()
        all_objs = storage.all()
        if len(entry_arg) == 0:
            print("** class name missing **")
        elif entry_arg[0] not in allClass:
            print("** class doesn't exist **")
        elif len(entry_arg) == 1:
            print("** instance id missing **")
        else:
            try:
                for k in all_objs.keys():
                    if obj.id == entry_arg[0] and entry_arg[1] in keys:
                        inst = ("{}.{}".format(type(obj).__name__, obj.id))
                        del all_objs[inst]
                    storage.save()
            except:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        allClass = ["BaseModel"]
        entry_arg = arg.split()
        all_objs = storage.all()
        list_ins = []
        if entry_arg[0] not in allClass:
            print("** class doesn't exist **")
        else:
            try:
                for instance in all_objs:
                    inst_str = str(all_objs[instance])
                    list_ins.append(inst_str)
                    print(list_ins)
                    break
            except e:
                pass

    def do_update(self, arg):
        allClass = ["BaseModel"]
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
                setattr(all_objs, entry_arg[2], entry_arg[3])
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
