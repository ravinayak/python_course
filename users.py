import requests

database = {
	1: 'Sam',
	2: 'Johnson',
	3: 'Rock',
	4: 'Marvin'
}

def get_users_from_db(user_id):
    return database.get(user_id)

def get_users_from_typicode():
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.HTTPError
    return response.json()