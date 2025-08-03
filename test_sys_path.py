#!/usr/bin/env python3
import sys
import os

print("=== Python Module Search Path (sys.path) ===")
print(f"Current working directory: {os.getcwd()}")
print(f"sys.path length: {len(sys.path)}")
print()

print("sys.path contents:")
for i, path in enumerate(sys.path):
    print(f"{i}: {repr(path)}")
print()

# Check if empty string is in sys.path
if '' in sys.path:
    empty_string_index = sys.path.index('')
    print(f"✓ Empty string '' found at index {empty_string_index}")
    print("This represents the current working directory")
else:
    print("✗ Empty string '' not found in sys.path")

print("\n=== How this affects imports ===")
print("When you import a module, Python searches in this order:")
print("1. Current directory (represented by '')")
print("2. PYTHONPATH environment variable directories")
print("3. Standard library directories")
print("4. Site-packages directories")

print("\n=== Example ===")
print("If you have a file 'my_module.py' in current directory:")
print("import my_module  # This will find my_module.py in current directory")
print("Because '' (current directory) is first in sys.path")


print("=== Detailed sys.path Investigation ===")
print(f"Current working directory: {os.getcwd()}")
print(f"sys.path length: {len(sys.path)}")
print()

print("sys.path contents:")
for i, path in enumerate(sys.path):
    print(f"{i}: {repr(path)}")
print()

# Check for empty string
if '' in sys.path:
    empty_string_index = sys.path.index('')
    print(f"✓ Empty string '' found at index {empty_string_index}")
else:
    print("✗ Empty string '' not found in sys.path")

print("\n=== Possible Reasons ===")
print("1. Python was started with -S flag (suppresses site module)")
print("2. PYTHONPATH environment variable is set")
print("3. Running from a different context (IDE, virtual environment, etc.)")
print("4. Python version or platform differences")

print("\n=== Testing import behavior ===")
print("Let's test if we can still import from current directory:")

# Create a simple test module
test_module_content = '''
def test_function():
    return "Hello from test module"
'''
with open('test_module.py', 'w') as f:
    f.write(test_module_content)

try:
    import test_module
    print("✓ Successfully imported test_module")
    print(f"test_module.test_function(): {test_module.test_function()}")
except ImportError as e:
    print(f"✗ Failed to import test_module: {e}")

# Clean up
import os
if os.path.exists('test_module.py'):
    os.remove('test_module.py')

print("\n=== Key Point ===")
print("Even if '' is not in sys.path, Python may still be able to")
print("import from the current directory through other mechanisms.") 