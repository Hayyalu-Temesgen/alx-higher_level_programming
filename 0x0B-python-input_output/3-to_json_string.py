#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
   """A function that return the JSON representation."""
    return json.dumps(my_obj)

