import random

while True:
  try:
    level = input("Level: ")
    n = int(level)
    num = random.randint(1,n)
    num = int(num)
    break

  except (ValueError, TypeError):
    pass

while True:
  try:
    user_guess = input("Guess: ")
    user_guess = int(user_guess)
    if user_guess <= 0:
      continue

    if user_guess < num:
      print("Too small!")
    elif user_guess > num:
      print("Too large!")
    else:
      print("Just right!")
      break

  except (ValueError, TypeError):
    pass