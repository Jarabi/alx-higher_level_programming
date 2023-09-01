#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the response body
If the HTTP status code is greater than or equal to 400, print: Error code:
followed by the value of the HTTP status code
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    res = requests.get(url)
    status_code = res.status_code

    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(res.text)
