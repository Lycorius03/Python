import sys
import csv
from tabulate import tabulate

def main():
  chcek_command_line_arg()

  file_path = sys.argv[1]
  try:
    csv_files = []
    with open(file_path,"r") as file:
      csv_file = csv.DictReader(file)
      for row in csv_file:
        csv_files.append(row)

      print(tabulate(csv_files, headers="keys", tablefmt="grid"))

  except FileNotFoundError:
    sys.exit("File does not exist")

def chcek_command_line_arg():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

  if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

if __name__ == "__main__":
  main()