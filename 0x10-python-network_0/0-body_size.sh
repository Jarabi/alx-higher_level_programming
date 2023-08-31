#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Fetch url
url="$1"

# Stores size of response in bytes
response_size=$(curl -sw "%{size_request}\n" "$url")

# Output response size
echo "$response_size"
