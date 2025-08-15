import re

def regex_ex():
    price = 'Price: $18,235.50'
    pattern = r'Price: \$(\d+[,]*\d+\.\d+)'
    psearch = re.search(pattern, price)
    print('Groups :: ', psearch.groups())
    print(f'Groups :: {psearch.groups()[0]}, Group :: {psearch.group(0)} -- {psearch.group(1)}')
    pr_matched = psearch.group(1).replace(',','')
    print(f'Price :: {float(pr_matched)}')
    pfind_all = re.findall(pattern, price)
    print(f'Price :: {float(pfind_all[0].replace(',', ''))}')

def greet(func):
    print('Invoking Func')
    func()
    print('Invoked Func')
    
def finder(movies, finder_fun):
    found = []
    for movie in movies:
        if finder_fun(movie):
            found.append(movie)
            
    return found or 'No Movie Found'
    
def higher_order():
    movies = [
		{
			'name': 'The Matrix', 'director': 'Keanu Reeves',
		},
		{
			'name': 'The Godfather', 'director': 'Anurag Kashyap'
		},
		{
			'name': 'Baby Driver', 'director': 'Aamir'
		}
	]
    property_input = input('Enter the property on which you want to search :: ')
    property_val = input('Enter the value of this property :: ')

    finder_fun = lambda x: x[property_input] == property_val
    print(finder(movies, finder_fun))
    
if __name__ == '__main__':  
	regex_ex()
	greet(lambda: print('lambda function defined'))
	higher_order()