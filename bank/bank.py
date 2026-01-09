def main():
  greetings = input("Greeting:").strip().lower()
  money = determine(greetings)
  print(money)

def determine(Greetings):
  if Greetings.startswith('hello'):
    return '0$'
  elif Greetings.startswith('h'):
    return '20$'
  else:
    return '100$'


main()