C = 299792458  # Speed of light in meters per second

def main():
    mass = float(input("Enter kilos of mass: "))
    energy = mass * C**2
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!\n")

if __name__ == '__main__':
    main()
