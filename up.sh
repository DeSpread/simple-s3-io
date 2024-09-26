#!/bin/bash
if [ -z "$1" ]; then
  echo "Error: Missing argument. Please provide the required argument." >&2
  exit 1
fi
python3 main.py --mode up $1