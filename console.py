#!/usr/bin/python3
""" Contains the entry point of the command interpreter"""
import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    prompt = '(hbnb) '

    # ----- basic commands -----
    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ Exit with EOF command """
        print()
        return True

    # ----- command with arguments -----
    def do_create(self, arg):
        """ Create a new instance of BaseModel and saves it """
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            new_inst = eval(arg)()
            new_inst.save()
            print(new_inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return
        try:
            if args[2]:
                print(eval(args[0])(**obj.to_dict()).__dict__[args[2]])
                return
        except IndexError:
            pass
        print(obj)

    def do_destroy(self, arg):
        """ Deletes an instance """
        args = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[args[0] + "." + args[1]]
            del obj
            storage.save()
        except KeyError:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        args = arg.split()
        objects = storage.all()
        lst = []
        if len(arg) == 0:
            for obj_id in objects:
                lst.append(str(objects[obj_id]))
            print(lst)
            return
        try:
            for obj_id in objects:
                obj = objects[obj_id]
                if obj.__class__.__name__ == args[0]:
                    lst.append(str(obj))
            print(lst)
            return
        except KeyError:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        """ Updates an instance """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if args[3].isdigit():
            args[3] = int(args[3])
        setattr(obj, args[2], args[3])
        obj.save()

    # ----- extra commands -----
    def do_count(self, arg):
        """ Counts the number of instances of a class """
        count = 0

if __name__ == "__main__":
    HBNBCommand().cmdloop()
