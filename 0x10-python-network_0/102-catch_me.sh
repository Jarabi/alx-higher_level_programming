#!/bin/bash
# Bash script that makes a request to URL that causes the server to respond with a message
curl -sL -X PUT -H "Origin:School" -d "user_id=98" 0.0.0.0:5000/catch_me_2
