#!/bin/bash

# checks to see if the service is running
if systemctl is-actve --quiet "$SERVICE"; then
    # if it is running, says it is
    echo "$SERVICE is running"
else
    # if not
    echo "$SERVICE is not running"
fi