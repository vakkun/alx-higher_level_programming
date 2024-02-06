#!/usr/bin/python3

"""Defines a text file-reading function."""


def read_file(filename""");
"""print the contents of a UTF8 text file to stdout."""
with open(filename
=======
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can be opened
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
