import time

def countdown(seconds): 
    while seconds > 0:
        print(f"{seconds//60:02d}:{seconds%60:02d} ⏳", end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00 🛑\nTime's up! 🎉")

countdown(int(input("Set timer (seconds): ⏰ ")))
