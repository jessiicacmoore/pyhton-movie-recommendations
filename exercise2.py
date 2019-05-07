# ----- Store reccomendations -----
documentary = 'Blackfish'
dramedy = 'Almost Famous'
drama = 'A Quiet Place'
comedy = 'The Hangover'
book = 'The book \'Harry Potter\''

# ----- Retrieve movie preferences from user -----
print("What do you rate your liking of documentaries on a scale of 1 to 5?")
documentary_rating = int(input())

print("What do you rate your liking of dramas on a scale of 1 to 5?")
drama_rating = int(input())

print("What do you rate your liking of comedies on a scale of 1 to 5?")
comedy_rating = int(input())


# ----- Select a recommendation -----
def recommendation():
  if documentary_rating >= 4:
    return documentary

  elif drama_rating >= 4 and comedy_rating >= 4:
    return dramedy

  elif drama_rating >= 4:
    return drama
  
  elif comedy_rating >=4:
    return comedy

  else:
    return book

# ----- Make the recommendation to the user -----
def make_recommendations():
  print() 
  print("-------------------------------")
  print()
  
  print("I recommend:")
  print(f"- {recommendation()}")

  print()
  print("-------------------------------")
  print()


# ----- Call the function to print recommendation to the user -----
make_recommendations()