#!/bin/bash
# Displays the status code
curl -w "%{http_code}\n" $1 -o /dev/null -s
