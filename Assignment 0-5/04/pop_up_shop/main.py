def main():
    print("\nWelcome to the Premium Fruit Shop Calculator!\n")

    fruit_prices = {
        'apple': 3.5,
        'durian': 15.0,
        'jackfruit': 25.0,
        'kiwi': 4.0,
        'rambutan': 2.5,
        'mango': 5.0
    }

    total_cost = 0
  
    for fruit, price in fruit_prices.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: ").strip())
                if quantity < 0:
                    print("Quantity cannot be negative. Please enter a valid number.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    print("\nYour total is $" + str(round(total_cost, 2)))

if __name__ == '__main__':
    main()
