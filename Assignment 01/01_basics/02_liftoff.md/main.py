import time

def main():
    print("\n🎬 Initiating Spacecraft Launch Sequence... 🌌")
    print("\n🚀 Ready for Liftoff? Countdown starting now... ⏳")
    time.sleep(1)
    
    for i in range(10, 0, -1):
        print(f"\n⏰ T-{i} seconds", end="")
        time.sleep(1)
    
    print("\n\n🌠 3... 2... 1... 🚀 LIFTOFF! 🌟\n")
    print("The spacecraft has launched into the cosmos... 🌌✨")
    
if __name__ == "__main__":
    main()
