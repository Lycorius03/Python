import sys

def main():
  check_command_line_arg()

  try:
    file_path = sys.argv[1]
    with open(file_path,"r") as file:
      lines = file.readlines()
    
    conut = 0
    for line in lines:
      stripped_line = line.strip()

      if not stripped_line:
        continue
      if stripped_line.startswith('#'):
        continue
      conut += 1

    print(conut)

  except FileExistsError:
    sys.exit("File does not exsit")

def check_command_line_arg():
  if len(sys.argv) < 2:
    sys.exsit("Too few command_line argumnets")
  elif len(sys.argv) > 2:
    sys.exsit("Too many command_line agruments")
  if not sys.argv[1].endswith(".py"):
    sys.exist("Not a Python file") 

if __name__ == "__main__":
  main()