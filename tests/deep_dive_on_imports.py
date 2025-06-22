# The Deep Dive: Packages, __name__, and the "Anchor" for Relative Imports
# At the heart of this issue are three concepts:

# 	1. How Python defines a "package."
# 	2. How a file knows its own name and location (__name__).
# 	3. How that name acts as an "anchor" for relative imports.

# 1. What is a package in Python?
# When you hear "package" in Python, it's easy to just think of it as a folder
# containing Python files. While that's part of it, the concept is richer,
# and understanding the "dotted path" is key to grasping how Python manages
# larger, more organized codebases.

# Let's break down why a package is more than just a directory and what the
# "dotted path" signifies:

# Beyond Just a Directory: The Essence of a Python Package
# Logical Grouping: Imagine a large application. You might have separate
# functionalities like user authentication, data processing, reporting,
# and a UI. If all your Python files were just in one flat directory, it
# would quickly become a chaotic mess. Packages provide a way to logically
# group related modules (Python files) and sub-packages
# (sub-directories acting as packages). This improves readability, maintainability,
# and reusability.

# Namespace Management: One of the most critical roles of packages is to help
# manage namespaces. In Python, every module has its own namespace. When you
# import a module, its contents become available in the importing module's
# namespace. Without packages, if two different files (modules) happened to
# have a function or variable with the same name, they would clash. Packages
# provide a hierarchical structure that effectively creates unique "paths" to
# these names.

# The __init__.py File (Historically Essential):

# Prior to Python 3.3: The presence of an __init__.py file within a directory was
# absolutely mandatory for Python to recognize that directory as a package. This
# file could be empty, or it could contain initialization code for the package
# (e.g., defining __all__, setting up package-level variables, or importing commonly
# used modules into the package's namespace).
# From Python 3.3 onwards (Implicit Namespace Packages): The requirement for
# __init__.py was relaxed with the introduction of "implicit namespace packages."
# A directory can now be recognized as a package even without an __init__.py file.
# This is particularly useful for distributing collections of related code that
# don't necessarily need shared initialization or a single top-level package.
# However, for most traditional applications and libraries, using __init__.py
# is still common practice as it clearly defines the package boundary and allows
# for explicit initialization.
# The "Dotted Path": my_app.components.utils
# The "dotted path" is the core mechanism by which Python identifies and locates
# modules and sub-packages within a package hierarchy. It's similar to a file path
# but uses dots (.) instead of slashes (/ or \) to denote directory separation.

# Let's break down my_app.components.utils:

# my_app (Top-Level Package): This is typically the root directory of your application
# or library. For Python to find it, my_app must be discoverable on Python's module
# search path (sys.path). When you import my_app, Python looks for a directory named
# my_app in the locations listed in sys.path.

# components (Sub-Package within my_app): Once my_app is found, Python then looks inside
# the my_app directory for a sub-directory named components. This components directory is
# treated as a sub-package of my_app.

# utils (Module within components): Finally, Python looks inside the components directory
# for a Python file named utils.py. When you perform from my_app.components import utils,
# Python loads the utils.py module.

# How Python Uses the Dotted Path:

# Hierarchical Import: When you write import my_app.components.utils, Python performs
# the following steps:

# It first tries to find my_app on sys.path.
# Once my_app is located, it then treats my_app as a package and looks for components
# within it. Finally, it looks for utils.py within components.


# Absolute vs. Relative Imports:

# Absolute Imports: import my_app.components.utils is an absolute import. It always
# starts from a top-level package that's on sys.path. This makes it clear where the
# module is coming from and reduces ambiguity.
# Relative Imports: If you are inside a module within my_app.components
# (say, my_app.components.some_module), you could use a relative import to
# import utils: from . import utils or from .. import components. Relative imports
# are useful for keeping imports concise within a package but can sometimes be less
# clear about the exact location of the imported module for someone unfamiliar with
# the codebase.
# sys.path and Discoverability: For Python to "see" a top-level package like my_app,
# the directory containing my_app must be included in sys.path. This is why you often
# set up virtual environments, use pip install -e . (editable install), or manually 
# add paths to sys.path when developing applications.

# In Summary:

# A Python package is more than just a collection of files in a folder. It's a structured
# organization system that:

