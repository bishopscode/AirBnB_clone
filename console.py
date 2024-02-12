#!/usr/bin/python3
"""
This module defines a command interpreter class for the AirBnB project.
"""
import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        """
        if not line:
            print("** class name missing **")
            return

        class_name = line.split()[0]
        if class_name not in ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = models.storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = models.storage.all()
        if key in all_objs:
            del all_objs[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        all_objs = models.storage.all()
        if not line:
            print([str(obj) for obj in all_objs.values()])
        elif line not in ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in all_objs.values() if type(obj).__name__ == line])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        if args[0] not in ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return

        key = args[0] + '.' + args[1]
        all_objs = models.storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        setattr(all_objs[key], args[2], args[3])
        models.storage.save()

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        Does nothing by default.
        """
        pass

    def do_EOF(self, line):
        """
        Handles the EOF signal to exit the program.
        """
        print()
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def precmd(self, line):
        """
        This method is called after the input prompt is displayed
        but before the input is read and interpreted.
        """
        if '.' not in line:
            return line
        else:
            units = line.split('.')
            class_name = units[0]
            motion = units[1]

            if motion == "all()":
                return class_name + " all"
            elif motion[:4] == "show":
                return class_name + " " + motion[5:-2]
            elif motion[:7] == "destroy":
                return class_name + " " + motion[8:-2]
            elif motion[:6] == "update":
                rest = motion[7:]
                idx = rest.find('"') + 1
                attribute = rest[:idx]
                rest = rest[idx + 1:].strip()
                idx = rest.find('"') + 1
                value = rest[:idx]
                return class_name + " " + rest[idx + 1:-1] + " " + attribute + " " + value
            else:
                return line

if __name__ == '__main__':
    HBNBCommand().cmdloop()
