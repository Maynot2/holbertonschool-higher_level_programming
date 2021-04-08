#!/bin/bash
# Displays accepted methods
curl -LsI $1 | grep Allow | cut -d':' -f2 | xargs
