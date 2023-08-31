#!/bin/bash
# Bash script that makes a request to URL that causes the server to respond with a message
curl -sf -XGET -w "You got me!" 0.0.0.0:5000/catch_me
