#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails” and prints all commits by:
`<sha>: <author name>` (one by line)
"""


if __name__ == "__main__":
    from sys import argv
    import requests

    repo = argv[1]
    owner = argv[2]
    params = {"per_page": 10}

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    res = requests.get(url, params=params)
    response = res.json()

    for line in response:
        print(f"{line.get('sha')}: {line.get('commit')['author']['name']}")
