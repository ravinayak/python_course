class Admin:
    content = { 'users': [] }
    
    @classmethod
    def insert(cls, data):
        for user in data:
            cls.content['users'].append(user)
    
    @classmethod
    def remove(cls, finder):
        cls.content['users'] = [ user for user in cls.content['users'] if not finder(user)]
        
    @classmethod
    def find(cls, finder):
        return [user for user in cls.content['users'] if finder(user)]
    
a = Admin()
data = [
    		{ 'username': 'Jack' }, 
      		{ 'username': 'Raj' }, 
        	{ 'username': 'Ron' }, 
         	{ 'username': 'Abishek' }, 
          	{ 'username': 'Sham' }
]

a.insert(data)

print(a.content)
finder = lambda x: x['username'] == 'Raj'
a.remove(finder)
print(a.content)