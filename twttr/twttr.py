def main():
  user_input = input("Input: ")
  Output = shorten(user_input)
  print(Output)

def shorten(user_input):
  output_str = ""
  for r in user_input:
    if r.lower() not in ['a','e','i','o','u']:          
      output_str += r
  return output_str

if __name__ == "__main__":
  main()