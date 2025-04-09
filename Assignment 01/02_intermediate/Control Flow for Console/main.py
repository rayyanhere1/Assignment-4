import random
import time

NUM_ROUNDS = 5

def print_slow(str, delay=0.05):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

def play_round(round_num, score):
    print(f"\nRound {round_num}")
    time.sleep(1)
    
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    
    print(f"\nYour number is {your_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ['higher', 'lower']:
        print("Please enter either 'higher' or 'lower'.")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

    print("Thinking... 🧠")
    time.sleep(1)
    
    if (guess == 'higher' and your_number > computer_number) or (guess == 'lower' and your_number < computer_number):
        print(f"You were right! 🎉 The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. 😞 The computer's number was {computer_number}")
    
    print(f"Your score is now {score} 🏅")
    return score

def print_end_message(score):
    if score == NUM_ROUNDS:
        print("\nWow! You played perfectly! 👑")
    elif score >= NUM_ROUNDS // 2:
        print("\nGood job, you played really well! 👍")
    else:
        print("\nBetter luck next time! 🤞")

def print_scoreboard(score):
    print(f"\nFinal Scoreboard: You won {score} out of {NUM_ROUNDS} rounds.")
    print("-" * 30)
    if score == NUM_ROUNDS:
        print("You are a High-Low Champion! 👑")
    elif score >= NUM_ROUNDS // 2:
        print("Great effort! You did really well! 🏅")
    else:
        print("Not bad, but there's room for improvement! 💪")

def main():
    print("\nWelcome to the High-Low Game! 🎮")
    print("--------------------------------")
    
    score = 0
    time.sleep(1)
    
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)
    
    print("\nThanks for playing! 🎉")
    print_end_message(score)
    print_scoreboard(score)

if __name__ == "__main__":
    main()
