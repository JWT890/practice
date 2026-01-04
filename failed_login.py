import re
import collections
from collections import Counter
import os

# starts the count
count = 0
# opens the log file
with open("auth.log") as f:
    # looks for failed logins
    for line in f:
        # if the line contains failed logins
        if "Failed password" in line:
            # add 1
            count += 1
print("Failed password count:", count)
