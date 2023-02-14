#!/usr/bin/python3
"""Discribs a locked class"""


class LockedClass:
    """
    Only allows  new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
