# ----- Retrieve movie preferences from user -----
print("Do you like documentaries?")
likes_documentaries = input()

print("Do you like dramas?")
likes_dramas = input()

print("Do you like comedies?")
likes_comedies = input()


# ----- Pick a movie to reccomend -----
def reccomendation():
  if likes_documentaries.lower() == 'yes':
    return "The documentary 'Blackfish'"

  elif likes_dramas.lower() == 'yes' and likes_comedies.lower() == 'yes':
    return "The dramedy 'Almost Famous'"

  elif likes_dramas.lower() == 'yes':
    return "The drama 'A Quiet Place'"

  elif likes_comedies.lower() == 'yes':
    return "The comedy 'The Hangover'"

  else:
    return "The book 'Harry Potter'"


# ----- Make the reccomendation to the user -----
def make_reccomendations(movie_preferences):
  print() 
  print("-------------------------------")
  print()
  
  print("I reccomend:")
  print(f"- {reccomendation()}")

  # attempt at making more than one reccomendation
  # for preference in movie_preferences:
  #   print(f"- {reccomendation()}")

  print()
  print("-------------------------------")
  print()

  
movie_preferences = [likes_documentaries, likes_dramas, likes_comedies]
make_reccomendations(movie_preferences)