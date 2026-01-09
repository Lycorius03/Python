import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
available_fonts = figlet.getFonts()

if len(sys.argv) == 1:
  font_name = random.choice(available_fonts)

elif len(sys.argv) == 3:
  is_flag_correct = sys.argv[1] in ["-f", "--font"]
  is_font_valid = sys.argv[2] in available_fonts

  if is_flag_correct and is_font_valid:
    font_name = sys.argv[2]

  else:
    sys.exit("Invalid usage")

else:
  sys.exit("Invalid usage")

user_input = input("Input: ")

figlet.setFont(font = font_name)
print(f"Output: {figlet.renderText(user_input)}")