#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.base_model import BaseModel
from models import storage
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
    """
    cmd Module.
    for building line-oriented command interpreters
    """
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
        Docs
        """
        staged_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    if len(line_array) > 1:
                        objs_dict = storage.all()
                        search_string = "{}.{}".format(
                                class_name, line_array[1])
                        if search_string in objs_dict:
                            print(objs_dict[search_string])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        staged_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    if len(line_array) > 1:
                        objs_dict = storage.all()
                        search_string = "{}.{}".format(
                                class_name, line_array[1])
                        if search_string in objs_dict:
                            del (objs_dict[search_string])
                            storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

def handle_custom_command(self, class_name, action):
        """Handling of custom commands like <class name>.all()
        or <class name>.count()."""
        parts = action.split("(")
        if len(parts) == 2 and parts[1].endswith(')'):
            action_name = parts[0]
            action_args = parts[1][:-1].split(',')

            # Removing of surrounding quotes if present
            action_args = [arg.strip('\"') for arg in action_args]

            if action_name == 'show':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no instance found **")
            elif action_name == 'all':
                instances = [
                    str(obj) for key, obj in storage.all().items()
                    if key.startswith(class_name + '.')
                ]
                print(instances)
            elif action_name == 'count':
                count = sum(
                    1 for key in storage.all()
                    if key.startswith(class_name + '.')
                )
                print(count)
            elif action_name == 'destroy':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print(f"** no instance found **")
            elif action_name == 'update':
                key = "{}.{}".format(class_name, action_args[0])
                if key in storage.all():
                    obj = storage.all()[key]
                    attribute_name = action_args[1]
                    attribute_value = action_args[2]

                    # Updating the attribute with the given value
                    setattr(obj, attribute_name, attribute_value)
                    obj.save()
                else:
                    print(f"** no instance found **")
            else:
                print(f"Unrecognized action: {action_name}.\
                Type 'help' for assistance.\n")
        else:
            print(f"Unrecognized action: {action}.\
            Type 'help' for assistance.\n")

def default(self, line):
        """Handle unrecognized commands."""
        parts = line.split('.')
        if len(parts) == 2:
            class_name, action = parts
            self.handle_custom_command(class_name, action)
        else:
            print(f"Unrecognized command: {line}.\
                  Type 'help' for assistance.\n")
def do_all(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        staged_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    full_list = []
                    for key, value in storage.all().items():
                        if (class_name in key):
                            full_list.append(str(value))
                    print(full_list)
                else:
                    print("** class doesn't exist **")
        else:
            full_list = []
            for key, value in storage.all().items():
                full_list.append(str(value))
            print(full_list)

def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        staged_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    if len(line_array) > 1:
                        objs_dict = storage.all()
                        search_string = "{}.{}".format(
                                class_name, line_array[1])
                        if search_string in objs_dict:
                            if len(line_array) > 2:
                                if len(line_array) > 3:
                                    if (line_array[3]
                                            not in
                                            ["created_at",
                                                "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(
                                            line_array[2]), str(line_array[3]))
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

def data_model_func(self, line, class_name):
        """
        handles all data models
        """
        allowed_methods = [".all()", ".count()"]
        show_regex = re.compile(r"\.show\(\"(.*?)\"\)")
        delete_regex = re.compile(r"\.destroy\(\"(.*?)\"\)")
        update_regex = re.compile(r"\.update\(\"(.*?)\", \"(.*?)\", (.*?)\)")
        update_dict_regex = re.compile(r"\.update\(\"(.*?)\",(.*?)\)")
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                command_method = line_array[0]
                if command_method in allowed_methods:
                    if command_method == ".all()":
                        self.do_all(class_name)
                    if command_method == ".count()":
                        self.get_count(class_name)
                elif (show_regex.search(line_array[0]) is not None):
                    obj_id = show_regex.search(line_array[0]).group(1)
                    self.do_show("{} {}".format(class_name, obj_id))
                elif (delete_regex.search(line_array[0]) is not None):
                    obj_id = delete_regex.search(line_array[0]).group(1)
                    self.do_destroy("{} {}".format(class_name, obj_id))
                elif (update_regex.search(line) is not None):
                    obj_id = update_regex.search(line).group(1)
                    obj_attr_name = update_regex.search(line).group(2)
                    obj_attr_value = update_regex.search(line).group(3)
                    self.do_update("{} {} {} {}".format(
                        class_name, obj_id, obj_attr_name, obj_attr_value))
                elif (update_dict_regex.search(line) is not None):
                    obj_id = update_dict_regex.search(line).group(1)
                    obj_dict = eval(update_dict_regex.search(line).group(2))
                    for key, value in obj_dict.items():
                        self.do_update("{} {} {} {}".format(
                            class_name, obj_id, key, value))

def get_count(self, class_name):
        """
        Account for full count of all the dataset
        """
        staged_classes = [
                "BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]
        if class_name in staged_classes:
            full_list = []
            for key, value in storage.all().items():
                if (class_name in key):
                    full_list.append(str(value))
            print(len(full_list))
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()