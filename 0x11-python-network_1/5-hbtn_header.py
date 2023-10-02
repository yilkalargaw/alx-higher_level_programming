#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    import sys
    try:
        print(requests.get(sys.argv[1]).headers['X-Request-Id'])
    except Exception:
        pass
