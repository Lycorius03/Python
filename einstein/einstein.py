def E(m,c = 3000000):
    E = m * pow(c,2)
    return E

def main():    
    m = int(input("m："))
    e = E(m)
    print(f"E:{e}")

main()