#!/usr/bin/python3
"""IO Practice"""


from sys import argv
import os.path


savejson = __import__('5-save_to_json_file').save_to_json_file
loadjson = __import__('6-load_from_json_file').load_from_json_file

fname = "add_item.json"
loaded_list = loadjson(fname) if os.path.exists(fname) else []
loaded_list.extend(argv[1:])
savejson(loaded_list, fname)
