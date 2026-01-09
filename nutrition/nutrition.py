def main():
  item = input("Item: ").strip().lower()
  calorie = calories(item)
  if calorie:
    print(f"Calories: {calorie}")
  
def calories(item):
  facts = {"apple":"130", 
           "avocado":"50",
           "banana":"110",
           "cantaloupe":"50",
           "grapefruit":"60",
           "grapes":"90",
           "honeydew melon":"50",
           "kiwifruit":"90",
           "lemon":"15",
           "lime":"20",
           "nectarine":"69",
           "orange":"80",
           "peach":"60",
           "pear":"100",
           "pineapple":"50",
           "plums":"70",
           "strawberris":"50",
           "sweet cherries":"100",
           "tangerine":"50",
           "watermelon":"80"}
  if item in facts:
    return facts[item]
  
if __name__ == "__main__":
  main()