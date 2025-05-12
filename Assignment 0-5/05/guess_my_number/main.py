import random

def main():
    print("\nWelcome to the Guess My Number Game!\n")
    print("I am thinking of a number between 0 and 99...")

    number_to_guess = random.randint(0, 99)

    while True:
        try:
            guess = int(input("Enter a guess: ").strip())

            if guess < 0 or guess > 99:
                print("Please enter a number between 0 and 99.")
                continue

            if guess > number_to_guess:
                print("Your guess is too high")
            elif guess < number_to_guess:
                print("Your guess is too low")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()
