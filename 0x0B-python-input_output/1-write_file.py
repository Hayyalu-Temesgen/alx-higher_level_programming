#!/usr/bin/python3
"""Defines a write function file."""


def write_file(filename="", text=""):
    """A function that writes a string to a text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(text)
    except FileNotFoundError:
        # If the file doesnt exist, create it and write the content
        with open(filename, 'w', encoding='utf-8') as new_f:
            num_chars_written = new_f.write(text)
            return num_chars_written
