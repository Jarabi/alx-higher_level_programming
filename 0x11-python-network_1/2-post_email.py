#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    params = {'email': argv[2]}

    data = urlencode(params)
    data_encoded = data.encode('ascii')
    req = Request(url, data_encoded)

    with urlopen(req) as res:
        response = res.read().decode('utf-8')

    print(response)