# Provides logical grouping for related code.
# Manages namespaces to prevent naming conflicts.
# Enables hierarchical imports through the "dotted path" mechanism.
# Facilitates code reusability and maintainability in larger projects.
# The "dotted path" is the precise address Python uses to navigate this hierarchical
# structure, allowing you to access specific modules and sub-packages within your application.

# 2. How does python know a directory is a package?
# Python has evolved in how it recognizes a directory as a package. Here's a 
# breakdown:

# 1. The Traditional Way (Pre-Python 3.3): The __init__.py File
# Historically, the primary way Python determined if a directory was a package
# was the presence of a special file named __init__.py (that's two underscores
# before and after "init", then .py).

# Marker: If a directory contained an __init__.py file, Python would treat that
# directory as a package.
# Initialization Code: This file could be empty, or it could contain Python code
# that would be executed when the package (or any module within it) was first
# imported. This made __init__.py useful for: 
# Package-level setup: Setting up logging, configuration, or connecting to databases.
# Defining __all__: Explicitly controlling which names (modules, functions, classes)
# are imported when a user uses from package_name import *.
# "Flattening" the package structure: Re-exporting items from submodules to make them
# directly accessible from the package's top level (e.g., from .submodule import
# some_function in __init__.py allows from package import some_function).
# 2. The Modern Way (Python 3.3+): Implicit Namespace Packages (PEP 420)
# With Python 3.3, a new concept called "Implicit Namespace Packages" was introduced
# (defined in PEP 420). This significantly changed how Python recognizes packages:

# No __init__.py Required: A directory no longer needs an __init__.py file to be
# considered a package. If Python finds a directory on its import path that matches
# an import statement (e.g., my_app when you do import my_app), it will treat it as
# a package, even without __init__.py.
# The Power of sys.path: Python looks for packages and modules in the directories
# listed in sys.path. This list typically includes: 
# The current working directory.
# Directories listed in the PYTHONPATH environment variable.
# Standard library directories.
# Site-packages directories (where third-party libraries are installed).

# How it Works with Implicit Namespace Packages:
# When Python encounters an import statement like import my_app.components.utils,
# it starts by looking for my_app in the directories on sys.path.
# If it finds a directory named my_app on sys.path, it then checks for components
# inside it, and finally utils.py inside components.
# If any of these intermediate directories (my_app, components) do not contain an
# __init__.py file, they are treated as implicit namespace packages.
# Use Case for Implicit Namespace Packages: The primary motivation for implicit
# namespace packages is to allow different parts of a single "logical" package to
# be installed in different physical locations on the filesystem, often by different
# distribution packages. For example, a company might release my_company.product_a
# and my_company.product_b as separate installable packages, but both contribute to
# the overall my_company namespace. This is less common for typical application
# development and more for large, distributed library ecosystems.
# Why __init__.py is Still Commonly Used

# Even with implicit namespace packages, the __init__.py file is still widely used for
# "regular" packages because it offers several advantages:

# Clear Package Boundary: It explicitly declares a directory as a package, making the
# project structure clearer for humans and tools.
# Initialization Code: It provides a dedicated place to run code when the package is
# imported, which is often crucial for setting up package-wide configurations, constants,
# or initial imports.
# Controlling from package import *: The __all__ variable defined in __init__.py allows
# developers to control what is exposed when a user imports all names from a package
# using the wildcard *.
# "Flattening" Imports: It allows you to expose submodules or functions/classes from
# submodules directly under the package's top-level namespace, making imports more
# convenient for users (e.g., from mypackage import MyClass instead of from
# mypackage.submodule import MyClass).
# In essence:

# Python 3.3+: Python can know a directory is a package either by the presence of an
# __init__.py file (explicit package) or by simply finding a matching directory on
# sys.path during an import (implicit namespace package).
# Best Practice (for most projects): For most applications and libraries, it's still
# recommended to include an __init__.py file to define a clear, explicit package,
# even if it's empty. This avoids potential ambiguity and allows for easy initialization
# or structure flattening.

# 4. What is a Package to Python?
# A package is more than just a directory. It's a structured collection of modules. 
# For Python to see a directory as a package, it needs to be able to determine a 
# "dotted path" to it, like my_app.components.utils. This allows Python to build
# a hierarchy.

# 5. The __name__ Special Variable
# Every Python module(file and sub-files) has a special variable called __name__.
# This variable is critical because it tells the module its identity within the
# project.

