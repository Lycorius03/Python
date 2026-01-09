def main():
  coke_machine()

def coke_machine():
  amount_due = 50
  while   amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    
    if insert_coin in [5, 10, 25]:
      amount_due -= insert_coin
      change_owed = abs(amount_due)
    else:
      continue

  print(f"Change Owed: {change_owed}") 

if __name__ == "__main__":
  main()
