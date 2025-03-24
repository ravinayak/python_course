# import module_import.file_operations as fo
# The above line would cause a Circular Import Error if we run file_operations.py as a script
# This would not cause an error if we execute app.py however
# The explanation is as below:
# Here's what actually happens:
# When running app.py:
# Python creates an entry for module_import.file_operations in sys.modules
# Starts executing file_operations.py
# file_operations.py imports find.py
# find.py imports file_operations
# Because file_operations is already in sys.modules, Python uses that existing module object
# Execution continues normally
# When running file_operations.py directly:
# Python creates an entry for file_operations.py in sys.modules
# Starts executing file_operations.py
# Imports find.py
# find.py tries to import file_operations
# Even though file_operations is in sys.modules, it's in a different import context (as a main module)
# This leads to the "partially initialized module" error
# The key isn't about execution order or module-level code - it's about how Python handles the 
# module caching differently when a module is run as __main__ versus imported as a module.

def find_matching_friend(friends, matcher):
	return [friend for friend in friends if matcher(friend)]
 
print(__name__)