menu_str = '''Please Enter one of the choices (a, b, c): 
	a. Enter Movie Name to store
	b. Search for a Movie (Case Insensitive)
	c. Delete a Movie (Case Insensitive)
	d. Press q to quit'''

print(menu_str)

user_input = ''
movies = []

def get_user_input():
  incorrect_input = True
  while incorrect_input:
    user_input = input("Enter your choice: ").lower()
    for menu_input in ['a', 'b', 'c', 'q']:
      if menu_input == user_input:
        incorrect_input = False
  return user_input

def add_movie(movie):
	movies.append(movie)
	print(f'Movie was added, current movies :: {movies}')
	return movie

def delete_movie(movie):
  for movie_in_list in movies:
    if movie_in_list.lower() == movie.lower():
      movies.remove(movie_in_list)
      print(f'Movie removed, current movies :: {movies}')
      return movie
  print(f'Movie not removed, current movies :: {movies}')
  return None
  

def search_movie(movie):
  for movie_in_list in movies:
    if movie_in_list.lower() == movie.lower():
      print(f'Movie found :: {movie}, current movies :: {movies}')
      return movie
  print(f'Movie not found :: {movie}, current movies :: {movies}')
  return None

def process_user_input(user_input):
  if user_input == 'q':
    print('Have a good day')
    return None
    
  print(f'Current Movies :: {movies}')
  movie = input('Enter movie name :: ')

  if user_input == 'a':
    result_val = add_movie(movie)
  elif user_input == 'b':
    result_val = search_movie(movie)
  else:
    result_val = delete_movie(movie)
    
while user_input != 'q':
  user_input = get_user_input()
  process_user_input(user_input)
  