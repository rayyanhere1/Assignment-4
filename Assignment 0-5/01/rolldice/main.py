import random
def main():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print(f"Roll 1 is : {die1}")
    print(f"Roll 2 is : {die2}")
    print(f"Total is : {die1 + die2}")

if __name__ == '__main__':
    main()    