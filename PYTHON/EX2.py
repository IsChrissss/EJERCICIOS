def main():
    print(factorial(int(input("Write a number: "))))
    print(factorial(9))

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)
    
if __name__ == "__main__":
    main()