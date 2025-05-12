def main():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()
