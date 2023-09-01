#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header.
"""
from sys import argv
from urllib.request import Request, urlopen

req = Request(argv[1])

with urlopen(req) as res:
    header = res.getheader("X-Request-Id")
    print(header)
