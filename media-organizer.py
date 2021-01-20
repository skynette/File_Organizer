import os
import math
from duplicate_checker import check_for_duplicates

num_of_files = 0
num_of_folders = 0
size_of_dir = 0
print("File counter, select head folder path")
path = input("Path: ")

def search_file(directory):
	global num_of_files
	global num_of_folders
	global size_of_dir

	size_of_dir = os.path.getsize(directory)
	if os.path.isdir(directory):
		rw = os.access(directory, os.R_OK) and os.access(directory, os.W_OK)
		try:
			for filename in os.listdir(directory):
				sub_dir = os.path.join(directory, filename)
				if not os.path.isdir(sub_dir):
					print(sub_dir)
					num_of_files+=1
				else:
					print(sub_dir)
					num_of_folders+=1
				size_of_dir+=search_file(sub_dir)
		except Exception as err:
			print(err)
	return size_of_dir

# rw = os.access(path, os.R_OK) and os.access(path, os.W_OK)
search_file(path)
print("Total files: {}, Total folders: {}, Approx Total size of dir: {}mb".format(num_of_files, num_of_folders, math.ceil(size_of_dir/1048576)))

check_for_duplicates(path)