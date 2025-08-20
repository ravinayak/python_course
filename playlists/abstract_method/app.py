from playlists.abstract_method.user import User
from playlists.abstract_method.database import Database
from playlists.abstract_method.admin import Admin

MENU_CHOICE = '''
	1. Enter username/password for user to add users
	2. Find user/admin given username
	3. Enter username/password for admin to add admin
	4. Remove user/admin given username
	5. Return all users
	6. Exit :: '''

def main():
	cond = True
	while cond:
		user_input = int(input(MENU_CHOICE))

		if user_input == 6:
			cond = False

		if user_input == 1:
			username = input('Please Enter username :: ')
			password = input('Please Enter password :: ')
			user = User(username, password)
			Database.save(user)
		elif user_input == 2:
			username = input('Please Enter username :: ')
			user = User(username, None)
			print(f'Users :: {Database.find(lambda user: user.username == username)}')
		elif user_input == 3:
			username = input('Please Enter username :: ')
			password = input('Please Enter password :: ')
			admin = Admin(username, password)
			Database.save(admin)
		elif user_input == 4:
			username = input('Please Enter username :: ')
			user = User(username, None)
			Database.remove(lambda user: user.username == username)
			print(f'User Removed :: {user}')
		elif user_input == 5:
			print(Database.users)
        
if __name__ == '__main__':
    main()