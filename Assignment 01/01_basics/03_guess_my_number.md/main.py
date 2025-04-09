import random
import time


def fade_print(message, delay=0.05):
    print(message)
    time.sleep(delay)

def main():
    print("\n🌟 Welcome to the Ultimate 'Guess My Number' Challenge! 🌟")
    time.sleep(1)
    fade_print("I'm thinking of a number between 0 and 99... 🤔 Let's see if you can crack it! 🚀")

    number_to_guess = random.randint(0, 99)
    guess = -1
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("\n🔢 Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            fade_print("🔽 Oops! Your guess is too low. Try guessing a bigger number!")
            time.sleep(0.5)
        elif guess > number_to_guess:
            fade_print("🔼 Hmm! Your guess is too high. Try guessing a smaller number!")
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            fade_print(f"\n🎉🎉 **CONGRATS!** You guessed it right! 🎉 The number was: {number_to_guess} 🎉")
            fade_print(f"\n👏 You guessed the number in {attempts} attempts! Well done, champion! 👏")
            time.sleep(1)

    fade_print("\n💥 **Game Over!** Wanna play again? 💥")

if __name__ == "__main__":
    main()
