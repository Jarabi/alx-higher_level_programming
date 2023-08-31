#!/bin/bash
# A script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

# Fetch url
url="$1"

# Store curl response
response=$(curl -s "$url")

# Get response length
length="${#response}"

# Output length
echo "$length"
