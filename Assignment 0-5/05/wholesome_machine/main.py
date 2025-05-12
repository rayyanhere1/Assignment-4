def main():
    affirmation = "I am capable of doing anything I put my mind to."

    print("Please type the following affirmation:")

    while True:
        user_input = input().strip()

        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm. That was not the affirmation.")
            print("Please type the following affirmation:")

if __name__ == '__main__':
    main()
