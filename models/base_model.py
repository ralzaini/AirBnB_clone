#!/usr/bin/python3

"""
    Module representing the Base class of
    all the classes
"""

import uuid
from datetime import datetime
import models
TIMEF = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    BaseModel class serves as a base class for other classes in the project.
    It has common attributes and methods that can be inherited by subclasses.

    Args:
        id(string): unique identifier for each instance
        created_at(datetime): time when the instance is created
        updated_at(datetime): time when the instance is updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        id: A unique identifier generated using uuid.uuid4().
        created_at: The current date and time when the instance is created.
        updated_at: The same as created_at, initially set to the same value.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, TIMEF))
                    else:
                        setattr(self, key, value)

            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with the current date and time.
        """

        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """

        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.strftime(TIMEF)[:-3]
        base_dict["updated_at"] = self.updated_at.strftime(TIMEF)[:-3]

        return base_dict

    def __str__(self) -> str:
        """
        Returns a string representation of the instance.
        """

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
