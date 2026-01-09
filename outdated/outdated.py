def main():
  outdated()

def outdated():
  months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
  while True:
    date = input("Date: ").strip()
    try:
      if '/' in date:
        month,day,year = date.split('/')
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
          print(f"{int(year):04}-{int(month):02}-{int(day):02}")
          break

      elif "," in date:
        month,day,year = date.replace(',',' ').split()
        if month in months:
          m = months.index(month) + 1
          d = int(day)
          if d >= 1 and d <= 31:
            print(f"{int(year):04}-{m:02}-{d:02}")
            break


    except (ValueError, IndexError):
      pass

if __name__ == "__main__":
  main()