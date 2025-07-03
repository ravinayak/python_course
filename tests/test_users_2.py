from playlists.users import get_users_from_db
from unittest import mock
from os import sys

# The core principle of mock.patch is: You must patch where an object
# is looked up (used), not where it is defined.
# When we import in the following line:
# from users import get_users_from_db, get_users_from_typicode
# When Python executes this, it finds the get_users_from_db function
# in the users module and creates a reference to it directly within
# the test_users module's namespace.
# The @mock.patch('users.get_users_from_db') decorator successfully
# replaces the function at its original source. However, your test
# is no longer looking at the original source; it's using the local
# reference it imported at the top of the file. That local reference
# still points to the real, un-mocked function.
# To get the correct output in this style of import, we must mock
# the local reference which is being looked up (used)
# Local Reference: test_users_2.get_users_from_db: 
# 		<module_name>.get_users_from_db

# To get output from print, use -s option

print(f'Sys path :: {sys.path}')
@mock.patch('test_users_2.get_users_from_db')
def test_users_get_from_db(mock_get_users_from_db):
    mock_get_users_from_db.return_value = 'Alice'
    assert get_users_from_db(1) == 'Alice'