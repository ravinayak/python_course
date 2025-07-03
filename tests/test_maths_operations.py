import pytest

# from tests.maths_operations import divide, subtract, add, multiply

# The above line gives ModuleNotFoundError when we run pytest from
# root directory - i.e. python_course
# 
# Answer is below:
# The "Why": Absolute Imports vs. Pytest's Path
# 1. The root of the issue lies in the difference between an absolute import
# and how pytest configures Python's search path.

# 2. Pytest's Behavior: When you run pytest from your project's root directory
# (/Users/ravikumarnayak/personal_projects/python/python_course), pytest
# helpfully adds this root directory to Python's sys.path. This is the list
# of directories Python searches when you try to import something.

# 3. Your Import Statement: The line from tests.maths_operations 
# import ... is an absolute import. It tells Python: "Starting from one of the
# top-level directories in sys.path, find a package named tests, and inside it,
# find the maths_operations module."

# 4. The Mismatch: Python starts searching in python_course/. It sees a directory
# named tests/, but it doesn't recognize it as an importable package. For a
# directory to be a package, it typically needs an __init__.py file. Even if you
# added one, you'd be treating your tests folder as a library to be installed, which
# isn't the standard convention. The tests folder is meant to be a container for
# test code, not a package itself.

# 5. Because Python cannot find a top-level package named tests, it raises
# the ModuleNotFoundError.

# 6. Solution: The correct way to import a "sibling" file within the same
# directory is with a relative import: from .maths_operations
# import .... The leading dot (.) tells Python, "Look in the same directory
# as the current file."



# from .maths_operations import divide, subtract, add, multiply
# Even the Above will give an error, though it implements Relative Import
# ImportError: attempted relative import with no known parent package, is the 
# sibling to the ModuleNotFoundError you saw before. 

# 1. Let's dive into what's happening and how to fix your project's structure
# for good.

# 2. The Problem: attempted relative import with no known parent package
# You are seeing this error because of the line: from .maths_operations
# import divide, subtract, add, multiply

# 3. This is a relative import. The leading dot (.) tells Python to look for
# maths_operations.py in the same directory as the current file
# (test_maths_operations.py).

# 4. However, for this to work, Python needs to recognize the containing
# directory (tests/) as part of a "package." When pytest discovers and
# runs your test file,
# it doesn't always treat the tests directory as a package by default, so it
# doesn't know what the "parent package" is. This leads to the ImportError.
# from .maths_operations import divide, subtract, add, multiply

# 5. Possible Solution: While a quick fix would be to add an __init__.py
# file to your tests directory to force it to be treated as a package, this
# is not a good solution. We should move all the application code to main
# repository folder

from playlists.maths_operations import add, multiply, divide, subtract


def test_divide_by_zero_error():
    y = 0
    x = 2
    # This syntax is used to capture a block in which to test for a specific context
    # Here we are testing for a ValueError being raised as we perform a division by 0
    # exc_info: Think of it as a special container that pytest gives you. When the
    # code inside the with block successfully raises the expected ValueError, pytest
    # "catches" that error and puts all of its details into the exc_info container
    # for you to inspect.

	# What's Inside exc_info?
	# The ExceptionInfo object has a few very useful attributes:

	# 1. exc_info.value: This is the most common one you'll use. It holds the actual
 	# exception instance that was raised. By calling str(exc_info.value), you get the
  	# error message string, which is exactly what your test does to verify the message
   	# is correct.
   
	# 2. exc_info.type: This holds the type of the exception (e.g., <class 'ValueError'>)
 
	# 3. exc_info.traceback: This gives you the full traceback object, which is useful
 	# for more advanced debugging or logging scenarios.
  
	# Summary: In short, exc_info is your tool for looking inside the exception to make
 	# sure it's not just the right type of error, but that it also has the right message
  	# or other properties.
   
    with pytest.raises(ValueError) as exc_info:
        divide(x, y)
    # The assertion should be outside the 'with' block to check the captured exception.
    assert str(exc_info.value) == 'Division by 0 is not allowed'

# To capture any output use capsys. Pass capsys as an argument to the method in which 
# we want to test for print statement execution.
# capsys.readouterr() gives us captured object
# captured.out contains the print statement's input
# Always append \n at the end of the statement being asserted for equality, this is because
# print appends \n at the end of the statement

