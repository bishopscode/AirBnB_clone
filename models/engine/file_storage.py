#!/usr/bin/python3
'''
Module Docs
'''
from json import dumps, loads
from models.base_model import BaseModel
from os.path import isfile
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:

    """
        Private class attributes:
    __file_path: string - path to JSON file
    __objects: dictionary - empty, will store all objects by <class name>.id
    """

    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # dictionary to store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        '''
        Serializes __objects to the JSON file -> path: __file_path
        '''
        full_dict = {
                key: value.to_dict() for key, value
                in FileStorage.__objects.items()}
        json_string = dumps(full_dict)
        filename = FileStorage.__file_path
        with open(filename, "w") as f:
            f.write(json_string)
   

    def reload(self):
        '''
        Deserialization of the JSON file to __objects.
        if the JSON file (__file_path) exists; or, do nothing.
        If the file does not exist, no exception should be raised
        '''
        staged_classes = ["BaseModel", "User", "State", "City",
                           "Amenity", "Place", "Review"]
        filename = FileStorage.__file_path
        if isfile(filename):
            with open(filename, "r") as f:
                json_string = f.read()
                full_dict = loads(json_string)
            for key, value in full_dict.items():
                class_name, obj_id = key.split(".")
                if class_name in staged_classes:
                    eval("self.new({}(**value))".format(class_name))

