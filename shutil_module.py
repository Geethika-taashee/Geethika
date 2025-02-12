# import shutil
# shutil.copy('file.txt','file_copy.txt')

#copying single files
# import shutil
# shutil.copy('file.txt','destination.txt')

#copying directories and their contents
# import shutil
# shutil.copytree('my_new_directory','target_dir')

#moving single files
# import shutil
# shutil.move('file.txt','my_directory/file.txt')

#moving directories and their contents
# import shutil
# shutil.move('my_new_directory','my_directory/my_new_directory')

#renaming files and directories
# import shutil
# shutil.move('example.txt','example_new.txt')

#deleting files and directories
# import os
# os.remove('file1.txt')

#deleting directories
# import shutil
# shutil.rmtree('directory')

#working with file permissions and attributes
# import shutil
# shutil.copystat('file_copy.txt','example_new.txt')

#finding a file
# import shutil
# cmd='python3'
# locate=shutil.which(cmd)
# print(locate)

#shutil.disk_usage()method
# import shutil
# path='/'
# memory=shutil.disk_usage(path)
# print(memory)

# import shutil
# path='/home/geethika/Documents/python_file'
# memory=shutil.disk_usage(path)
# print(memory)

# import shutil
# path='/home/geethika/Documents/python_file'
# stat=shutil.disk_usage(path)
# print("Disk usage statistics:")
# print(stat)

#shutil.get_terminal_size()
# import shutil
# terminal_size=shutil.get_terminal_size()
# print(terminal_size)

# import shutil
# size = shutil.get_terminal_size()
# print(f"Terminal size: {size.columns} columns, {size.lines} lines")

#shutil.make_archive()
# import shutil
# shutil.make_archive('example.py', 'zip', 'folder_to_compress')

#shutil.unpack_archive()
# import shutil
# shutil.unpack_archive('example.py.zip','extracted_folder')