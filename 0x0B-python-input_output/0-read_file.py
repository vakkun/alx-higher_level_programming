#!/usr/bin/python3

""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file
    Args:
        filename: filename
    Raises
        Exception: when the file can't be opened
    """

    try:
        with open(filename, 'r', encoding="utf-8") as f:
            read_data = f.read()
            print(read_data, end='')
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Example usage:
    read_file("example.txt")

