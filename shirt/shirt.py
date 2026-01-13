import sys
import os
from PIL import Image,ImageOps

def main():
  check_command_line()

  input_path = sys.argv[1]
  output_path = sys.argv[2]
  
  try:
    with Image.open("shirt.png") as shirt:
      pass
    
      with Image.open(input_path) as input_img:
        size = shirt.size
        cropped_img = ImageOps.fit(input_img,size)

        cropped_img.paste(shirt,shirt)
        cropped_img.save(f"{output_path}")

  except FileNotFoundError:
    sys.exit("Inout does not exist")

def check_command_line():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

  ex1 = os.path.splitext(sys.argv[1])[1].lower()
  ex2 = os.path.splitext(sys.argv[2])[1].lower()
  valid_extensions = [".jpg", ".jpeg", ".png"]

  if ex1 not in valid_extensions:
    sys.exit("Invalid input")
  if ex2 not in valid_extensions:
    sys.exit("Invalid output")

  if ex1 != ex2:
    sys.exit("Input and output have different extensions")

if __name__ == "__main__":
  main()