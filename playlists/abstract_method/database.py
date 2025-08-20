class Database:
    users = []
    
    @classmethod
    def save(cls, user):
        cls.users.append(user)
        
    @classmethod # finder = lambda x: x.username == 'Rolf'
    def remove(cls, finder):
        cls.users = [user for user in cls.users if not finder(user)]
    
    @classmethod
    def find(cls, finder):
        return [user for user in cls.users if finder(user)]