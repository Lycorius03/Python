import sys
import csv

def main():
  chcek_command_line_arg()

  data = []
  try:
    with open(sys.argv[1], "r") as before:
      reader = csv.DictReader(before)
      for row in reader:
        last,first = row["name"].split(",")
        data.append({
          "first":first.strip(),
          "last":last.strip(),
          "house":row["house"]
        })

  except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

  #check50 pass
  """  fieldnames =["first","last","house"]
n = len(first)
with open(sys.argv[2], "w", newline="") as after:
  writer = csv.DictWriter(after, fieldnames=fieldnames)
  writer.writeheader()

  writer.writerows(data)"""
  
  #Safer:avoid accidental overwrite but check50 not pass
  try:
    fieldnames =["first","last","house"]
    with open(sys.argv[2], "x", newline="") as after:
      writer = csv.DictWriter(after, fieldnames=fieldnames)
      writer.writeheader()

      writer.writerows(data)
  except FileExistsError:
    sys.exit(F"Error:{sys.argv[2]} already exists!")

def chcek_command_line_arg():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

  if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

if __name__ == "__main__":
  main()