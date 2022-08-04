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
        self.id = uuid.uuid4()
        self.created_at = datetime().today()
        self.updated_at = datetime().today()

    def __str__():
        pass

    def save(self):
        self.updated_at = datetime().now()

    def to_dict(self):
        valueToReturn = {}
        valueToReturn.pop(self.__dict__)
        valueToReturn.pop(self.__class__())
        valueToReturn.pop(json.dump(self.created_at, fp))
        valueToReturn.pop(json.dump(self.updated_at, fp))
        return valueToReturn
