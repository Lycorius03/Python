def main():
  expression = input("Expression: ").strip()
  result = interpreter(expression)
  print(f"{result:.1f}")

def interpreter(expression):
  x, y, z = expression.split(" ")
#Turn the numeric part into an interger
  x = int(x)
  z = int(z)
#inpterpreter
  if  y == "+":
    return float(x + z)
  elif y == "-":
    return float(x - z)
  elif y == "*":
    return float(x * z)
  elif y == "/":
    return float(x / z)

main()