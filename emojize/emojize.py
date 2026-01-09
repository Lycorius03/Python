from emoji import emojize

user_input = input("Input: ")
print(emojize(f"{user_input}", language = 'alias'))