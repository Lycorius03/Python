def main():
  greetings = input("Greeting:")
  money = determine(greetings)
  print(money)

def determine(Greetings):
  Greetings = Greetings.strip().lower()
  if Greetings.startswith('hello'):
    return '0$'
  elif Greetings.startswith('h'):
    return '20$'
  else:
    return '100$'


main()