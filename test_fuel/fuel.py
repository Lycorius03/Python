def main():
    while True:
        fraction_str = input("Fraction: ")
        try:
            percentage_int = convert(fraction_str)
            break 
        except (ValueError, ZeroDivisionError):
            pass 
            
    print(gauge(percentage_int))


def convert(fraction):
    x_str, y_str = fraction.split("/")
    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError
    
    if x < 0 or y < 0:
        raise ValueError
    
    if x > y:
        raise ValueError
        
    return int(round((x / y) * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
