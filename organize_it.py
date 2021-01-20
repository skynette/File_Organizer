import sys
import  os
import shutil
from colorama import Fore, Back, Style, init
from time import sleep
init(autoreset=True)

extensions = {}

extensions["images"] = ['.jpg', '.jpeg','.png','.gif']
extensions["videos"] = ['.mp4','.avi','.mkv', '.m4v']
extensions["music"] = ['.mp3','.wav','.aac']
extensions['archives'] = ['.zip', '.rar', '.rz']

print(Fore.CYAN+str(extensions)+'\n\n')

def create_folder(filetype):
	current_dir = os.getcwd()
	if not os.path.exists(os.path.join(current_dir, filetype)):
		print(Fore.YELLOW+'[+] creating directory for {}...'.format(filetype))
		os.mkdir(filetype)
		return True
	print(Fore.YELLOW+'[!] directory {} already exists, skipping...'.format(filetype))
	return True

def move_files(filename, destination):
	print(Fore.GREEN+'[*] moving {} to {}.....'.format(filename, destination))
	shutil.move(filename, destination)
	return True
	
for e in extensions:
	create_folder(e)

for files in os.listdir():
	file_name, extension = os.path.splitext(files)
	print(Fore.WHITE+"\n"+"[*] "+files)
	sleep(1)
	if extension:
		found = False
		found_dir = ''
		for file_type, extens in extensions.items():
			if extension in extens:
				found = True
				found_dir = file_type
		if found:
			print(Fore.GREEN+"[+] found extension in {}".format(found_dir))
			move_files(files, found_dir)
			print('\n')
		else: print(Fore.RED+'[-] not found in extension\n')
	else:
		print(Fore.YELLOW+'[+] Folder Type')

	
print(Fore.GREEN+'\n[+] OK!\n')