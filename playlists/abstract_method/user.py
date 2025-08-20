from playlists.abstract_method.saveable import Saveable

class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return f'Username :: {self.username}, Password :: {self.password}'
        
    def to_dict(self):
        return (
			{
				'username': self.username,
				'password': self.password,
			}
		)
        
    