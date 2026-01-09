def main():
  fuels = gauge("Faction: ")
  print(f"{fuels}")

def gauge(prompt):
  while True:
    try:
      X,Y = input(prompt).split('/')
      X,Y = int(X),int(Y)
      fuels = 100 / Y * X
      if X < 0 or Y < 0:
        pass
      elif fuels <= 1:
        return "E"
      elif X > Y:
        pass
      elif fuels >= 99 :
        return "F"
      else:
        return f"{fuels:.0f}%"

    except ValueError:
      pass

    except ZeroDivisionError:
      pass

if __name__ == "__main__":
  main()