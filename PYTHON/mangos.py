def main():
    num_mangos = int(input("Number of mangos you wanna buy: "))
    print(mango(num_mangos, 3))

def mango(num_mangos, price_mango):
    if num_mangos < 3:
        return f"{num_mangos * price_mango} $"
    elif (num_mangos % 3 == 0):
        return f"{(num_mangos // 3 * 2) * price_mango} $"
    else:
        return f"{(num_mangos // 3 * 2 + num_mangos % 3) * price_mango} $"
        
        
if __name__ == "__main__":
    main()