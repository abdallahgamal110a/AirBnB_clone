#!/usr/bin/python3
"""
    Main Console program
"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Console
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "State": State,
        "Place": Place,
        "Review": Review,
    }

    def do_EOF(self, line):
        """Quit the program"""
        print("")
        return True

    def do_quit(self, line):
        """Quit the program"""
        return True

    def do_help(self, arg):
        """help cmd in Program"""
        return super().do_help(arg)

    def emptyline(self):
        """Ignore empty inputs"""
        pass

    def do_prompt(self, line):
        """propt = (hbnb)"""
        self.prompt = line

    def do_create(self, arg):
        """Creates a new instance of a Model"""
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        else:
            name = HBNBCommand.__classes[argl[0]]
            new_instance = name()
            name.save(new_instance)
            print(new_instance.id)

    def do_show(self, arg):
        """string representation of an instance"""
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(argl) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            store = storage.all(argl[0])
            if key in store:
                print(store[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(argl) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argl[0], argl[1])
            store = storage.all(argl[0])
            if key in store:
                garbage = store.pop(key)
                del garbage
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """string representation of all instances"""
        argl = arg.split()
        store = storage.all()
        if not argl:
            for key in store.keys():
                print(store[key])
        else:
            if argl not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            else:
                for value in store.values():
                    if value.__class__.__name__ == argl:
                        print(value)

    def do_update(self, arg):
        """Updates an instance adding or updating attribute"""
        argl = arg.split()
        store = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes.keys():
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif f"{argl[0]}.{argl[1]}" not in store.keys():
            print("** no instance found **")
        elif len(argl) == 2:
            print("** attribute name missing **")
        elif len(argl) == 3:
            print("** value missing **")
        else:
            instan = store[f"{argl[0]}.{argl[1]}"]
            instan.__dict__[argl[2]] = argl[3]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
