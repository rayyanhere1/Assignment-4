def main():
    num_1 = int(input("Please enter an integer to be divided: "))
    num_2 = int(input("Please enter an integer to divide by: "))

    quotient = num_1 // num_2
    remainder = num_1 % num_2

    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()
