import module_import.common.find as find
print(find.find_matching_friend(['Roe', 'Joe', 'Doe', 'Moe', 'Boe'], lambda x: x == 'Joe'))

# If you want to run any file as a script using absolute import, it is essential to
# set PYTHONPATH to the project root in the terminal where we want to execute the 
# file as a script, without setting the project root, the absolute path import will
# not work. This is because Python will ønot start looking at the top level module
# since current file is in a folder inside the top level module, and by default
# only the current file's upper directory is included in PYTHONPATH, and is sys os path
# Many editors like PyCharm set it by default and hence you do not have to do it
# separately
# Relative imports only work with from ... import ... (syntax)
# Ex: from .common import find
# Absolute Imports are always preferred
def save_to_file(content):
	with open('file_to_save.txt', 'w') as file:
		file.write(content)
	with open('file_to_save.txt', 'r') as file:
		print(file.readlines())
  
print(f'File Operations :: {__name__}')