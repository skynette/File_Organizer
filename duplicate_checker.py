
import os
import hashlib

def check_for_duplicates(directory):
	os.chdir(directory)
	index = {}
	duplicates = []
	for file in os.listdir(directory):
		if not os.path.isdir(file):
			target = open(file, 'rb')
			content = target.read()
			file_hash = hashlib.sha256(content).hexdigest()
			try:
				if index[file_hash]:
					print('Duplicate file found: '+file)
					duplicates.append(file)
					continue
			except:
				index[file_hash] = 1
	return duplicates

# path = input("PATH: ")
# print(check_for_duplicates(path))
# print("ENd of program")
# input()

# january 2021 ------- anime

def check_for_duplicates_optimized(directory):
	os.chdir(directory)
	index = {}
	duplicates = []
	for file in os.listdir(directory):
		if not os.path.isdir(file):
			target = open(file, 'rb')
			content = open('content.temp', 'wb')
			for line in target.readlines():
				if not line:
					break
				else:
					content.write(line)
			file_hash = hashlib.sha256(content).hexdigest()
			try:
				if index[file_hash]:
					print('Duplicate file found: '+file)
					duplicates.append(file)
					continue
			except:
				index[file_hash] = 1
	return duplicates

path = input("PATH: ")
print(check_for_duplicates_optimized(path))
print("ENd of program")
input()