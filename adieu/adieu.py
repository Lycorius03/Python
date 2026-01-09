import inflect

names_list = [] 
while True:
  try:
    f = inflect.engine()
    user_input = input("Name: ")
    if user_input and len(user_input):
      names_list.append(user_input.strip())

  except EOFError:
    print()
    break

if names_list:
    Output = f.join(names_list)
    print(f"Adieu, adieu, to {Output}")