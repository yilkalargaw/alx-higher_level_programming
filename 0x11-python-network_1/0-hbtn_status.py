#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    http_resp = resp.read()
    print("Body response:")
    print("\t- type: {}".format(type(http_resp)))
    print("\t- content: {}".format(http_resp))
    print("\t- utf8 content: {}".format(http_resp.decode("utf-8")))
