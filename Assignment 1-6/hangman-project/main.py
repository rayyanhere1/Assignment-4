import random

def main():
    word_list = ["python", "java", "hangman", "coding", "programming", "developer"]
    word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("🔒 Welcome to Hangman! Guess the word!")
    print("You have 6 tries to guess the word.")

    while tries > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Word: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Tries left: {tries}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("🔄 You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Incorrect guess!")
            tries -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"🎉 You guessed the word '{word}'! You win!")
            break
    else:
        print(f"💀 You lost! The word was '{word}'.")

if __name__ == '__main__':
    main()
