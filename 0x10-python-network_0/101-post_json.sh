#!/bin/bash
# Send json
curl --data '{"name": "John Doe", "age": 33}' -H 'Content-Type: application/json' $1
