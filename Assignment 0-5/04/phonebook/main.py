def main():
    phonebook = {}

    print("Phonebook Application")
    print("---------------------")

    while True:
        print("\nChoose an option:")
        print("1. Add a contact")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("4. Display all contacts")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            phonebook[name] = phone
            print(f"{name} has been added to the phonebook.")

        elif choice == "2":
            name = input("Enter the name to search: ")
            if name in phonebook:
                print(f"{name}'s phone number is {phonebook[name]}.")
            else:
                print("Contact not found.")

        elif choice == "3":
            name = input("Enter the name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"{name} has been deleted from the phonebook.")
            else:
                print("Contact not found.")

        elif choice == "4":
            if not phonebook:
                print("The phonebook is empty.")
            else:
                print("\nPhonebook Contacts:")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")

        elif choice == "5":
            print("Exiting the phonebook application.")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()
