#!/bin/bash


if [ "$#" -lt 2 ]; then
    echo "Usage: $0 /path/to/input_dir /path/to/output_dir [--max_depth N]"
    exit 1
fi

python3 main.py "$1" "$2" "$3" "$4"
