#!/usr/bin/python3
"""
 Python script that takes in a URL and an email sends a
 POST request to the passed URL with the email as aparameter,
 and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], data) as url:
        d = url.read()
        print(d.decode('utf-8'))
