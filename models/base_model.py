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

    def __init__(self):
        self.id = uuid.uuid4().__str__()
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

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
