#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.base_model import BaseModel
import models
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        command for quitting
        """
        return True

    def do_EOF(self, line):
        """
        determines what happens at end of file
        """
        return True

    def emptyline(self):
        """
        handles an empty line
        """
        pass

    def do_create(self, line):
        """
        handles the create action
        """
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                if line_array[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()
                    print(obj.id)
                elif line_array[0] == "User":
                    obj = User()
                    obj.save()
                    print(obj.id)
                elif line_array[0] == "State":
                    obj = State()
                    obj.save()
                    print(obj.id)
                elif line_array[0] == "City":
                    obj = City()
                    obj.save()
                    print(obj.id)
                elif line_array[0] == "Amenity":
                    obj = Amenity()
                    obj.save()
                    print(obj.id)
                elif line_array[0] == "Place":
                    obj = Place()
                    obj.save()
                    print(obj.id)
                elif line_array[0] == "Review":
                    obj = Review()
                    obj.save()
                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        if not line:
            print("** class name missing **")
            return

        line_array = line.split()
        if len(line_array) < 2:
            print("** instance id missing **")
            return

        class_name = line_array[0]
        obj_id = line_array[1]

        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        objs_dict = models.storage.all()
        if key in objs_dict:
            print(objs_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        if not line:
            print("** class name missing **")
            return

        line_array = line.split()
        if len(line_array) < 2:
            print("** instance id missing **")
            return

        class_name = line_array[0]
        obj_id = line_array[1]

        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        objs_dict = models.storage.all()
        if key in objs_dict:
            del objs_dict[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representations of instances based on the class name.
        """
        if not line:
            all_instances = models.storage.all().values()
        else:
            class_name = line.split()[0]
            if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                print("** class doesn't exist **")
                return
            all_instances = [obj for key, obj in models.storage.all().items() if key.startswith(class_name + ".")]

        print([str(instance) for instance in all_instances])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        """
        if not line:
            print("** class name missing **")
            return

        line_array = line.split()
        if len(line_array) < 2:
            print("** instance id missing **")
            return

        class_name = line_array[0]
        obj_id = line_array[1]

        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(class_name, obj_id)
        objs_dict = models.storage.all()
        if key not in objs_dict:
            print("** no instance found **")
            return

        if len(line_array) < 3:
            print("** attribute name missing **")
            return

        if len(line_array) < 4:
            print("** value missing **")
            return

        attribute_name = line_array[2]
        attribute_value = line_array[3]

        if attribute_name in ["id", "created_at", "updated_at"]:
            return

        obj = objs_dict[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def fill_custom_command(self, class_name, motion):
        """Handling of custom commands like <class name>.all()
        or <class name>.count()."""
        units = motion.split("(")
        if len(units) == 2 and units[1].endswith(')'):
            motion_name = units[0]
            motion_args = units[1][:-1].split(',')

            # Striping of surrounding quotes if present
            motion_args = [arg.strip('\"') for arg in motion_args]

            if motion_name == 'show':
                key = "{}.{}".format(class_name, motion_args[0])
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif motion_name == 'all':
                instances = [
                    str(obj) for key, obj in models.storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(instances)
            elif motion_name == 'count':
                count = sum(
                    1 for key in models.storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            elif motion_name == 'destroy':
                key = "{}.{}".format(class_name, motion_args[0])
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print(f"** no instance found **")
            elif motion_name == 'update':
                key = "{}.{}".format(class_name, motion_args[0])
                if key in models.storage.all():
                    obj = models.storage.all()[key]
                    attribute_name = motion_args[1]
                    attribute_value = motion_args[2]

                    # Updating the attribute with the given value
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print(f"** no instance found **")
            else:
                print(f"Unrecognized action: {motion_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {motion}.\
            Type 'help' for assistance.\n")

    def default(self, line):
        """Handle unrecognized commands."""
        units = line.split('.')
        if len(units) == 2:
            class_name, motion = units
            self.fill_custom_command(class_name, motion)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")

    def get_count(self, class_name):
        """
        Account for full count of all the dataset
        """
        staged_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if class_name in staged_classes:
            full_list = []
            for key, value in models.storage.all().items():
                if (class_name in key):
                    full_list.append(str(value))
            print(len(full_list))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
