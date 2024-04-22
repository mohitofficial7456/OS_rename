# this program is to change files names with the help of OS modules

import os

files = os.listdir("clutter")
print(files)

i = 0
for file in files:
    if file.endswith(".png"):
        os.rename(f"clutter/{file}",f"clutter/{i}.png")
        i=i+1
