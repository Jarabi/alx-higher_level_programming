#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    from sys import argv
    import requests

    query_term = ""
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) >= 2:
        query_term = argv[1]

    query = {'q': query_term}

    try:
        res = requests.post(url, data=query)
        response = res.json()

        if len(response) == 0:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError as err:
        print("Not a valid JSON")
