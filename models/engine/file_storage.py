#!/usr/bin/python3
""" class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances """

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Manages storage and retrieval of instances of BaseModel using JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """
        Adds a new instance of BaseModel to the __objects dictionary.

        Args:
            obj (BaseModel): The instance of BaseModel to be added.
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def all(self):
        """
        Retrieves all instances of BaseModel from the __objects dictionary.

        Returns:
            dict: A dictionary containing all instances of BaseModel.
        """
        return FileStorage.__objects

    def save(self):
        """
        Serializes the __objects dictionary into JSON format and,
        saves it to the file specified by __file_path.
        """
        a_objs = FileStorage.__objects
        objs_dict = {}
        for key, value in a_objs.items():
            objs_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(objs_dict, f)

    def reload(self):
        """
        Deserializes the JSON file specified by __file_path,
        and loads the instances of BaseModel into the __objects dictionary.
        """

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding='utf-8') as f:
                try:
                    objs_dict = json.load(f)
                    for key, value in objs_dict.items():
                        class_name, objs_dict = key.split('.')
                        cls = eval(class_name)
                        inst = cls(**value)
                        FileStorage.__objects[key] = inst
                except Exception:
                    print(f"Error during deserialization: {e}")
