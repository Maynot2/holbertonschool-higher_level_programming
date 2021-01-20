#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    args = sys.argv
    save_to_json_file(args[1:], 'add_item.json')
    print(load_from_json_file('add_item.json'))
