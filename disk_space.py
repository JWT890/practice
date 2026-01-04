import shutil

# gets the dis usage from shutil
total, used, free = shutil.disk_usage("/")

# calculates the total used
percent_used = (used / total) * 100

# prints the total used
print(f"Disk space used:  {percent_used}")

# if over 80%, prints a warning
if percent_used > 80:
    print("Warning: Disk usage is over 80%")