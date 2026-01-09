def main():
  camelCase = input("camelCase: ")
  result = convert(camelCase)
  print(f"snake_name: {result}")

def convert(camelCase):
  snake_str = ""
  for n in camelCase:
    if n.isupper():
      snake_str += f"_{n.lower()}"
    else:
      snake_str += n
  return snake_str

main()
