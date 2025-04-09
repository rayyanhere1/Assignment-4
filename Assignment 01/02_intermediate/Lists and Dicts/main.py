def main():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(f"\nHere’s your starting fruit list: {fruit_list}")
    print(f"✨ The list contains {len(fruit_list)} fruits right now. ✨\n")
    fruit_list.append('mango')
    print(f"💥 You added 'mango' to the fruit list!")
    print(f"🍉 Updated Fruit List: {fruit_list}")
    print(f"🎉 New list length: {len(fruit_list)}\n")


def index_game():
    elements = [3, 'apple', 14.5, 'banana', True]
    print("\nCurrent List:", elements)

    def access_element(lst, index):
        try:
            return lst[index]
        except IndexError:
            return "Index out of range!"

    def modify_element(lst, index, new_value):
        try:
            lst[index] = new_value
            return lst
        except IndexError:
            return "Index out of range!"

    def slice_list(lst, start, end):
        try:
            return lst[start:end]
        except IndexError:
            return "Index out of range!"

    action = input("\nWhat would you like to do? Choose: 'Access', 'Modify', or 'Slice': ").lower()

    if action == "access":
        index = int(input("Enter index to access (0-4): "))
        print(f"Accessing index {index}: {access_element(elements, index)}")
    elif action == "modify":
        index = int(input("Enter index to modify (0-4): "))
        new_value = input("Enter the new value: ")
        print(f"Modifying index {index} to {new_value}. Updated list: {modify_element(elements, index, new_value)}")
    elif action == "slice":
        start = int(input("Enter the start index (0-4): "))
        end = int(input("Enter the end index (1-5): "))
        print(f"Slicing from {start} to {end}: {slice_list(elements, start, end)}")
    else:
        print("\nPlease choose a valid operation: 'Access', 'Modify', or 'Slice'.")


def play_game():
    main()
    index_game()


if __name__ == "__main__":
    play_game()
