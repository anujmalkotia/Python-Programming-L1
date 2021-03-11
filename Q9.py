import os

path=os.path.abspath(input("Enter path::"))

size = 0
min_file=""

for folder,subfolders,files in os.walk(path):
    for file in files:
        size = os.stat(os.path.join(folder, file)).st_size

        if size==0:
            min_file=os.path.join(folder,file)
print("The smallest file is:",min_file)
            
