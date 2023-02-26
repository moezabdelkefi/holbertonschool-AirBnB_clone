#!/usr/bin/python3
""" Module for command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ Empty line + ENTER shouldn’t execute anything """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            new_inst = eval(args[0])()
            new_inst.save()
            print(new_inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            print(obj)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            obj.delete()
            storage.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        objects = storage.all()
        args = arg.split()
        if not arg:
            print([str(v) for v in objects.values()])
        elif args[0] in storage.classes:
            print([str(v) for k, v in objects.items() if args[0] in k])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            obj = storage.all()[f"{args[0]}.{args[1]}"]
        except KeyError:
            print("** no instance found **")
            return
        except IndexError:
            print("** instance id missing **")
            return
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], type(getattr(obj, args[2]))(args[3]))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
