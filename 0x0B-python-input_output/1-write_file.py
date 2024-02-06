#!/usr/bin/python3

"""
Python Module created by vak
"""

def write_file(filename="", text=""):
    """
    function that writes text to a utf-8 encoded file
    Arguments:
        filename (str): The name of the file
        text (str): The text to write
    Return:
        A file with text written
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        return my_file.write(text)


if __name__ == "__main__":
    # Example usage:
    write_file("example.txt", "This is an example text.")
