import sys

def main():
  check_command_line_arg()

  try:
    file_path = sys.argv[1]
    with open(file_path,"r") as file:
      lines = file.readlines()
    
    count = 0
    for line in lines:
      stripped_line = line.strip()

      if not stripped_line:
        continue
      if stripped_line.startswith('#'):
        continue
      count += 1

    print(count)

  except FileNotFoundError:
    sys.exit("File does not exsit")

def check_command_line_arg():
  if len(sys.argv) < 2:
    sys.exit("Too few command_line argumnets")
  elif len(sys.argv) > 2:
    sys.exit("Too many command_line agruments")
  if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file") 

if __name__ == "__main__":
   main()