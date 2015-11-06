# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from inspect import getmembers
from inspect import isdatadescriptor
from inspect import ismethod
from abc import ABCMeta


class StructuralTypeBase:

    def show_class(self):
        print(self.__class__)


class StructuralType(object, StructuralTypeBase):
    """Python is inherently nominal -- classes extend based on explicit
    class declarations, and are then checked by the internal Method Resolution
    Order. This class allows a new type checking system, that of structural."""

    __metaclass__ = ABCMeta
    DEBUG = True

    @staticmethod
    def _compare(self_methods, self_props, other_methods, other_props):
        """Prints the various properties and methods of the two
        methods used for comparison. Useful for debugging."""
        string = 'Self methods/props: {}, {} | Other methods/props: {}, {}'
        print(string.format(
            self_methods, self_props, other_methods, other_props))

    @staticmethod
    def _extract_props(cls):
        """Extracts all properties of this class for comparison."""
        return map(lambda e: e[0], getmembers(cls, predicate=isdatadescriptor))

    @staticmethod
    def _extract_members(cls):
        """Extracts the members of this class (methods) for comparison."""
        return map(lambda e: e[0], getmembers(cls, predicate=ismethod))

    @classmethod
    def __subclasshook__(cls, subclass):
        """Use an ABC and override subclass hook by looking over all the methods
        and properties of the class. This allows for structural comparison,
        instead of the typical inheritance pattern."""
        self_methods = StructuralType._extract_members(cls)
        other_methods = StructuralType._extract_members(subclass)
        self_props = StructuralType._extract_props(cls)
        other_props = StructuralType._extract_props(subclass)
        if cls.DEBUG:
            cls._compare(self_methods, self_props, other_methods, other_props)
        if self_methods == other_methods and self_props == other_props:
            return True
        return False

    def __str__(self):
        return str(StructuralType._extract_members(self))
