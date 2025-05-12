def main():
    lst = []

    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        lst.append(value)
    
    print("\nHere's the list:", lst)

if __name__ == '__main__':
    main()
