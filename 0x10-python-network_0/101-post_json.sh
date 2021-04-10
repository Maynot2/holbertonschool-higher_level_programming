#!/bin/bash
# Send json
curl -s -d @"$2" -H 'Content-Type: application/json' "$1"