# When a file is run directly: If you execute a file from your terminal
# (python my_app/main.py), Python sets that file's __name__ to the special string 
# "__main__". This signifies "I am the entry point of this program."
# When a file is imported: If main.py instead does import my_app.utils, then inside
# the utils.py file, its __name__ will be the string "my_app.utils".
# 3. The "Anchor" for Relative Imports
# A relative import (. or ..) is a command that says, "start from my own location
# and navigate from there." Python uses the module's __name__ as the map and anchor
# for this navigation.

# Let's imagine test_shapes.py is inside a proper package, and its __name__ is
# "python_course.tests.test_shapes".

# from . import sibling: Python looks at the __name__, lops off the last part
# (test_shapes), and gets python_course.tests. It then appends sibling, resulting
# in an import of python_course.tests.sibling.
# from .. import parent_sibling: Python looks at the __name__, lops off the last
# two parts (tests.test_shapes), and gets python_course. It then appends parent_sibling,
# resulting in an import of python_course.parent_sibling.

# Why It Fails with pytest
# Now, let's connect this to your situation.

# pytest Runs Your Test File: When you run pytest, it discovers tests/test_shapes.py.
# It does not import it as python_course.tests.test_shapes. Instead, for all intents and
# purposes, it runs it as a top-level script.
# __name__ is Not a Dotted Path: Because it's run like a script, the __name__ inside
# test_shapes.py is not a dotted path. It doesn't contain the package information.
# The Anchor is Missing: When the line from ..shapes import ... is executed, Python
# looks at the __name__ to figure out where it is. Since the name has no dots, it has
# no concept of a "parent package." It can't go "up one level" (..) because there's no
# "level" to go up from.
# This is precisely what the error message means: ImportError: attempted relative import
# with no known parent package. Python is telling you, "You asked me to go up, but I
# don't know where I am in a package, so I don't know what 'up' means."

# The Solution: Absolute Imports and a Clean Structure
# The solution you identified is the industry standard.

# pytest Helps You: pytest adds your project's root directory
# (/Users/ravikumarnayak/personal_projects/python/python_course/)
# to sys.path (Python's list of places to look for modules).
# Use Absolute Imports: Because the root is in the path, you can use a simple,
# direct absolute import: from shapes import Rectangle, Square.
# How it Works: Python sees this absolute import, searches sys.path, finds your
# project root, and looks inside. It sees shapes.py right there and imports it
# successfully. No relative navigation is needed.


# 7. pipenv shell:
# pipenv shell (and dependency managers like it, such as Poetry) solves the sys.path
# and discoverability problem by leveraging virtual environments in a more streamlined
# and automated way.

# Here's a breakdown of how it works:

# 1. Automated Virtual Environment Creation
# Isolation: When you run pipenv install in a project directory for the first time,
# pipenv automatically creates a dedicated virtual environment for that project. This
# virtual environment is a self-contained directory that includes:
# A copy of the Python interpreter (selected based on your Pipfile or specified by you).
# Its own site-packages directory, where all project-specific dependencies are installed.
# Default Location: By default, pipenv places these virtual environments in a centralized
# location
# (e.g., ~/.local/share/virtualenvs/ on Linux/macOS or %USERPROFILE%\.virtualenvs\ on Windows).
# This keeps your project directories clean.
# Project-Specific Venv (Optional): You can also configure pipenv to create the virtual
# environment directly inside your project directory (e.g., in a .venv folder) by setting
# the PIPENV_VENV_IN_PROJECT=1 environment variable. This can be convenient for some
# workflows, especially if you want to keep everything for a project self-contained.
# 2. Modifying sys.path When You Enter the Shell
# pipenv shell's Role: When you execute pipenv shell, pipenv does more than just spawn a
# new shell. It intelligently modifies the environment variables of that new shell session,
# most critically the PATH environment variable.
# Prepend Virtual Environment Bins: pipenv shell prepends the bin (or Scripts on Windows)
# directory of your project's virtual environment to your shell's PATH.
# How sys.path is Affected: Because the virtual environment's bin directory is now at the
# beginning of your PATH, when you run python or pip within that pipenv shell session,
# your system's shell will find the virtual environment's Python interpreter and its
# associated pip first.
# When the virtual environment's Python interpreter starts, it automatically sets up
# its sys.path to include:
# The standard library.
# The virtual environment's own site-packages directory (where pipenv installed your
# project's dependencies).
# Crucially, the directory where your Pipfile (and thus your top-level project code)
# resides. This is often done implicitly or through an "editable install"
# (pipenv install -e . or similar under the hood for the project itself)
# which places a .pth file in the virtual environment's site-packages that
# points back to your project's root.
# 3. Benefits for Discoverability
# By doing all of this, pipenv shell solves the sys.path and discoverability problem in
# the following ways:

