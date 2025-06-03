#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
then saves them to a file as JSON.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"


def main():
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
