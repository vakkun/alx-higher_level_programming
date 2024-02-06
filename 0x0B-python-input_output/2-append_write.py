#!/usr/bin/python3

"""
function that appends string
"""

def append_write(filename="", text=""):
    """returns the number of characters added:"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    # Example usage:
    append_write("example.txt", "This is an appended text.")
