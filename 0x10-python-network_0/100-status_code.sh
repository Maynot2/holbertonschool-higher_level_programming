#!/bin/bash
# Displays the status code
curl -w "%{http_code}" $1 -o /dev/null -s
