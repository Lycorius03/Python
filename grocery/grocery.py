def main():
  grocery()

def grocery():
  groceries = []
  gro_list = {}
  while True:
    try:
      item = input().strip().upper()
      if item and len(item) > 0:
        groceries.append(item)

    except EOFError:
      for grocery in groceries:
        gro_list[grocery] = gro_list.get(grocery, 0) + 1
      
      # for k,v in gro_list.items():
      #   print(f"{v} {k}")

      # Note: This step ensures compatibility with Python <3.7.
      # Starting in Python 3.7, dict insertion order is guaranteed by the language specification:
      # new keys are appended in insertion order, and updating a key's value does not change its position.
      # On Python 3.7+, the simpler approach (iterating over gro_list.items() directly) is safe to use.

      for k,v in sorted(gro_list.items(), key = lambda x:x[0].casefold()):
        print(f"{v} {k}")

      break 


if __name__ =="__main__":
  main()