def test_divide(capsys):
    y = 2
    x = 4
    assert divide(x, y) == 2
    
    captured = capsys.readouterr()
    assert captured.out == 'Result of division of x by y is 2.00\n'
    
def test_add():
    x = 3
    y = 2
    assert add(x, y) == 5
    
def test_multiply():
    x = 3.75
    y = 4.25
    # Using pytest.approx is the best practice for comparing floating-point numbers.
    assert multiply(x, y) == pytest.approx(15.94)
    
def test_subtract(capsys):
    x = 4
    y = 2
    assert subtract(x, y) == 2
    
    captured = capsys.readouterr()
    assert(captured.out) == 'Result of x - y is 2.00\n'
    
# Tests marked slow, skip, xfail can be executed individually by using
# cd ~/personal_projects/python_course (root directory of the project)
# PYTHONPATH=. pytest -m slow

# If you execute the following command, it will display a summary of the tests
# which have been skipped, xpassed, 
# PYTHONPATH=. pytest tests/test_maths_operations.py
# python_course git:(development) ✗ PYTHONPATH=. pytest tests/test_maths_operations.py
# =========================================================================== test session starts ============================================================================
# platform darwin -- Python 3.12.1, pytest-7.4.3, pluggy-1.6.0
# rootdir: /Users/ravikumarnayak/personal_projects/python/python_course
# plugins: anyio-4.9.0
# collected 8 items                                                                                                                                                          

# tests/test_maths_operations.py ......sX                                                                                                                              [100%]

# ============================================================================= warnings summary =============================================================================
# tests/test_maths_operations.py:138
#   /Users/ravikumarnayak/personal_projects/python/python_course/tests/test_maths_operations.py:138: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.slow

# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ============================================================ 6 passed, 1 skipped, 1 xpassed, 1 warning in 0.01s =====

# To remove PytestUnknownMarkWarning.

# This warning appears because you're using a custom marker, @pytest.mark.slow,
# that pytest doesn't recognize by default. You can fix this by creating
# a pytest.ini file in the root directory to register the marker
# PYTHONPATH=. pytest -m slow (runs only tests which have been marked as slow,
# skips/deselects every other test)
# PYTHONPATH=. pytest -m 'not slow' (runs all tests except those tests which have
# been marked as slow)
@pytest.mark.slow
def test_subtract_marked_slow(reason = 'to test custom markings'):
    x = 5
    y = 2
    assert subtract(x, y) == 3

# If a test is incomplete, we can skip running/executing this test by marking
# it as skip
@pytest.mark.skip(reason = 'to test skip markings')
def test_add_marked_skip():
    x = 3
    y = 2
    assert add(x, y) == 5
    
# tests which have been marked as xfail will not show as failed with a red dot
# If it fails, it will show as 1 xfailed
# If it passes, it will show as 1 xpassed
@pytest.mark.xfail(reason = 'to test xfail markings')
def test_multiply_marked_xfail():
    x = 3
    y = 2
    assert multiply(x, y) == 5
    
@pytest.mark.parametrize('x, y, expected_result', [(2, 3, 6), (3, 5, 15), (4, 5, 20), (5, 6, 30), (8, 9, 72), (3, 7, 21), (7, 6, 42)])
# Running the test file results in following output
# Parameter tests => 7 parameter sets
# 6 standard tests in the file (not marked anything or parametrized)
# 1 skipped test
# 1 xfail test
# 1 marked as slow
# 6 standard tests + 7 parametrized tests = 13 tests
# 1 skipped
# 1 xfailed
# Total = 13 + 2 = 15
# Total tests in this file except parametrized tests = 8 (including all marked)
# ➜  python_course git:(development) ✗ PYTHONPATH=. pytest tests/test_maths_operations.py
# =========================================================================== test session starts ============================================================================
# platform darwin -- Python 3.12.1, pytest-7.4.3, pluggy-1.6.0
# rootdir: /Users/ravikumarnayak/personal_projects/python/python_course
# configfile: pytest.ini
# plugins: anyio-4.9.0
# collected 15 items                                                                                                                                                         

# tests/test_maths_operations.py ......sx.......                                                                                                                       [100%]

# ================================================================= 13 passed, 1 skipped, 1 xfailed in 0.02s =================================================================
def test_multiply_parametrize(x, y, expected_result):
    assert multiply(x, y) == expected_result
    