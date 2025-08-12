import module_import_sys_path_python_path.module_import.file_operations as file_operations
import sys

file_operations.save_to_file('Hello World!')
print(f'Sys Path :: {sys.path}')
print(__name__)