#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    if len(sys.argv) < 2:
        args = []
    else:
        args = sys.argv[1:]
    if os.path.isfile('add_item.json'):
        args = load_from_json_file('add_item.json') + args
    save_to_json_file(args, 'add_item.json')
    load_from_json_file('add_item.json')
