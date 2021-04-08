#!/bin/bash
# Send json
curl --data "$2" -H 'Content-Type: application/json' "$1"
