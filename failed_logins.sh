#!/bin/bash

files='auth.log'

echo "Analyzing file"

for file in $files; do
    if cat $files | grep "Invalid user" | cut -d ' ' -f 10 | sort | uniq -c | sort -nr; then
    echo "Complete"
    fi
done