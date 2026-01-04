import re
import argparse
import os
from collections import Counter

# Define the path to the log file
log_file = 'auth.log'

# function that counts the occurences of IP addresses
def count_ip_occurences(log_file):
    # Regular expression pattern to match IP addresses
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    # reads the log file and counts
    ip_counts = Counter()
    with open(log_file, 'r') as f:
        # loops through the log file
        for line in f:
            # finds the IP addresses and adds them to the counter
            ips = re.findall(ip_pattern, line)
            # looks at the IP addresses
            for ip in ips:
                # adds 1 the the counter
                ip_counts[ip] += 1
    return ip_counts
# printes the amount
print("Extracted IP addresses counts: ", count_ip_occurences(log_file))