import unittest.mock as mock
import users
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

# Why the full path 'users.get_users_from_db'?
# The error "TypeError: Need a valid target to patch. If you supply only: 
# 		'get_users_from_db'" you will get the following error:
# tests/test_users.py:13: in <module>
#     @mock.patch('get_users_from_db')
# /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1782: in patch
#     getter, attribute = _get_target(target)
# /Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/unittest/mock.py:1624: in _get_target
#     raise TypeError(
# E   TypeError: Need a valid target to patch. You supplied: 'get_users_from_db'
# ========================================================================= short test summary info ==========================================================================
# ERROR tests/test_users.py - TypeError: Need a valid target to patch. You supplied: 'get_users_from_db'
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ============================================================================= 1 error in 0.12s 

# This error arises because mock.patch couldn't locate the target we specified
# as a string.
# When using mock.patch with a string, it expects a fully qualified
# name, which includes the module where the function is defined.

# To fix this, you need to provide the full path to the get_users_from_db
# function. Assuming get_users_from_db is defined in users.py
@mock.patch('users.get_users_from_db')
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
