#!/usr/bin/python3
"""Size validation"""


class Square:
    """A class called Square"""
    def __init__(self, size=0):
        """Initialize a square
        Args:
            size: An int, the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
