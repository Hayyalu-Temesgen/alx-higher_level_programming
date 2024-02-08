#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """A function that return the Python object representation of a JSON string.

    Args:
        my_str (str): The name of the file
    Return:
        The JSON string.
    """
    return json.loads(my_str)
