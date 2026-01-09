import random


def main():
    level = get_level()

    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        attempts = 0
        while True:
            try:
              user_answer = input(f"{x} + {y} = ")
              corrcet_answer = x + y
              if int(user_answer) == corrcet_answer:
                  score += 1
                  break
                
              else:
                  print("EEE")
                  attempts += 1
                            
            except ValueError:
                attempts += 1
                print("EEE")
        
            if attempts == 3:
              print(f"{x} + {y} = {corrcet_answer}")
              break

    print(f"Score: {score}")   
        

def get_level():
    while True:
      try:
          n = int(input("Level: "))
          if n in [1, 2, 3]:
            return n

      except ValueError:
          pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError("Level must be 1, 2, or 3")


if __name__ == "__main__":
    main()