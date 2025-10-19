

import shutil

# Check disk usage of C: drive
total, used, free = shutil.disk_usage("C:/")

print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

# Alert if free space < 10 GB
if free // (2**30) < 10:
    print("Warning: Low disk space!")
else:
    print("Disk space is sufficient.")
