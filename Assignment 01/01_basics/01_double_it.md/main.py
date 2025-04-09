import time

def main():
    print("\n🔢 Welcome to the Magic Doubler! 🔢")
    curr_value = int(input("\n✨ Enter a number and watch the magic unfold: "))
    
    results = []
    
    print("\n🌀 Doubling in progress...\n")
    time.sleep(1)  # Thoda suspense add karna

    while curr_value < 100:
        curr_value *= 2
        results.append(str(curr_value))
        print(f"➡ {curr_value}")  
        time.sleep(0.5)  # Smooth effect

    print("\n🎉 Boom! We reached or crossed 100! 🎉")
    print("Final Sequence:", " → ".join(results))

if __name__ == "__main__":
    main()