# Automatic Inclusion of Project Root: When you are inside the pipenv shell, Python's
# sys.path is automatically configured to include your project's root directory. This
# means your top-level packages (like my_app in your example) are immediately discoverable
# without any manual PYTHONPATH manipulation. You can directly import my_app or from
# my_app.components import utils.
# Isolation of Dependencies: Each project gets its own isolated set of dependencies.
# This prevents "dependency hell" where different projects require different versions
# of the same library, which would clash if installed globally. sys.path within one
# pipenv shell is only aware of that project's specific dependencies.
# Reproducible Environments: The Pipfile and Pipfile.lock files ensure that anyone working
# on the project can create an identical virtual environment with the exact same
# dependencies and versions, leading to more consistent development and deployment.
# Simplified Workflow: You don't have to manually activate virtual environments, remember
# their paths, or mess with PYTHONPATH directly. pipenv shell handles all that for you
# with a single command.
# In essence, pipenv shell acts as a convenient wrapper around the underlying virtual
# environment mechanism. It ensures that when you're working on a specific project,
# the Python interpreter and its sys.path are correctly configured to "see" your
# project's code and its specific dependencies, all without manual intervention

# 8. Executing a python script directly:
# Running a script vs importing a module are treated differently by Python:
# Script execution: Python adds the script's directory to the path, if the
# script is importing anyting from the current directory, the script execution will
# work.
# If the script is importing from a directory other than the current directory
# the execution will not work
# Python's module search is based on the script's location, not the current working director

# 9. python -m 
# What python -m Does
# The -m flag tells Python to:
# Find a module in the Python path
# Execute it as the __main__ module
# Set up the module's package context properly
# Key Differences from Direct Script Execution
# 1. Package Context
# When you run python -m module_name, Python:
# Treats the module as part of its package
# Sets up proper package imports
# Maintains the package hierarchy
# 2. Module Discovery
# python script.py - looks for the file directly
# python -m module_name - searches sys.path for the module

# 10. python -m tests.test_shapes
# How Python Finds the tests Package
# 1. Current Working Directory is in sys.path
# When you run python -m tests.test_shapes from the python_course directory:
# 	python -m tests.test_shapes
# Python's sys.path includes the current working directory (as the empty string ''), so Python can find:
# /Users/ravikumarnayak/personal_projects/python/python_course/ ✅

# 2. Python Looks for Package Structure
# Python searches sys.path for a directory named tests that contains an __init__.py file:

# python_course/
# ├── __init__.py          # Makes python_course a package
# ├── tests/               # Directory
# │   ├── __init__.py      # Makes tests a package ← Python finds this!
# │   └── test_shapes.py   # Module inside tests package
# └── shapes.py            # Module in parent directory

# 3. The Search Process
# # Python's search process:
# sys.path = ['', '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12', ...]

# Python looks for 'tests' package in each sys.path entry:
# 1. Look in '' (current directory): /Users/.../python_course/
#    - Found: tests/ directory with __init__.py ✅
# 2. Look in other sys.path entries (standard library, etc.)
#    - No 'tests' package found there
# 3. Even without __init__.py it works because of implicit package
# Implicit Packages (Python 3.3+)
# Since Python 3.3, Python introduced the concept of implicit packages (also called namespace packages). This means:
# 1. No __init__.py Required
# Directories can be treated as packages without __init__.py
# Python 3.3+ automatically recognizes directories as potential packages
# This is called implicit package discovery
# 2. How It Works
# # Even without __init__.py, this works:
# python -m tests.test_shapes
# Python can find the tests directory and treat it as a package because:
# The directory exists in sys.path
# Python 3.3+ doesn't require __init__.py for basic package functionality
# The -m flag can resolve the module path
# 3. When __init__.py is Still Needed
# __init__.py is still required for:
# Traditional package imports: import tests.something
# Package initialization: Running code when the package is imported
# Explicit package markers: Making it clear this is a package
# Backward compatibility: Some tools still expect it

# 11. pytest -m vs python -m
# python -m: Runs a module as a script
# pytest -m: Runs tests with specific markers (like @pytest.mark.slow)


