#!/usr/bin/python3


"""
This FileStorage class serializes instances to a JSON file
and deserializes JSON file to instances.

ARGS:
    __file_path: Private class attribute. A path to the JSON file.

    __objects: Private class attribute. An empty dictionary
    to store all objects.

    Public instance methods:

    all(self): Returns the dictionary __objects.
    new(self, obj): sets in __objects the obj with key <obj class name>.id.
    save(self): serializes __objects to the JSON file (path: __file_path).
    reload(self): deserializes the JSON file to __objects
    (only if the JSON file (__file_path) exists, otherwise it does nothing.
"""


import os
import json
from models.base_model import BaseModel


class FileStorage:
    """A database that handles serialization and deserialization
    of instances.
    """

    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """Returns a dictionary of all valid classes."""

        return ({
            'BaseModel': BaseModel
        })

    def all(self):
        """Returns the dictionary __objects"""

        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        only if the JSON file exists, otherwise do nothing.
        """

        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    class_name, object_id = key.split(".")
                    class_obj = self.classes().get(class_name)
                    if class_obj:
                        obj = class_obj(**value)
                        self.__objects[key] = obj
