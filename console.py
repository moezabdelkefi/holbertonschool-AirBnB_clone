#!/usr/bin/python3
"""this is the declaration of the class HBNBCommand"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import re


def parse(arg):
    """this funcrion parse the line arg"""
    match_list = re.findall(r"\{(.*?)\}|\[(.*?)\]|(\S+)", arg)
    return [match[0] or match[1] or match[2] for match in match_list]


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "City",
        "State",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file,
        and prints the id.
        Usage: create <class name>
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            models.storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if not arg[1]:
            print("** class doesn't exist **")
            return
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        inst_id = args[1]
        key = cls_name + '.' + inst_id
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if not arg[1]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        inst_id = args[1]
        key = cls_name + '.' + inst_id
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in models.storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        Update an instance based on the class name and id by
        adding or updating attribute.
        """
        args = arg.split()
        obj_dict = models.storage.all()

        # Check for class name
        if len(args) < 1:
            print("** class name missing **")
            return False

        cls_name = args[0]

        # Check if class exists
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False

        # Check for id
        if len(args) < 2:
            print("** instance id missing **")
            return False

        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False

        obj_id = args[1]
        key = cls_name + "." + obj_id

        # Check for attribute name
        if len(args) < 3:
            print("** attribute name missing **")
            return False

        attr_name = args[2]

        # Check for attribute value
        if len(args) < 4:
            print("** value missing **")
        else:
            attr_value = str(args[3][1:-1])
            obj = obj_dict[key]
            setattr(obj, attr_name, attr_value)
            models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
