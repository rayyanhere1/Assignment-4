import random

def main():
    number = random.choice(range(1, 31))
    guess = None

    print("🎯 I'm thinking of a number from 1 to 30.")
    print("Can you guess it?")

    while guess != number:
        guess = input("➤ Your guess: ")

        if not guess.isdigit():
            print("⛔ Only numbers allowed!")
            continue

        guess = int(guess)

        if guess == number:
            print("✅ Correct! You guessed it! 🎉")
        elif abs(guess - number) <= 3:
            print("🔥 So close! Try again.")
        elif guess < number:
            print("📉 Too low.")
        else:
            print("📈 Too high.")

if __name__ == '__main__':
    main()
