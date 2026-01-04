#!/bin/bash

ip=1.2.3.4.6

if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "IP address is valid"
else
    echo "Ip address is not valid"
fi