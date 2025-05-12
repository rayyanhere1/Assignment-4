def num_in_stock(fruit):
    # This is a sample inventory of fruits
    inventory = {
        "apple": 50,
        "banana": 100,
        "pear": 1000,
        "mango": 200,
        "orange": 150
    }

    # Return the number of fruits in stock for the given fruit, or 0 if it's not found
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip()

    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()
