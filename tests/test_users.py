import unittest.mock as mock
import playlists.users as users
import pytest
from requests import HTTPError

# When we patch 'get_users_from_db', we are mocking the method
# This method is mocked and the mocked object for this method
# is passed to the test_<method> as the parameter in the method
# This is a mocked object for the method, and hence like any
# method, it must have a return value, because we shall be asserting
# on the return value of the method
# Hence we assign the return_value of the mocked object to a value
# which we assert on

# Why the full path 'playlists.users.get_users_from_db'?
# ➜  python_course  source /Users/ravikumarnayak/.local/share/virtualenvs/python_course-y0ZEJACr/bin/activate
# (python_course) ➜  python_course git:(development) ✗ PYTHONPATH=. pytest tests/test_users.py
# =========================================================================== test session starts ============================================================================
# platform darwin -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
# rootdir: /Users/ravikumarnayak/personal_projects/python/python_course
# configfile: pytest.ini
# collected 3 items                                                                                                                                                          

# tests/test_users.py F..                                                                                                                                              [100%]

# ================================================================================= FAILURES =================================================================================
# __________________________________________________________________________ test_get_users_from_db __________________________________________________________________________

# args = (), keywargs = {}

#     @wraps(func)
#     def patched(*args, **keywargs):
# >       with self.decoration_helper(patched,
#                                     args,
#                                     keywargs) as (newargs, newkeywargs):

# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/unittest/mock.py:1423: 
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/contextlib.py:141: in __enter__
#     return next(self.gen)
#            ^^^^^^^^^^^^^^
# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/unittest/mock.py:1405: in decoration_helper
#     arg = exit_stack.enter_context(patching)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/contextlib.py:530: in enter_context
#     result = _enter(cm)
#              ^^^^^^^^^^
# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/unittest/mock.py:1481: in __enter__
#     self.target = self.getter()
#                   ^^^^^^^^^^^^^
# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/pkgutil.py:513: in resolve_name
#     mod = importlib.import_module(modname)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

# name = 'users', package = None

#     def import_module(name, package=None):
#         """Import a module.
    
#         The 'package' argument is required when performing a relative import. It
#         specifies the package to use as the anchor point from which to resolve the
#         relative import to an absolute import.
    
#         """
#         level = 0
#         if name.startswith('.'):
#             if not package:
#                 raise TypeError("the 'package' argument is required to perform a "
#                                 f"relative import for {name!r}")
#             for character in name:
#                 if character != '.':
#                     break
#                 level += 1
# >       return _bootstrap._gcd_import(name[level:], package, level)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# E       ModuleNotFoundError: No module named 'users'

# /opt/homebrew/Cellar/python@3.13/3.13.5/Frameworks/Python.framework/Versions/3.13/lib/python3.13/importlib/__init__.py:88: ModuleNotFoundError
# ========================================================================= short test summary info ==========================================================================
# FAILED tests/test_users.py::test_get_users_from_db - ModuleNotFoundError: No module named 'users'
# ======================================================================= 1 failed, 2 passed in 0.39s ========================================================================

# To fix this, you need to provide the full path to the get_users_from_db
# function. Assuming get_users_from_db is defined in playlists.users.py

# The error ModuleNotFoundError: No module named 'users' occurs because mock.patch is
# trying to find a top-level module named users in your project's path, but it doesn't
# exist there.

# Your Project Structure: Your get_users_from_db function is located in the file
# /Users/ravikumarnayak/personal_projects/python/python_course/playlists/users.py.
# How Pytest Sees Your Project: When you run pytest, it adds your project's root
# directory (python_course) to Python's search path (sys.path).
# The mock.patch Target: The string you provide to @mock.patch must be the full,
# importable path to the object from the project root.
# In your test file, you are correctly importing the module as import
# playlists.users as users. The mock.patch decorator needs to use this same
# "full path" logic.
@mock.patch('playlists.users.get_users_from_db')
def test_get_users_from_db(mocked_test_user_from_db):
    mocked_test_user_from_db.return_value = 'Alice'
    username = users.get_users_from_db(1)
    assert username == 'Alice'

@mock.patch('requests.get')
def test_get_users_from_typicode(mocked_request_get):
    # This is more preferred than using mock.Mock()
    # 	1. It’s more Pythonic and concise in most unit tests.
	# 	2. It’s also easier for others to understand when reading your test.
	# But if you need custom behavior, or are passing the mock around,
 	# then mock.Mock() gives you flexibility
	# Use Case
	# 			Recommended 							Style
	# -----------------------------------		------------------------------------------
	# 	Simple return mocking					mocked_request_get.return_value ✅
	# 	Complex or reusable mocking				mock.Mock()

    mocked_response = mocked_request_get.return_value
    mocked_response.status_code = 200
    json_output = { 'id': 1, 'name': 'Alice' }
    mocked_response.json.return_value = json_output
    assert users.get_users_from_typicode() == json_output
    
@mock.patch('requests.get')
def test_get_users_from_typicode_exception(mocked_response_get):
    mocked_response = mock.Mock()
    mocked_response.status_code = 400
    with pytest.raises(HTTPError) as exc_info:
        users.get_users_from_typicode()
