def main():
  a = input("What is the Answer to the Great Question of Life, the Universe, the Everything?").strip().lower()
  result = answer(a)
  print (result)

def answer(a):
  if a in ["42" ,"forty-two" , "forty two"]:
  #if a == "42" or a == "forty-two" or a == "forty two"
    return "Yes"
  else:
   return "No"

main()