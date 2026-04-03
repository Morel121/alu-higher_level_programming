#!/usr/bin/python3
"""
This script adds all arguments to a Python list, and then saves them to a file.
"""
import sys
import os

# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    
    # Check if the file exists; if so, load the list. If not, start with an empty list.
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # sys.argv[1:] captures all arguments passed to the script (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)
