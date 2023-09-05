#!/usr/bin/python3
"""
Connects to Personal Github account and fetches Github id
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    username = argv[1]
    token = argv[2]

    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"token {token}"
    }

    res = requests.get(url, headers=headers)
    response = res.json()

    print(f"{response.get('id')}")
