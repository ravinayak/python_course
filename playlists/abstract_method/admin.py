from playlists.abstract_method.user import User
from playlists.abstract_method.saveable import Saveable

class Admin(User, Saveable):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.access = 'admin'
  
	def __repr__(self):
		return f'Username :: {self.username}, Password :: {self.password}, Access :: admin'
  
	def to_dict(self):
		return(
			{
				'username': self.username,
				'password': self.password,
				'level': 'admin'
			}
		)