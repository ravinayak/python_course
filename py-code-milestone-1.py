menu_str = ''' Please Enter one of the choices (a, b, c): 
	a. Enter Movie Name to store
	b. Search for a Movie (Case Insensitive)
	c. Delete a Movie (Case Insensitive)
	d. Press q to quit
'''
print(menu_str)
movies = []

def repeat_input():
  incorrect_input = True
  while incorrect_input:
    user_input = input('Enter your choice :: ').lower()
    for menu_input in ['a', 'b', 'c', 'q']:
      if user_input == menu_input:
        incorrect_input = False
  return user_input

def add_movie(movie_name):
	movies.append(movie_name)
	print(f'Movie added')
	print(f'Current Movies :: {movies}')
 
def search_movie(movie_name):
  print(f'Current Movies :: {movies}')
  for movie in movies:
    if movie.lower() == movie_name.lower():
      return f'Movie exists :: {movie}'
  return 'Movie does not exist'

def delete_movie(movie_name):
  for movie in movies:
    if movie.lower() == movie_name.lower():
      movies.remove(movie)
      print(f'Movie deleted :: {movie}')
      print(f'Current Movies :: {movies}')

def process_user_input(user_input):
  if user_input == 'q':
    return print('Good Luck')

  movie_name = input('Enter Movie Name: ')
  if user_input == 'a':
    add_movie(movie_name)
  elif user_input == 'b':
    print(search_movie(movie_name))
  else:
    delete_movie(movie_name)

user_input = ''
while user_input != 'q':
  user_input = repeat_input()
  process_user_input(user_input)
  