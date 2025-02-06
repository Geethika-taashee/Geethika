#os.path.basename(path)-used to return the  basename of the file
# import os
# result=os.path.basename("/home/documents")
# print(result)


#os.path.dirname(path)-used to return the directory name
# import os
# result=os.path.dirname("/home/documents")
# print(result)


#os.path.isabs(path)-specify wheather path is absolute or not
# import os
# result=os.path.isabs("/home/documents")
# print(result)


#os.path.isdir(path)-the path is existing directory or not
# import os
# path = "/home/geethika/Documents/python_file/"
# if os.path.isdir(path):
#     print(f"'{path}' is a directory.")
# else:
#     print(f"'{path}' is not a directory.")

# import os
# result=os.path.isdir("/home/geethika/Documents/python_file")
# print(result)


#os.path.isfile(path)-the path is existing file or not
# import os
# result = os.path.isfile("/home/geethika/Documents/python_file/example.txt")
# print(result)


#os.path.normcase(path)
# import os
# result=os.path.normcase("/home/geethika")
# print(result)


#os.path.normpath(path)
# import os
# result=("home/./documents")
# print(result)

# import os
# normalized_path = os.path.normpath("folder//subfolder/../file.txt")
# print("Normalized path:", normalized_path)


#os.path.abspath(path)
import os
file_name='example.txt'
print(os.path.abspath(file_name))

#os.path.join
# import os
# file_path=os.path.join("home","Documents","example.txt")
# print("joined parts:",file_path)

#os.path.split(path)
# import os
# file_path="/home/Documents/example.txt"
# dir_name,file_name=os.path.split(file_path)
# print("Directory:",dir_name)
# print("File Name:",file_name)