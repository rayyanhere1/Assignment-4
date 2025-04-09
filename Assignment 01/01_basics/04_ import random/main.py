import random
import time

def main():
    print("\n🎲 Welcome to the **Random Number Generator**! 🎲")
    time.sleep(0.5)
    print("Generating 10 random numbers between 1 and 100... Let's see what we get! 🤩")
    time.sleep(1)

    random_numbers = [random.randint(1, 100) for _ in range(10)]
    
    print("\nHere are the random numbers for you:")
    time.sleep(0.5)
    for num in random_numbers:
        print(num)
        time.sleep(0.3)

    print("\n💥 Random numbers generated successfully! 💥")

if __name__ == "__main__":
    main()
