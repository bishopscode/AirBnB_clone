#!/usr/bin/python3

# main.py

import models
from cmd import Cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from file_storage import FileStorage  # Import FileStorage class

class HBNBCommand(Cmd):
    prompt = "(hbnb) "

    def __init__(self):
        super().__init__()
        # Instantiate FileStorage and assign it to models.storage
        models.storage = FileStorage()

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
                class_name = line_array[0]
                if class_name in models.storage.CLASSES:
                    obj = models.storage.CLASSES[class_name]()
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
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    if len(line_array) > 1:
                        objs_dict = models.storage.all()
                        scout_string = "{}.{}".format(
                            class_name, line_array[1])
                        if scout_string in objs_dict:
                            print(objs_dict[scout_string])
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
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    if len(line_array) > 1:
                        objs_dict = models.storage.all()
                        scout_string = "{}.{}".format(
                            class_name, line_array[1])
                        if scout_string in objs_dict:
                            del (objs_dict[scout_string])
                            models.storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        staged_classes = [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    full_list = []
                    for key, value in models.storage.all().items():
                        if (class_name in key):
                            full_list.append(str(value))
                    print(full_list)
                else:
                    print("** class doesn't exist **")
        else:
            full_list = []
            for key, value in models.storage.all().items():
                full_list.append(str(value))
            print(full_list)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        staged_classes = [
            "BaseModel", "User", "State", "City",
            "Amenity", "Place", "Review"
        ]
        if len(line) > 0:
            line_array = line.split()
            if len(line_array) > 0:
                class_name = line_array[0]
                if class_name in staged_classes:
                    if len(line_array) > 1:
                        objs_dict = models.storage.all()
                        scout_string = "{}.{}".format(
                            class_name, line_array[1])
                        if scout_string in objs_dict:
                            if len(line_array) > 2:
                                if len(line_array) > 3:
                                    if (line_array[3]
                                            not in
                                            ["created_at",
                                             "updated_at", "id"]):
                                        setattr(
                                            objs_dict[scout_string],
                                            str(line_array[2]),
                                            str(line_array[3]))
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
