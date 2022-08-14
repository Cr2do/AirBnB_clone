#!/usr/bin/python3
"""
File storage
"""


class FileStorage:

    def __init__(self):
        self.__file_path = None
        self.__objects = None

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj] = 2
