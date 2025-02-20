# import os
# new_directory="directory"
# os.mkdir(new_directory)
# if os.path.exists(new_directory):
#     print(f"directory'{new_directory}'created succesfull.")
# else:
#     print(f"failed to create '{new_directory}'.")

#shutil.get_unpack_formtas()
# import shutil
# formats=shutil.get_unpack_formats()
# print("supported unpacking formats:\n",formats)

import shutil
from pathlib import Path 
path = '/home/geethika/Documents/python_file/file_copy.txt'
info = Path(path)
user = info.owner()
group = info.group()
print("Current owner and group of the specified path") 
print("Owner:", user)
print("Group:", group)
user = 'geethika'
group = 'geethika'
shutil.chown(path, user, group) 
print("\nOwner and group changed")
info = Path(path)
user = info.owner()
group = info.group()
print("Current owner:", user)
print("Current group:", group)