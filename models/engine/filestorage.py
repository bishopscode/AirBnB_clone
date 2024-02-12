#!/usr/bin/python3

# file_storage.py

from json import dumps, loads
from os.path import isfile

class FileStorage:
    def __init__(self):
        self.objects = {}
        self.__file_path = "file.json"

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file -> path: __file_path
        """
        full_dict = {
            key: value.to_dict() for key, value
            in self.objects.items()
        }
        json_string = dumps(full_dict)
        filename = self.__file_path
        with open(filename, "w") as f:
            f.write(json_string)

    def reload(self):
        """
        Deserialization of the JSON file to __objects.
        """
        staged_classes = ["BaseModel", "User", "State", "City",
                          "Amenity", "Place", "Review"]
        filename = self.__file_path
        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read()
                full_dict = loads(json_string)
            for key, value in full_dict.items():
                class_name, obj_id = key.split(".")
                if class_name in staged_classes:
                    obj = eval(class_name)(**value)
                    self.new(obj)
