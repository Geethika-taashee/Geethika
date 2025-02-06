#os.name-returns the name
# import os
# print(os.name)


#os.error-exception raised
# import os
# try:
#     os.open('example.txt', os.O_RDONLY)
# except os.error as e:
#     print("Caught os.error:", e)



#os.popen()-used to open a pipe
# import os
# result=os.popen('ls').read()
# print(result)


#os.close()-used to delete the file descriptor
# import os
# file_descriptor=os.open("example.txt",os.O_RDONLY)
# os.close(file_descriptor)


#os.remove()-used to delete a file
# import os
# os.remove("example.txt")


#os.path.getsize()-return the size of a file in bytes
# import os
# size=os.path.getsize("os_module.py")
# print(f"file size : {size} bytes")


#os.path.exists()-if that file exists then it shows true other wise it shows false
import os
result=os.path.exists("example.txt")
print(result)