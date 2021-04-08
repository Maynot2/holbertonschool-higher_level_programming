#!/bin/bash
# Send json
curl -d @"$2" -H 'Content-Type: application/json' $1
