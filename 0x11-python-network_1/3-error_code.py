#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        with urlopen(argv[1]) as url:
            print(url.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code:', error.code)
