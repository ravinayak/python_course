#!/usr/bin/env python3
import os
import sys

print("=== Checking PYTHONPATH Environment Variable ===")

# Check if PYTHONPATH is set
pythonpath = os.environ.get('PYTHONPATH')

if pythonpath:
    print(f"✓ PYTHONPATH is set: {pythonpath}")
    print(f"Type: {type(pythonpath)}")
    
    # Split by path separator to see individual paths
    if os.name == 'nt':  # Windows
        paths = pythonpath.split(';')
    else:  # Unix/Linux/macOS
        paths = pythonpath.split(':')
    
    print(f"Individual paths in PYTHONPATH:")
    for i, path in enumerate(paths):
        print(f"  {i}: {repr(path)}")
else:
    print("✗ PYTHONPATH is not set")

print("\n=== Current sys.path ===")
print("sys.path contents:")
for i, path in enumerate(sys.path):
    print(f"{i}: {repr(path)}")

print("\n=== Analysis ===")
if pythonpath:
    print("PYTHONPATH being set might explain why '' is not in sys.path")
    print("When PYTHONPATH is set, it can override the default behavior")
    print("and prevent the current directory from being added to sys.path")
else:
    print("PYTHONPATH is not set, so the absence of '' in sys.path")
    print("might be due to other factors (Python version, startup flags, etc.)")

print("\n=== Environment Variables Related to Python ===")
python_related_vars = [
    'PYTHONPATH',
    'PYTHONHOME', 
    'PYTHONSTARTUP',
    'PYTHONUNBUFFERED',
    'PYTHONHASHSEED'
]

for var in python_related_vars:
    value = os.environ.get(var)
    if value:
        print(f"{var}: {value}")
    else:
        print(f"{var}: Not set") 