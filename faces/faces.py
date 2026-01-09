def main():
  user_input = input()
  user_output = convert(user_input)
  print(user_output)

def convert(text):
  faces = text.replace(":)","🙂")
  faces = faces.replace(":(","☹️")
  # print(text)
  return faces

main()