planet_gravity = {
    'Mercury': 0.376,
    'Venus': 0.889,
    'Mars': 0.378,
    'Jupiter': 2.360,
    'Saturn': 1.081,
    'Uranus': 0.815,
    'Neptune': 1.140
}

def calculate_planetary_weight(earth_weight, planet):
    if planet in planet_gravity:
        gravity = planet_gravity[planet]
        return round(earth_weight * gravity, 2)
    else:
        print(f"Oops! Looks like we don't have the gravity data for {planet}.")
        return None

def main():
    print("\n🚀 Welcome to the Cosmic Weight Calculator! 🌌")
    print("-------------------------------------------")
    
    try:
        earth_weight = float(input("💪 Enter your Earth weight (in kg): "))
        
        if earth_weight <= 0:
            print("Uh-oh! Please enter a valid weight greater than zero. 💥")
            return
        
        print("\n🎯 Let's pick a planet to calculate your weight on! 🌍")
        print("Here are the options you can choose from:")
        print("- Mercury")
        print("- Venus")
        print("- Mars")
        print("- Jupiter")
        print("- Saturn")
        print("- Uranus")
        print("- Neptune")
        
        planet = input("\n🚀 Enter the planet of your choice: ")
        
        if planet not in planet_gravity:
            print(f"Oops! We don't have data for {planet}. Please check your input! 😅")
            return
        
        planetary_weight = calculate_planetary_weight(earth_weight, planet)
        
        if planetary_weight is not None:
            print(f"\n🎉 Your weight on {planet} would be: {planetary_weight} kg! 🌟")
            print(f"Isn't that amazing? Your cosmic adventure just got more fun! ✨")

        print("\nThank you for using the Cosmic Weight Calculator! 🪐🌙")
    
    except ValueError:
        print("🚨 Oops! Looks like that wasn't a valid number for your weight. Please try again. 🛸")

if __name__ == "__main__":
    main()
