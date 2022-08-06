#!/usr/bin/python3
"""
Module BaseModel
"""

from datetime import datetime
import uuid
import json


class BaseModel:
    """
    BaseModel Class
    """

    def __init__(self, *args, **kwargs):
        # id
        if "id" in kwargs:
            self.id = kwargs.get("id")
        else:
            self.id = uuid.uuid4().__str__()

        # created at
        if "created_at" in kwargs:
            self.created_at = datetime.fromisoformat(kwargs.get("created_at"))
        else:
            self.created_at = datetime.today()

        # updated at
        if "updated_at" in kwargs:
            self.updated_at = datetime.fromisoformat(kwargs.get("updated_at"))
        else:
            self.updated_at = datetime.today()

        # name
        if "name" in kwargs:
            self.name = kwargs.get("name")

        # my_number
        if "my_number" in kwargs:
            self.my_number = kwargs.get("my_number")

    def save(self):
        self.updated_at = datetime.now()

    def __str__(self):
        return str("[" + self.__class__.__name__ + "] (" + self.id + ") " + str(self.__dict__))

    def to_dict(self):
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.id = str(self.id)
        self.__dict__["__class__"] = str(self.__class__)
        value_to_return = self.__dict__
        return value_to_return
