#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sL "$@" -X OPTIONS -i |  grep -i "allow" | cut -d " " -f2-10
