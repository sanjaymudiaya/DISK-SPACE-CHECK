import shutil

# Check disk usage of C: drive
total, used, free = shutil.disk_usage("C:/")

print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")

# Alert if free space < 20 GB
if free // (2**30) < 10:
    print("Warning: Low disk space!") 
elif free // (2*30) < 50:
    print("Disk space is average")
elif free // (2*30) < 75:
    print("Disk space is quite normal")
elif free // (2*30) < 100:
    print("Disk space is sufficiant")
elif free // (2*30) < 125:
    print("Disk space is very good")
else:
    print("Disk space is a lot")
