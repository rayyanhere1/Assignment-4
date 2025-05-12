def get_last_element(lst):
    print("\nThe last element in the list is:", lst[-1])

def main():
    lst = []
    n = int(input("How many elements do you want in the list? "))

    for _ in range(n):
        element = input("Enter an element: ")
        lst.append(element)

    print("\nList you created:", lst)
    get_last_element(lst)

if __name__ == '__main__':
    main()
