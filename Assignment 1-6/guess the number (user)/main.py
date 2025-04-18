import random

def main():
    low = 1
    high = 50
    tries = 0

    print("Think of a number between 1 and 50.")
    input("Press Enter when you're ready... 🤔")

    while True:
        guess = random.randint(low, high)
        tries += 1
        print(f"My guess is: {guess}")

        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"🎉 I got it in {tries} tries! I'm a genius! 😎")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Please type only h, l, or c.")

if __name__ == '__main__':
    main()
