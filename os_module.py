#os.getcwd()-current working directory
# import os
# cwd=os.getcwd()
# print("current working directory:",cwd)


#os.chdir()-change directory
# import os
# new_directory='/home/geethika/Documents'
# os.chdir(new_directory)
# print("current working directory:",os.getcwd())


# import os 
# new_directory='/home/geethika/Documents/python_file'
# os.chdir(new_directory)
# print("current working directory:",os.getcwd())


#os.mkdir()-create directory
# import os
# new_directory="my_new_directory"
# os.mkdir(new_directory)
# if os.path.exists(new_directory):
#     print(f"directory'{new_directory}'created succesfull.")
# else:
#     print(f"failed to create '{new_directory}'.")


#os.makedirs()-create directory
# import os
# path="my_directory/subdirectories"
# os.makedirs(path)
# if os.path.exists(path):
#     print("directory structure created succesfull")
# else:
#     print("directory creation failed")


#os.listdir()-list files in current directory
import os
print("files and directories:",os.listdir())