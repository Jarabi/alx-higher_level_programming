#!/usr/bin/python3
"""
Manages urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            response = res.read().decode('utf-8')
        print(response)
    except HTTPError as e:
        print(f"Error code: {e.code}")
