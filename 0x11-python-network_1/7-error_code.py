#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to
 the URL and displays the body of the response
"""
from requests import get
from sys import argv

if __name__ == "__main__":
    req = get(argv[1])
    if req.status_code >= 400:
        print("Error code:", req.status_code)
    else:
        print(req.text)
