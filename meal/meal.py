def main():
  time = input("What time is it? ").strip()
  time = convert(time)
  if time >= 7 and time <= 8:
    print("breakfast time")
  elif time >= 12 and time <= 13:
    print("lunch time")
  elif time >=18 and time <= 19:
     print ("dinner time")

def convert(time):
  if time.endswith("a.m.") or  time.endswith("p.m."):
   #12-hour times
      time_part, notation = time.split(" ")
      hours, minutes = time_part.split(":")
      match notation:
        # This is a.m.
        case n if n.endswith("a.m."):
          if hours == "12": 
            hours = float(hours) - 12
          else:
            hours = float(hours)
          minutes = float(minutes) / 60
          time = hours + minutes
        #  This is p.m.    
        case n if n.endswith("p.m."):
          if hours == "12":
            hours = float(hours)
          else:
            hours = float(hours) + 12
          minutes = float(minutes) / 60
          time = hours + minutes 

  else:
    #24-hour times 
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes) / 60
    time = hours + minutes

  return time

if __name__ == "__main__":
    main()