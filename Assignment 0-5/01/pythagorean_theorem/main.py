import math

def main():
    ab = float(input("Enter the length of AB :"))
    ac = float(input("Enter the length of AC :"))
    bc = math.sqrt(ab ** 2 + ac ** 2)
    print(f"\nThe length of BC (Hypotenuse) is : {bc} ")

if __name__ == '__main__':
    main()
