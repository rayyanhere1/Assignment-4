import random

NUM_SIDES = 6

def roll_dice(attempt):
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Roll {attempt}: Die1 = {die1}, Die2 = {die2}, Total = {total}")

def main():
    for i in range(1, 4):
        roll_dice(i)

if __name__ == '__main__':
    main()
